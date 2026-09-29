from telegram import Update
from telegram.ext import ContextTypes
from data import BIBLIOTECA_INFO
from services import responder_con_gemini


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    text_lower = text.lower()
    response = None

    if any(word in text_lower for word in ["hola", "buenas", "buenos dias", "hello"]):
        response = (
            "Hola. Soy el asistente virtual de BiblioFAUD.\n\n"
            "Puedo ayudarte con:\n"
            "- Horarios\n"
            "- Búsqueda de materiales\n"
            "- Préstamo de libros\n"
            "- Consulta de TFG y Tesis\n"
            "- Socios\n"
            "- Reglamento\n"
            "- Pérdida de material Bibliográfico"
        )

    elif any(word in text_lower for word in ["horario", "hora", "atencion", "abra", "cierra"]):
        h = BIBLIOTECA_INFO["horarios"]
        response = (
            "🕐 *Horarios de Atención*\n\n"
            f"Lunes a Viernes: {h['lunes_a_viernes']}\n"
            f"Sábados: {h['sabados']}\n"
            f"Domingos: {h['domingos']}"
        )

    elif any(word in text_lower for word in ["regla", "norma", "prohibido", "permitido", "silencio"]):
        reglas = BIBLIOTECA_INFO["reglamento"]
        response = "📋 *Reglamento de la Biblioteca*\n\n"
        for i, regla in enumerate(reglas, 1):
            response += f"{i}. {regla}\n"

    elif any(word in text_lower for word in ["perdida", "pérdida", "perdi", "perdí", "extravio", "extravío", "me robaron", "robo", "robado", "no devolvi", "no devolví", "material perdido", "libro perdido", "libro robado"]):
        pe = BIBLIOTECA_INFO["perdida_material"]
        response = (
            "📕 *Pérdida de material Bibliográfico*\n\n"
            f"{pe['descripcion']}"
        )

    elif any(word in text_lower for word in ["asociar", "asociarme", "asociarse", "hacerme socio", "quiero ser socio", "no soy socio", "quiero asociarme", "como me asocio"]):
        s = BIBLIOTECA_INFO["socios"]
        response = (
            "🪪 *Asociarse a la Biblioteca*\n\n"
            f"{s['descripcion']}"
        )

    elif any(word in text_lower for word in ["soy socio", "ya soy socio", "socio registrado", "soy socia", "ya soy socia"]):
        p = BIBLIOTECA_INFO["prestamo_libros"]
        response = (
            f"📚 *Préstamo de Libros*\n\n"
            f"• Máximo: {p['maximo']} libros\n"
            f"• Duración: {p['duracion']}\n"
            f"• Renovable: {p['renovable']}\n"
            f"• Requisitos: {p['requisitos']}\n\n"
            f"Aquí está el catálogo: {p['catalogo_url']}"
        )

    elif any(word in text_lower for word in ["prestamo de libros", "prestamo libro", "prestamos libro", "prestar libro", "llevar libro", "devolver libro", "vencimiento", "catalogo", "buscar libro"]):
        p = BIBLIOTECA_INFO["prestamo_libros"]
        response = (
            f"📚 *Préstamo de Libros*\n\n"
            f"• Máximo: {p['maximo']} libros\n"
            f"• Duración: {p['duracion']}\n"
            f"• Renovable: {p['renovable']}\n"
            f"• Requisitos: {p['requisitos']}\n\n"
            f"Aquí está el catálogo: {p['catalogo_url']}"
        )

    elif any(word in text_lower for word in ["tesis", "tfg", "tesis de grado", "posgrado", "documentos academicos", "repositorio"]):
        t = BIBLIOTECA_INFO["consulta_tfg_tesis"]
        response = (
            "📝 *Consulta de Tesis*\n\n"
            f"{t['descripcion']}:\n"
            f"{t['url']}"
        )

    elif any(word in text_lower for word in ["socio", "socios", "domicilio", "certificado", "regularidad"]):
        s = BIBLIOTECA_INFO["socios"]
        response = (
            "🪪 *Socios*\n\n"
            f"{s['descripcion']}"
        )

    elif any(word in text_lower for word in ["busqueda de materiales", "busqueda", "buscar", "material", "materiales", "catalogo", "libro disponible"]):
        response = (
            "🔍Aquí puede realizar la búsqueda en esta página:\n\n"
            "https://biblioteca.unsj.edu.ar/"
        )

    elif any(word in text_lower for word in ["categoria", "categorias", "temas"]):
        cat = BIBLIOTECA_INFO["categorias"]
        response = "📖 *Categorías Disponibles*\n\n"
        for c in cat:
            response += f"• {c}\n"

    elif any(word in text_lower for word in ["contacto", "telefono", "email", "donde"]):
        ho = BIBLIOTECA_INFO
        response = (
            "📞 *Datos de Contacto*\n\n"
            f"Nombre: {ho['nombre']}\n"
            f"Teléfono: {ho['telefono']}\n"
            f"Email: {ho['email']}"
        )

    if not response:
        response = responder_con_gemini(text)

    await update.message.reply_text(response, parse_mode='Markdown')