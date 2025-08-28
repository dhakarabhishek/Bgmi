import os
import threading
from flask import Flask
from pyrogram import Client, filters

# =======================
# Flask keep-alive server
# =======================
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "✅ Bot is running on Render!"

def run_flask():
    flask_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

# =======================
# Pyrogram Bot Client
# =======================
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    ipv6=False,              # force IPv4 only
    sleep_threshold=30,      # increase ping timeout
    connection_retries=10    # retry connections
)

# =======================
# Handlers
# =======================
@bot.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("👋 Hello! Your bot is live on Render 🚀")

# =======================
# Start both Flask + Bot
# =======================
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    bot.run()

