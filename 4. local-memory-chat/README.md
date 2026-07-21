# Local Memory Chat

A personal chat assistant that runs entirely offline and remembers you across sessions, using [Hindsight](https://github.com/vectorize-io/hindsight) for long-term memory instead of just replaying raw chat logs.

## Overview

Local Memory Chat is a Flask chat app backed by two fully local pieces:

- **Ollama** — runs the conversational LLM on your machine, no cloud calls
- **Hindsight** (embedded mode) — a local memory system with three operations:
  - **Retain**: after every exchange, the conversation is stored and Hindsight extracts durable facts from it (entities, relationships, context)
  - **Recall**: before replying, the app looks up memories relevant to what you just said and feeds them to the model as context
  - **Reflect**: a "What do you remember about me?" button that asks Hindsight to reason over everything it has stored and summarize it

Unlike the other projects in this portfolio, this one does **not** use the shared root `.env` / `GROQ_API_KEY` — there's no cloud API key involved at all. Everything runs on-device.

## Technology Stack

- **Python 3.10+**
- **Flask** — web chat interface
- **Ollama** — local LLM inference
- **hindsight-all** — embedded Hindsight server + client (local Postgres, local embeddings, local reranker)
- **python-dotenv** — environment variable management

## Prerequisites

- Python 3.10 or higher
- [Ollama](https://ollama.com) installed and running (`ollama serve`)
- ~5 GB free disk for the local model

## Installation

### 1. Clone or Download

```bash
git clone <repository-url>
cd "4. local-memory-chat"
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Pull a Tool-Calling Model

Hindsight's `reflect` operation is an agentic loop that relies on tool/function calling. Not every Ollama model supports that — `gemma3` in particular does **not**, and reflect degrades to a low-quality forced answer if you use it. `qwen2.5:7b` was tested and works correctly for both chat and Hindsight's internal reasoning:

```bash
ollama pull qwen2.5:7b
```

### 5. Configure Environment Variables (optional)

This project ships sensible defaults and doesn't require any secrets. If you want to override the model, memory profile name, or bank id, copy the template:

```bash
cp .env.example .env
```

```
OLLAMA_MODEL=qwen2.5:7b
OLLAMA_BASE_URL=http://localhost:11434
HINDSIGHT_PROFILE=local-memory-chat
HINDSIGHT_BANK_ID=default-user
FLASK_SECRET_KEY=change-me
DEBUG=false
```

## Usage

Make sure Ollama is running first:

```bash
ollama serve
```

Then start the app:

```bash
python app.py
```

**The very first run takes 30-90+ seconds** with no output while it initializes the embedded database from scratch (`initdb`) — this is normal, not a freeze. Wait for `Running on http://127.0.0.1:5000` in the terminal before opening the page. Every run after the first reuses that database and starts in a couple of seconds.

Stop the app with **Ctrl+C** (not `kill -9` / force quit) so the embedded database shuts down cleanly — a hard kill can leave orphaned Postgres processes running in the background, which can then block the next `python app.py` from starting cleanly. If that happens, find and stop them with:

```bash
pg_ctl -D ~/.pg0/instances/local-memory-chat/data stop -m fast
```

Open `http://127.0.0.1:5000`, chat normally, and click **"What do you remember about me?"** at any point to see Hindsight reflect on what it has learned. Memory persists across restarts — the embedded database lives at `~/.pg0/instances/local-memory-chat/`, so closing and reopening the app doesn't lose anything.

## Project Structure

```
.
├── app.py               # Flask app: chat + reflect endpoints, Hindsight + Ollama wiring
├── requirements.txt     # Python dependencies
├── .env.example          # Environment variable template (no secrets needed)
├── templates/
│   └── index.html       # Chat UI
└── static/
    └── style.css         # Page styling
```

## How It Works

1. **Startup**: the app launches an embedded Hindsight server in-process (`HindsightServer`, using local Postgres via `pg0`), pointed at the local Ollama model for its own fact-extraction and reflection calls.
2. **Message in**: `client.recall(...)` retrieves memories relevant to the new message.
3. **Reply**: the recalled memories are added as system context, and the local Ollama model generates the reply.
4. **Message out**: the exchange is sent to `client.retain(..., retain_async=True)`, which extracts and stores durable facts in the background without blocking the response.
5. **Reflect**: the "what do you remember about me" button calls `client.reflect(...)`, which reasons over stored memories (using tool calls to search them) and returns a natural-language summary.

## Troubleshooting

**"does not support tools" errors in the logs**
```bash
# Your OLLAMA_MODEL doesn't support function calling - switch to a model that does
ollama pull qwen2.5:7b
```

**Can't connect to Ollama**
```bash
ollama serve
ollama list   # confirm the model is pulled
```

**Reset memory**
```bash
# Deletes the local embedded database for this project
rm -rf ~/.pg0/instances/local-memory-chat
```

**App seems frozen right after `python app.py`**
This is expected on the very first run only (see Usage above) — it's initializing the embedded database, not hung. Give it up to 90 seconds. If a *later* run hangs the same way, you likely have an orphaned Postgres process from a previous hard kill (see below).

**Next run won't start / port conflicts after a force-quit**
```bash
# Cleanly stop any leftover embedded Postgres process, then retry
pg_ctl -D ~/.pg0/instances/local-memory-chat/data stop -m fast
```

**Import Errors**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

## License

This project is provided as-is for educational and research purposes.

## Author

Developed by Anas AlGhannam

## Acknowledgments

- Vectorize for Hindsight
- Ollama for local LLM inference
- Flask for the web framework
