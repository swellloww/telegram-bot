from pyrogram import Client
from pyrogram.types import ChatJoinRequest
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

app = Client("join_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_chat_join_request()
def auto_message(client, request: ChatJoinRequest):
    message =     message = """
👋 Hey there, Trader!

😓 Struggling with losses on Quotex?
💸 Losing money every day?
🚀 Can’t find the right group to guide you?

💥 Don’t worry! You’re just 1 step away from winning!  
Join my **BUG VIP Group** — 100% FREE! 🆓💎  
🎯 No fees, no charges — just real signals & expert guidance.

🔥 Click the links below and start your winning journey today! 🏆

📍 Join VIP Now ⬇️  
🔗 https://t.me/+LCqPFEoYMqJjZDQ1

📍 For Compounding Setup ⬇️  
🔗 https://t.me/+LCqPFEoYMqJjZDQ1

📍 Real-Time Signals ⬇️  
🔗 https://t.me/+LCqPFEoYMqJjZDQ1

📍 Daily Profit Access ⬇️  
🔗 https://t.me/+LCqPFEoYMqJjZDQ1
"""

    client.send_message(chat_id=request.from_user.id, text=message)

app.run()
