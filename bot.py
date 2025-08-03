from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from pytube import YouTube
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎵 Welcome to WaifuTunes Bot!")

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = context.args[0]
    yt = YouTube(url)
    stream = yt.streams.get_audio_only()
    stream.download(filename="song.mp3")
    await update.message.reply_audio(audio=open("song.mp3", "rb"))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("play", play))

app.run_polling()
