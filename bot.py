from pyrogram import Client
from pyrogram.types import ChatJoinRequest
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

app = Client("join_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_chat_join_request()
def auto_message(client, request: ChatJoinRequest):
    message = """
Hey there, Trader! 👋  
Struggling with losses on Quotex? 😔💸  
Losing money every day and can’t find the right group to guide you? 🚀✨

Don’t worry! Join my BUG VIP group absolutely FREE! 🆓💎  
No hidden charges, no fees — just FREE trades and expert guidance. 🎯📈  
Click the link below and start winning today! 🏆🔥  

For Compounding ⬇️⬇️⬇️⬇️  
https://t.me/+LCqPFEoYMqJjZDQ1
"""
    client.send_message(chat_id=request.from_user.id, text=message)

app.run()
