# LaborAI

LaborAI es una aplicación web diseñada para proporcionar respuestas rápidas y precisas a consultas sobre legislación laboral argentina. Utiliza el modelo Ollama ajustado con BERT para la generación de pares de preguntas y respuestas, basándose en datos que comprenden cuatro leyes completas de la legislación laboral argentina.

## Descripción

LaborAI utiliza tecnologías avanzadas de procesamiento del lenguaje natural (NLP) para entender y responder preguntas sobre la legislación laboral argentina. El backend de la aplicación está construido con FastAPI y Uvicorn, mientras que el frontend está desarrollado con Angular y Tailwind CSS.

## Herramientas Utilizadas

### Backend

- **FastAPI**: Framework moderno para construir APIs con Python.
- **Uvicorn**: Servidor ASGI de alto rendimiento para ejecutar aplicaciones FastAPI.
- **LangChain**: Biblioteca para la construcción de aplicaciones de lenguaje natural.
- **Ollama**: Modelo de lenguaje utilizado para procesar y generar respuestas.
- **HuggingFace Transformers**: Biblioteca para embeddings y modelos de NLP.
- **Chroma**: Base de datos de vectores para búsquedas eficientes.
- **BeautifulSoup**: Biblioteca para la extracción de datos de archivos HTML y XML.
- **AsyncHtmlLoader**: Cargador asíncrono para documentos HTML.

### Frontend

- **Angular**: Framework de desarrollo web basado en TypeScript.
- **Tailwind CSS**: Framework de CSS para diseño moderno y responsivo.
- **RxJS**: Biblioteca para programación reactiva en Angular.
- **LocalStorage**: API de almacenamiento web para mantener el historial de chat.

## Instalación y Ejecución

### Backend

1. **Clonar el Repositorio**

    ```bash
    git clone <repository_url>
    cd laborAI
    ```

2. **Crear un Entorno Virtual de Python**

    ```bash
    python -m venv .venv
    ```

3. **Instalar los Requisitos**

    ```bash
    .venv/bin/pip install -r requirements.txt
    ```

4. **Activar el Entorno Virtual**

    ```bash
    # Windows Command Prompt
    .venv\Scripts\activate.bat

    # Windows PowerShell
    .venv\Scripts\Activate.ps1

    # macOS y Linux
    source .venv/bin/activate
    ```

5. **Instalar y Configurar Ollama**

    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ollama serve &
    ollama pull llama3-chaqa
    ```

6. **Ejecutar la Aplicación FastAPI**

    ```bash
    uvicorn api:app --reload
    ```

### Frontend

1. **Navegar al Directorio del Frontend**

    ```bash
    cd frontend
    ```

2. **Instalar las Dependencias de Angular**

    ```bash
    npm install
    ```

3. **Ejecutar la Aplicación Angular**

    ```bash
    ng serve
    ```

4. **Acceder a la Aplicación**

    Abra su navegador y navegue a `http://localhost:4200`.

## Uso

1. **Ingresar una Pregunta**: En el campo de entrada, escriba su pregunta sobre la legislación laboral argentina.
2. **Enviar la Pregunta**: Presione el botón "Send" para enviar la pregunta.
3. **Ver la Respuesta**: La respuesta de LaborAI se mostrará en el historial del chat.
4. **Mostrar/Ocultar Contexto**: Si la respuesta incluye contexto adicional, se mostrará debajo de la respuesta.
5. **Limpiar el Historial**: Para limpiar el historial del chat, presione el botón "Clear Chat".

## Contribuciones

Las contribuciones son bienvenidas. Por favor, cree un fork del repositorio y envíe un pull request con sus cambios.



Este README proporciona una guía completa sobre cómo instalar, configurar y ejecutar LaborAI, así como una descripción de las herramientas utilizadas y las funcionalidades clave de la aplicación.
