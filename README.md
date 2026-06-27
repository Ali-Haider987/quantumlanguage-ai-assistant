# ⚛ QuantumLanguage AI Assistant

A tutor-style AI chatbot for quantum computing concepts and Qiskit programming, served as a Flask REST API and interactive CLI.

---

##  Features
- Smart query classification (concept, coding, debugging)
- Built-in quantum knowledge (concepts + Qiskit examples)
- Debugging assistance for common errors
- Context-aware AI responses
- Multi-turn conversation memory
- Session management (/reset, /save, /load)
- REST API support (JSON input/output)
- Interactive CLI mode

---

##  Project Structure

QuantumLanguage-AI-Assistant/
│
├── app.py            # Flask REST API
├── chatbot.py        # Core chatbot logic
├── utils.py          # Helper utilities
├── requirements.txt  # Dependencies
└── README.md         # Documentation

---

##  Setup & Run

Run these commands in terminal:

git clone https://github.com/your-username/quantumlanguage-ai-assistant.git  
cd quantumlanguage-ai-assistant  
pip install -r requirements.txt  
python app.py  

Then open in your browser:
http://127.0.0.1:5000

---

##  CLI Mode (Optional)

Run:
python chatbot.py

Commands:
- /reset → clear history  
- /save → save session  
- /load → load session  
- /quit → exit  

---

##  API Usage

POST /chat

Request:

{
  "message": "What is superposition?"
}

Response:

{
  "ok": true,
  "type": "concept",
  "response": "Superposition allows qubits to exist in multiple states simultaneously..."
}

---

## 📌 Query Types

- Concept → theory explanations  
- Coding → Qiskit code help  
- Debugging → fixing errors  

---

## Error Response

{
  "ok": false,
  "error": "\"message\" field is required."
}

---

##  Requirements

- Python 3.9+
- Flask
- Anthropic SDK

---

##  Future Improvements

- AI-enhanced responses  
- Better NLP understanding  
- Web interface  
- Quantum visualization  

---
