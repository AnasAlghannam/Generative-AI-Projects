import os
import re

import ollama
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request, session
from hindsight import HindsightClient, HindsightServer

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:7b")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
HINDSIGHT_PROFILE = os.getenv("HINDSIGHT_PROFILE", "local-memory-chat")
BANK_ID = os.getenv("HINDSIGHT_BANK_ID", "default-user")

SYSTEM_PROMPT = (
    "You are a warm, concise personal assistant. Use the memories provided below "
    "to personalize your reply when relevant, but don't force it in if the "
    "question doesn't call for it. Respond only in English."
)

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key")

# Embedded Hindsight server: local Postgres (pg0), local embeddings, local
# reranker. The LLM Hindsight itself uses for extraction/reflection also
# points at the same local Ollama model, so nothing here touches the network.
hindsight_server = HindsightServer(
    db_url=f"pg0://{HINDSIGHT_PROFILE}",
    llm_provider="ollama",
    llm_api_key="ollama",
    llm_model=OLLAMA_MODEL,
    llm_base_url=f"{OLLAMA_BASE_URL}/v1",
    log_level="warning",
)
hindsight_server.start(timeout=120)


def get_hindsight_client() -> HindsightClient:
    # A fresh client is created per call rather than reused across requests:
    # the generated client caches an aiohttp session on first use bound to
    # whichever asyncio loop is active at that moment, which breaks once
    # Flask's dev server serves a later request on a different loop/thread.
    return HindsightClient(base_url=hindsight_server.url)


def clean_markdown(text: str) -> str:
    """Strip markdown syntax and stray agent artifacts so a response reads as plain text."""
    # Drop fenced code blocks - the model tends to restate the same summary
    # inside one, and occasionally leaks raw tool-call syntax there too.
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    # Drop a leaked tool-call fragment left dangling on its own line, e.g. done("...", [...])
    text = re.sub(r"^\s*[A-Za-z_]\w*\([^\n]*\)\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"^[-*]\s+", "• ", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def recall_context(user_message: str) -> str:
    recall = get_hindsight_client().recall(bank_id=BANK_ID, query=user_message, budget="low")
    if not recall.results:
        return ""
    memories = "\n".join(f"- {r.text}" for r in recall.results)
    return f"Relevant memories about the user:\n{memories}"


@app.route("/")
def index():
    session.setdefault("history", [])
    return render_template("index.html", history=session["history"])


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    context = recall_context(user_message)

    history = session.get("history", [])
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    if context:
        messages.append({"role": "system", "content": context})
    messages += history[-10:]
    messages.append({"role": "user", "content": user_message})

    response = ollama.chat(model=OLLAMA_MODEL, messages=messages)
    reply = response["message"]["content"]

    history.append({"role": "user", "content": user_message})
    history.append({"role": "assistant", "content": reply})
    session["history"] = history

    get_hindsight_client().retain(
        bank_id=BANK_ID,
        content=f"User: {user_message}\nAssistant: {reply}",
        retain_async=True,
    )

    return jsonify({"reply": reply})


@app.route("/reflect", methods=["POST"])
def reflect():
    result = get_hindsight_client().reflect(
        bank_id=BANK_ID,
        query="Summarize what you know about the user. Respond only in English.",
    )
    return jsonify({"summary": clean_markdown(result.text)})


if __name__ == "__main__":
    try:
        app.run(debug=os.getenv("DEBUG", "false").lower() == "true")
    finally:
        hindsight_server.stop()
