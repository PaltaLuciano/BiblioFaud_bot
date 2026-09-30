import os
from dotenv import load_dotenv

load_dotenv()

from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TELEGRAM_TOKEN, GEMINI_API_KEY, GEMINI_MODEL
from handlers import (
    start_command,
    help_command,
    horarios_command,
    reglamento_command,
    prestamos_libros_command,
    busqueda_command,
    categorias_command,
    contacto_command,
    tfg_tesis_command,
    socios_command,
    perdida_material_command,
    handle_message,
)


def _check_config():
    faltantes = [
        nombre
        for nombre, valor in (
            ("TELEGRAM_TOKEN", TELEGRAM_TOKEN),
            ("GEMINI_API_KEY", GEMINI_API_KEY),
        )
        if not valor
    ]
    if faltantes:
        raise ValueError(
            f"❌ Faltan variables de entorno: {', '.join(faltantes)}. "
            "Configuralas en Railway (Variables) y reiniciá el servicio."
        )
    print("🔑 TOKEN cargado correctamente")
    print(f"🤖 Modelo de Gemini: {GEMINI_MODEL}")


def main():
    _check_config()

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("horarios", horarios_command))
    app.add_handler(CommandHandler("reglamento", reglamento_command))
    app.add_handler(CommandHandler("prestamos_libros", prestamos_libros_command))
    app.add_handler(CommandHandler("busqueda", busqueda_command))
    app.add_handler(CommandHandler("categorias", categorias_command))
    app.add_handler(CommandHandler("tfg_tesis", tfg_tesis_command))
    app.add_handler(CommandHandler("socios", socios_command))
    app.add_handler(CommandHandler("contacto", contacto_command))
    app.add_handler(CommandHandler("perdida_material", perdida_material_command))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("📚 Bot de BiblioFAUD iniciado correctamente...")

    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(str(e))
    except RuntimeError as e:
        print(f"⚠️  No se pudo iniciar el bot: {e}")
        print("Si el error menciona 'Conflict' o 'terminated by other getUpdates', "
              "hay otra instancia del bot corriendo con el mismo token. "
              "Detenela localmente o revocá el token en @BotFather.")
    except KeyboardInterrupt:
        print("\n👋 Bot detenido.")
