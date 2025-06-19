
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = 'YOUR_BOT_TOKEN'  # Замените на ваш токен

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет, сладкий, хочешь расслабиться и получать незабываемые удовольствия?")

if __name__ == '__main__':
    app = ApplicationBuilder().token("7750610421:AAFusUJ3dcxSSEDYoUvl0jAnsSeEsZDM1zA").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
