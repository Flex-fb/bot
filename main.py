import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет, сладкий, хочешь расслабиться и получать незабываемые удовольствия?")

if __name__ == '__main__':
    app = ApplicationBuilder().token(os.environ['BOT_TOKEN']).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
