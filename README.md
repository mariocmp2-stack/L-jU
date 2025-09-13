# Synapse - Conversational API

Synapse is a project that provides a conversational API layer for web services, allowing both humans and AI agents to interact with them through natural language or structured intents.

This initial version sets up a basic FastAPI application with a single endpoint for handling intents.

## Features

-   **Intent Handling:** A core `/intent` endpoint to process actions.
-   **Structured Responses:** Returns predictable JSON responses.
-   **API Key Authentication:** The endpoint is secured and requires an API key.
-   **Mocked Logic:** Simulates a `search_product` action for demonstration.

## Setup and Installation

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

Use `uvicorn` to run the FastAPI application:

```bash
uvicorn synapse.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## How to Test

You can test the `/intent` endpoint using a tool like `curl`. You must include the `X-API-KEY` header for authentication.

**API Key:** `synapse-secret-key`

### Example: Successful `search_product` request

```bash
curl -X POST "http://127.0.0.1:8000/intent" \
-H "Content-Type: application/json" \
-H "X-API-KEY: synapse-secret-key" \
-d '{
  "action": "search_product",
  "query": "proteína vegana"
}'
```

### Example: Unsupported action request

```bash
curl -X POST "http://127.0.0.1:8000/intent" \
-H "Content-Type: application/json" \
-H "X-API-KEY: synapse-secret-key" \
-d '{
  "action": "delete_database",
  "query": "all of it"
}'
```

### Example: Missing API Key

```bash
curl -X POST "http://127.0.0.1:8000/intent" \
-H "Content-Type: application/json" \
-d '{
  "action": "search_product",
  "query": "proteína vegana"
}'
```
