from google import genai
from config import GEMINI_API_KEY, GEMINI_MODEL, GEMINI_FALLBACK_MODELS
from data import BIBLIOTECA_INFO

client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None

SYSTEM_INSTRUCTION = (
    "Sos el asistente virtual de la biblioteca universitaria BiblioFAUD. "
    "Tu ÚNICA función es responder preguntas relacionadas con la biblioteca, sus servicios, "
    "horarios, préstamos, reglas, personal, categorías de libros y materiales.\n\n"
    f"Información de la biblioteca:\n{BIBLIOTECA_INFO}\n\n"
    "REGLAS ESTRICTAS:\n"
    "1. Si la consulta NO tiene relación con la biblioteca o sus servicios, responde ÚNICAMENTE con la frase exacta: 'Eso no está relacionado con la biblioteca, no puedo responder.'\n"
    "2. Si el usuario te insulta o usa groserías, responde: 'Mantengamos el respeto. Solo puedo ayudarte con consultas sobre la biblioteca.'\n"
    "3. NO actúes como un asistente general. NO generes texto, código ni opiniones fuera del tema de la biblioteca."
)

MENSAJE_NO_DISPONIBLE = "En este momento, el chatbot no se encuentra disponible para consultas personalizadas. Por favor, intente nuevamente en unos minutos. Mientras tanto, al escribir “Hola” en el chat podrá acceder a la sección “Puede ayudarte con:”, donde encontrará consultas frecuentes con respuestas ya disponibles; solo debe escribir la opción que desee, por ejemplo: “Reglas”."


def _is_quota_error(error_msg: str) -> bool:
    return (
        "429" in error_msg
        or "RESOURCE_EXHAUSTED" in error_msg
        or "quota" in error_msg.lower()
    )


def _try_model(model: str, mensaje: str) -> str:
    response = client.models.generate_content(
        model=model,
        contents=mensaje,
        config={"system_instruction": SYSTEM_INSTRUCTION},
    )
    if response.text:
        return response.text
    raise ValueError("Empty response")


def responder_con_gemini(mensaje: str) -> str:
    if client is None:
        return MENSAJE_NO_DISPONIBLE

    models_to_try = list(GEMINI_FALLBACK_MODELS)
    if GEMINI_MODEL not in models_to_try:
        models_to_try.insert(0, GEMINI_MODEL)

    for model in models_to_try:
        try:
            return _try_model(model, mensaje)
        except Exception as e:
            error_msg = str(e)
            if not _is_quota_error(error_msg):
                return MENSAJE_NO_DISPONIBLE
            # Si es error de cuota, continúa al siguiente modelo

    return MENSAJE_NO_DISPONIBLE