from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import requests

TOKEN = "8697118542:AAHEFAhe-jAuGS-S9fWezvJmxxIn0ru8K1E"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📸 Send me a photo. I will give Telegraph link.")

async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await context.bot.get_file(photo.file_id)
    url = file.file_path

    img = requests.get(url).content
    response = requests.post("https://telegra.ph/upload", files={"file": img})

    link = "https://telegra.ph" + response.json()[0]["src"]

    await update.message.reply_text(f"🔗 Telegraph Link:\n{link}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.PHOTO, photo))

app.run_polling()
