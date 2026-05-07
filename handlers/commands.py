from telegram import Update
from telegram.ext import ContextTypes
from data import BIBLIOTECA_INFO


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hola. Soy el asistente virtual de BiblioFAUD.\n\n"
        "Puedo ayudarte con:\n"
        "- Horarios\n"
        "- Reglas\n"
        "- Préstamo de libros\n"
        "- Consulta de tesis\n"
        "- Socios\n"
        "- Búsqueda de materiales"
    )

async def tesis_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    t = BIBLIOTECA_INFO["consulta_tesis"]
    await update.message.reply_text(
        "📝 *Consulta de Tesis*\n\n"
        f"{t['descripcion']}:\n"
        f"{t['url']}",
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Comandos disponibles:\n\n"
        "/start - Iniciar conversación\n"
        "/horarios - Ver horarios de atención\n"
        "/reglas - Normas de la biblioteca\n"
        "/prestamos_libros - Información sobre préstamos de libros\n"
        "/busqueda - Cómo buscar materiales\n"
        "/categorias - Categorías de libros disponibles\n"
        "/tesis - Consulta de tesis digitales\n"
        "/contacto - Datos de contacto\n"
        "/socios - Cómo hacerse socio de la biblioteca\n"
        "/help - Ver este mensaje de ayuda"
    )


async def horarios_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    h = BIBLIOTECA_INFO["horarios"]
    await update.message.reply_text(
        "🕐 *Horarios de Atención*\n\n"
        f"Lunes a Viernes: {h['lunes_a_viernes']}\n"
        f"Sábados: {h['sabados']}\n"
        f"Domingos: {h['domingos']}",
        parse_mode='Markdown'
    )


async def reglas_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reglas = BIBLIOTECA_INFO["reglas"]
    texto = "📋 *Normas de la Biblioteca*\n\n"
    for i, regla in enumerate(reglas, 1):
        texto += f"{i}. {regla}\n"
    await update.message.reply_text(texto, parse_mode='Markdown')


async def prestamos_libros_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    p = BIBLIOTECA_INFO["prestamo_libros"]
    await update.message.reply_text(
        f"📚 *Préstamo de Libros*\n\n"
        f"• Máximo: {p['maximo']} libros\n"
        f"• Duración: {p['duracion']}\n"
        f"• Renovable: {p['renovable']}\n"
        f"• Requisitos: {p['requisitos']}\n\n"
        f"Aquí esta el catálogo para que busques bien: {p['catalogo_url']}",
        parse_mode='Markdown'
    )





async def busqueda_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Aquí puede realizar la búsqueda en esta página, donde se encuentra disponible el catálogo: https://biblioteca.unsj.edu.ar/")


async def categorias_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cat = BIBLIOTECA_INFO["categorias"]
    texto = "📖 *Categorías Disponibles*\n\n"
    for c in cat:
        texto += f"• {c}\n"
    await update.message.reply_text(texto, parse_mode='Markdown')

async def socios_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    s = BIBLIOTECA_INFO["socios"]
    await update.message.reply_text(
        "🪪 *Socios*\n\n"
        f"{s['descripcion']}",
        parse_mode='Markdown'
    )

async def contacto_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ho = BIBLIOTECA_INFO
    await update.message.reply_text(
        "📞 *Datos de Contacto*\n\n"
        f"Nombre: {ho['nombre']}\n"
        f"Teléfono: {ho['telefono']}\n"
        f"Email: {ho['email']}",
        parse_mode='Markdown'
    )
