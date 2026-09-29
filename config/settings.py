import os

# Variables principales
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

# Validaciones (evita errores silenciosos)
if not TELEGRAM_TOKEN:
    raise ValueError("Falta TELEGRAM_TOKEN en las variables de entorno")

if not GEMINI_API_KEY:
    raise ValueError("Falta GEMINI_API_KEY en las variables de entorno")

# Modelos de respaldo
GEMINI_FALLBACK_MODELS = [
    "gemini-3-flash-preview",
    "gemini-3.1-flash-lite-preview",
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-2.0-flash",
]