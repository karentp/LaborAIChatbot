# LaborAI API Backend

## Initial Setup

1. **Clone this Repository**

    ```bash
    git clone <repository_url>
    cd laborAI
    ```

2. **Create a Python Virtual Environment**

    ```bash
    python -m venv .venv
    ```

3. **Install the Requirements**

    ```bash
    .venv/bin/pip install -r requirements.txt
    ```

4. **Activate Your Virtual Environment**

    ```bash
    # Windows Command Prompt
    .venv\Scripts\activate.bat

    # Windows PowerShell
    .venv\Scripts\Activate.ps1

    # macOS and Linux
    source .venv/bin/activate
    ```

## Ollama Setup

1. **Install Ollama**

    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ```

2. **Run Ollama Server**

    ```bash
    ollama serve &
    ```

3. **Download the Model**

    ```bash
    ollama pull llama3-chatqa
    ```

## Running the API

1. **Ensure Ollama is Running**

    Make sure the Ollama server is running:

    ```bash
    ollama serve &
    ```

2. **Run the FastAPI Application**

    ```bash
    uvicorn api:app --reload
    ```

## Making Requests

### Using `curl`

To make a POST request using `curl`, use the following command:

```bash
curl -X POST "http://localhost:8000/get_answer" -H "Content-Type: application/json" -d '{"question": "¿Cuáles son los derechos de los trabajadores según la ley 20.744?"}'
