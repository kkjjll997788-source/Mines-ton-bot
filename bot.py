import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from flask import Flask
from threading import Thread

# Flask সার্ভার (Render-এর জন্য পোর্ট খোলা রাখতে)
app_flask = Flask(__name__)

@app_flask.route('/')
def health_check():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app_flask.run(host='0.0.0.0', port=port)

# Telegram বট
API_TOKEN = os.environ.get("TELEGRAM_TOKEN")  # টোকেন এনভায়রনমেন্ট ভেরিয়েবল থেকে নিবে
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.reply("🚀 Mines Ton Signal বটে স্বাগতম!\n\n/signal — নতুন সিগন্যাল পেতে এখানে ক্লিক করুন।")

@dp.message(Command("signal"))
async def send_signal(message: types.Message):
    signal = "🎯 মাইনস টন সিগন্যাল: লাল বাটনে ক্লিক করো!"
    await message.reply(signal)

async def run_bot():
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Flask থ্রেডে চালান
    flask_thread = Thread(target=run_flask)
    flask_thread.start()
    # বট চালান
    asyncio.run(run_bot())
