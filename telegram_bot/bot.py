import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests
import json

load_dotenv()

API_URL = "http://localhost:8000/aggregate"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Send me a JSON with dt_from, dt_upto, and group_type.")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if update.message.text is None:
            await update.message.reply_text("Error: Message text is None")
            return

        data = json.loads(update.message.text)
        response = requests.post(API_URL, json=data)
        result = response.json()

        result_str = json.dumps(result, indent=4)
        # Split response into chunks if too long
        MAX_MESSAGE_LENGTH = 4096
        for i in range(0, len(result_str), MAX_MESSAGE_LENGTH):
            await update.message.reply_text(result_str[i:i + MAX_MESSAGE_LENGTH])
    except json.JSONDecodeError:
        await update.message.reply_text("Error: Invalid JSON")
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")


def main():
    TOKEN = os.getenv('TELEGRAM_TOKEN')
    if not TOKEN:
        raise ValueError("No TELEGRAM_TOKEN found in environment variables")

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()


if __name__ == "__main__":
    main()

