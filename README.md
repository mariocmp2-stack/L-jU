# 🧠 Synapse - Conversational API Gateway for AI Agents

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

**Synapse** is a conversational API layer designed to bridge the gap between AI Agents (or natural language users) and traditional web services.

Instead of forcing AI models to learn complex REST or GraphQL routing, Synapse provides a single unified entry point (`/intent`). It receives structured intents, executes the backend logic, and returns a predictable, standardized JSON response so your AI always knows if it succeeded.

## ✨ Features (MVP)

- ⚡️ **High Performance:** Built on modern **FastAPI**.
- 🧠 **Intent Routing:** A core `/intent` endpoint to process classified actions natively.
- 🔒 **Secure:** Endpoints secured with API Keys, managed cleanly via environment variables using `pydantic-settings`.
- 🐳 **Production Ready:** Ships with a `Dockerfile` pre-configured with Gunicorn and Uvicorn workers, ready for immediate deployment.

---

## 🚀 Quickstart

Get Synapse running locally in less than 3 minutes.

### 1. Clone & Setup
```bash
git clone <repository-url>
cd <repository-directory>
cp .env.example .env
```
*(Make sure to update the `api_key` inside `.env` for production)*

### 2. Run with Docker (Recommended)
```bash
docker build -t synapse-api .
docker run -p 8000:8000 synapse-api
```
*(Alternatively, run locally with `pip install -r requirements.txt` and `uvicorn synapse.main:app --reload`)*

### 3. Test the flow!

Send an intent request (make sure to use the API key you set in your `.env` file, default is `synapse-secret-key` in `.env.example`):

```bash
curl -X POST "http://127.0.0.1:8000/intent" \
-H "X-API-KEY: synapse-secret-key" \
-H "Content-Type: application/json" \
-d '{
  "action": "search_product",
  "query": "proteína vegana"
}'
```

---

## 🏗 Architecture & Project Structure

- `synapse/main.py`: Core routing and dependency injection.
- `synapse/actions.py`: Business logic separated from HTTP transport.
- `synapse/models.py` & `schemas.py`: Strict database schemas and Pydantic validation.
- `synapse/config.py`: Environment variable and secrets management using `pydantic-settings`.

## 🛣 Roadmap & Contributing

Synapse is currently an MVP, but the architecture is ready to scale. We are actively looking for contributors!

**Next major milestones:**
- [ ] Integrate native LLM Support (OpenAI / Anthropic SDKs) to replace static intent requirements with raw text parsing.
- [ ] Add Database Integration (e.g. SQLAlchemy, Redis) for faster, scalable session context management.
- [ ] Implement JWT/OAuth2 user authentication for personalized requests.
- [ ] Build a plugin architecture to easily connect to Stripe, Shopify, or custom CRMs.

### Want to help?
Look for issues tagged with `good first issue` or `help wanted`. Feel free to fork the repository, open a Pull Request, or start a discussion.

## 📝 License
This project is licensed under the MIT License.
