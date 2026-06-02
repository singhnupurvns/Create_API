# 🤖 LLM API — FastAPI + Ollama + Gemma4

A lightweight, production-style REST API that integrates a locally running Large Language Model (Gemma4 via Ollama) with API key authentication and a credits-based access control system — built entirely with Python.

---

## ✨ Features

- 🔐 **Custom API Key Authentication** — every request is validated via `x-api-key` header
- 💳 **Credits System** — each API key has limited usage credits
- 🧠 **LLM Integration** — powered by Gemma4 running locally via Ollama
- ⚡ **FastAPI** — async, high-performance Python web framework
- 🧪 **Postman Ready** — easily testable with Postman or any HTTP client

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [FastAPI](https://fastapi.tiangolo.com/) | Web framework & API routing |
| [Ollama](https://ollama.com/) | Local LLM runner |
| Gemma4 (`gemma4:e2b`) | Language model |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |
| [uv](https://github.com/astral-sh/uv) | Fast Python package manager |

---

## 📁 Project Structure

```
API_LLM_GEMMA/
├── main.py           # FastAPI app — routes, auth, LLM call
├── requirements.txt  # Python dependencies
├── .env              # API key (never commit this!)
└── .gitignore        # Ignores .env and __pycache__
```

---

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com/download) installed and running
- Gemma4 model pulled locally

```bash
ollama pull gemma4:e2b
```

### 2. Clone the repo

```bash
git clone https://github.com/singhnupurvns/Create_API.git
cd Create_API
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Or with `uv`:

```bash
uv run uvicorn main:app --reload
```

### 4. Set up your `.env` file

Create a `.env` file in the root directory:

```env
API_KEY=your_secret_key_here
```

> ⚠️ Never share or commit your `.env` file.

### 5. Run the server

```bash
uvicorn main:app --reload
```

Server starts at: `http://127.0.0.1:8000`

---

## 📡 API Reference

### `GET /generate`

Generate a response from the LLM using a prompt.

**Headers**

| Key | Value |
|-----|-------|
| `x-api-key` | Your secret API key |

**Query Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `prompt` | `string` | The input text sent to the LLM |

**Example Request**

```
GET http://localhost:8000/generate?prompt=What is Python?
```

**Success Response** `200 OK`

```json
{
  "response": "Python is a high-level, interpreted programming language..."
}
```

**Error Response** `401 Unauthorized`

```json
{
  "detail": "Invalid API Key or insufficient credits"
}
```

---

## 🧪 Testing with Postman

1. Open Postman
2. Set method to `GET`
3. Enter URL: `http://localhost:8000/generate?prompt=hello world`
4. Go to **Headers** tab
5. Add:
   - Key: `x-api-key`
   - Value: `your_secret_key_here`
6. Click **Send**

---

## 🔒 How Authentication Works

```
Request → x-api-key header
         ↓
    Validate key exists in API_KEYS_CREDITS
         ↓
    Check credits > 0
         ↓
    Deduct 1 credit → forward to Ollama → return response
```

Each API key starts with **5 credits**. Once exhausted, the key returns `401 Unauthorized`.

---



---

## 🙋‍♀️ Author

**Nupur Singh**  
[GitHub](https://github.com/singhnupurvns) · [LinkedIn](https://linkedin.com/in/singhnupurvns)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
