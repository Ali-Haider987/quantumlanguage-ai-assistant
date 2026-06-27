"""
app.py — QuantumLanguage AI Assistant · Flask API
==================================================
Exposes the chatbot as a REST API.

Endpoints:
  POST /chat          — send a message, get a response
  GET  /health        — liveness check
  POST /reset         — clear conversation history
  GET  /history       — return the current conversation history

Run:
  python app.py
"""

from flask import Flask, request, jsonify, Response
from chatbot import get_response, reset_conversation, conversation_history

app = Flask(__name__)


# ── Helpers ──────────────────────────────────────────────────────────────────

def _error(message: str, status: int) -> tuple[Response, int]:
    """Return a consistent JSON error response."""
    return jsonify({"ok": False, "error": message}), status


# ─────────────────────────────────────────────────────────────────────────────
# ENDPOINTS
# ─────────────────────────────────────────────────────────────────────────────

@app.post("/chat")
def chat() -> tuple[Response, int]:
    """
    Send a message to the chatbot.
    """
    body = request.get_json(silent=True)

    if not body:
        return _error('Request must be JSON with "message".', 400)

    message = body.get("message", "").strip()
    if not message:
        return _error('"message" field is required.', 400)

    try:
        reply = get_response(message)
    except Exception as exc:
        return _error(f"Chatbot error: {exc}", 500)

    # Detect type
    query_type = "unknown"
    for line in reply.splitlines():
        if "CONCEPT" in line:
            query_type = "concept"
            break
        elif "CODING" in line:
            query_type = "coding"
            break
        elif "DEBUGGING" in line:
            query_type = "debugging"
            break

    return jsonify({
        "ok": True,
        "response": reply,
        "type": query_type
    }), 200


@app.get("/health")
def health() -> tuple[Response, int]:
    return jsonify({
        "ok": True,
        "status": "healthy",
        "service": "QuantumLanguage-AI-Assistant"
    }), 200


@app.post("/reset")
def reset() -> tuple[Response, int]:
    reset_conversation()
    return jsonify({
        "ok": True,
        "message": "Conversation history cleared."
    }), 200


@app.get("/history")
def history() -> tuple[Response, int]:
    return jsonify({
        "ok": True,
        "turns": len(conversation_history) // 2,
        "history": conversation_history
    }), 200


# ─────────────────────────────────────────────────────────────────────────────
# ERROR HANDLERS
# ─────────────────────────────────────────────────────────────────────────────

@app.errorhandler(404)
def not_found(_):
    return _error(
        "Endpoint not found. Use /chat, /health, /reset, /history",
        404
    )


@app.errorhandler(405)
def method_not_allowed(_):
    return _error("Method not allowed for this endpoint.", 405)


# ─────────────────────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True, port=5000)