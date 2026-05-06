import os
from dotenv import load_dotenv

# Cargar variables de entorno SIEMPRE al inicio
load_dotenv()

from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TELEGRAM_TOKEN
from handlers import (
    start_command,
    help_command,
    horarios_command,
    reglas_command,
    prestamos_libros_command,
    busqueda_command,
    categorias_command,
    contacto_command,
    tesis_command,
    socios_command,
    handle_message,
)


def main():
    # Validación del token (evita errores silenciosos)
    if not TELEGRAM_TOKEN:
        raise ValueError("❌ TELEGRAM_TOKEN no está configurado. Revisá tu .env o variables de entorno.")

    print("🔑 TOKEN cargado correctamente")

    # Crear aplicación
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Comandos
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("horarios", horarios_command))
    app.add_handler(CommandHandler("reglas", reglas_command))
    app.add_handler(CommandHandler("prestamos_libros", prestamos_libros_command))
    app.add_handler(CommandHandler("busqueda", busqueda_command))
    app.add_handler(CommandHandler("categorias", categorias_command))
    app.add_handler(CommandHandler("tesis", tesis_command))
    app.add_handler(CommandHandler("socios", socios_command))
    app.add_handler(CommandHandler("contacto", contacto_command))
    
    # Mensajes de texto
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("📚 Bot de BiblioFAUD iniciado correctamente...")
    
    # Ejecutar bot
    app.run_polling()


if __name__ == "__main__":
    main()