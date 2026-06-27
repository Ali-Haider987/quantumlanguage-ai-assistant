import re
from enum import Enum

# ─────────────────────────────────────────────────────────────
# QUERY TYPE
# ─────────────────────────────────────────────────────────────

class QueryType(Enum):
    CONCEPT = "concept"
    CODING = "coding"
    DEBUGGING = "debugging"

    @property
    def label(self) -> str:
        icons = {
            QueryType.CONCEPT: "📌 CONCEPT",
            QueryType.CODING: "🛠 CODING",
            QueryType.DEBUGGING: "🐛 DEBUGGING",
        }
        return icons[self]

    @property
    def colour_code(self) -> str:
        codes = {
            QueryType.CONCEPT: "\033[96m",
            QueryType.CODING: "\033[92m",
            QueryType.DEBUGGING: "\033[93m",
        }
        return codes[self]


# ─────────────────────────────────────────────────────────────
# CLASSIFICATION
# ─────────────────────────────────────────────────────────────

_DEBUGGING_SIGNALS = (
    "error", "exception", "traceback", "attributeerror",
    "typeerror", "importerror", "indexerror", "valueerror",
    "bug", "broken", "crash", "not working", "fix", "debug"
)

_CODING_SIGNALS = (
    "code", "write", "show me", "implement", "create",
    "program", "example", "qiskit", "simulate"
)


def classify_query(text: str) -> QueryType:
    lowered = text.lower()

    if any(sig in lowered for sig in _DEBUGGING_SIGNALS):
        return QueryType.DEBUGGING

    if any(sig in lowered for sig in _CODING_SIGNALS):
        return QueryType.CODING

    return QueryType.CONCEPT


# ─────────────────────────────────────────────────────────────
# RESPONSE FORMATTER
# ─────────────────────────────────────────────────────────────

def divider(char="─", width=60) -> str:
    return char * width


def format_response(content: str, query_type: QueryType) -> str:
    label = query_type.label

    return (
        f"\n{divider('═')}\n"
        f"[ {label} ]\n"
        f"{divider('─')}\n"
        f"{content}\n"
        f"{divider('═')}\n"
    )


# ─────────────────────────────────────────────────────────────
# DEBUGGING HELPERS
# ─────────────────────────────────────────────────────────────

def extract_error(text: str) -> str | None:
    patterns = {
        "AttributeError": r"attributeerror",
        "TypeError": r"typeerror",
        "ImportError": r"importerror|modulenotfounderror",
        "IndexError": r"indexerror",
        "ValueError": r"valueerror",
    }

    for name, pattern in patterns.items():
        if re.search(pattern, text, re.IGNORECASE):
            return name

    return None


def suggest_fix(error_name: str) -> str | None:
    fixes = {
        "AttributeError": "Check if function name is correct or object type is valid.",
        "TypeError": "Ensure correct data types for variables and function arguments.",
        "ImportError": "Install missing libraries using pip install.",
        "IndexError": "Check list or array indexing (out of range).",
        "ValueError": "Check if input values are within valid range.",
    }

    return fixes.get(error_name)


def build_debug_prefix(user_text: str) -> str:
    error = extract_error(user_text)
    if not error:
        return ""

    fix = suggest_fix(error)
    if not fix:
        return ""

    return (
        f"⚡ QUICK FIX for {error}\n"
        f"{divider('-')}\n"
        f"{fix}\n"
        f"{divider('-')}\n\n"
    )