import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_community.document_transformers import BeautifulSoupTransformer
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.llms.ollama import Ollama
from langchain.vectorstores import Chroma

from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough
)
from langchain.schema.output_parser import StrOutputParser
import os

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
MODEL = "llama3-chatqa"

PROMPT_TEMPLATE = """
Responda en español a la siguiente pregunta:

{question}

, basándose en el siguiente contexto: {context}
"""

links = [
    "https://www.argentina.gob.ar/normativa/nacional/ley-20744-25552/actualizacion",
    "https://www.argentina.gob.ar/normativa/nacional/ley-24013-412/actualizacion",
    "https://www.argentina.gob.ar/normativa/nacional/ley-24557-27971/actualizacion",
    "https://www.argentina.gob.ar/normativa/nacional/ley-11544-63368/actualizacion"
]

titles = [
    "REGIMEN DE CONTRATO DE TRABAJO LEY N° 20.744",
    "EMPLEO Ley Nº 24.013",
    "RIESGOS DEL TRABAJO LEY N° 24.557",
    "JORNADA DE TRABAJO Ley 11.544"
]

def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)

def download_documents():
    loader = AsyncHtmlLoader(links)
    docs = loader.load()
    return docs

def get_dataset():
    docs = download_documents()
    print("Texto legal descargado.")
    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(docs, tags_to_extract=["article"])

    documents = []
    for i in range(len(docs_transformed)):
        metadata = {"title": titles[i], "source": links[i]}
        d = Document(metadata=metadata, page_content=docs_transformed[i].page_content)
        documents.append(d)

    chunks = split_documents(documents)
    print("Documentos creados.")
    return chunks

def create_or_load_database():
    collection_name = "laborAI_db"
    db_directory = f"./{collection_name}"

    embedding = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    if not os.path.exists(db_directory):
        print("Inicio de proceso de creación de base de datos.")
        os.makedirs(db_directory)
        chunks = get_dataset()
        database = Chroma.from_documents(chunks, embedding=embedding, collection_name=collection_name, persist_directory=db_directory)
        print("Base de datos CREADA y cargada exitosamente.")
    else:
        database = Chroma(collection_name=collection_name, embedding_function=embedding, persist_directory=db_directory)
        print("Base de datos cargada exitosamente.")

    return database

def get_rag_chain(retriever):
    llm = Ollama(model=MODEL)
    retrieval = RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    chain = retrieval | prompt | llm | StrOutputParser()
    return chain

database = create_or_load_database()
print("Hay ", database._collection.count(), " elementos en la base de datos ")
retriever = database.as_retriever(search_type="mmr", search_kwargs={'k': 5, 'fetch_k': 50})
chain = get_rag_chain(retriever)

class QuestionRequest(BaseModel):
    question: str

@app.put("/get_answer")
async def ask_question(request: QuestionRequest):
    question = request.question
    try:
        result = chain.invoke(question)
        contexts = [docs.page_content for docs in retriever.get_relevant_documents(question)]
        return {"answer": result, "context": contexts}
    except Exception as e:
        logger.error(f"Error processing request: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
