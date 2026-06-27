# chatbot.py

conversation_history = []

def get_response(user_input):
    user_input = user_input.lower()

    conversation_history.append({"role": "user", "content": user_input})

    if "qubit" in user_input:
        response = "📌 CONCEPT: A qubit is the basic unit of quantum information."

    elif "superposition" in user_input:
        response = "📌 CONCEPT: Superposition allows a qubit to exist in multiple states at once."

    elif "entanglement" in user_input:
        response = "📌 CONCEPT: Entanglement links qubits so that one affects the other instantly."

    elif "code" in user_input or "qiskit" in user_input:
        response = """🛠 CODING:
from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.draw()
"""

    elif "error" in user_input or "debug" in user_input:
        response = "🐛 DEBUGGING: Check your imports and Qiskit installation."

    else:
        response = "I can help with quantum concepts, coding, and debugging."

    conversation_history.append({"role": "assistant", "content": response})

    return response


def reset_conversation():
    conversation_history.clear()