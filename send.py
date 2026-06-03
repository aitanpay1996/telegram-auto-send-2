import requests
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_IDS = os.environ["CHAT_IDS"].split(",")

MESSAGE = """High-Quality Guestpost Available 🔥

Metrik kuat, harga tetap ramah di kantong 💸
Konten full English, siap publish profesional 🌍

Cukup Rp 250.000 per post aja

Cocok banget buat boost authority & ranking website kamu 🚀

Langsung order atau tanya detail ke @karyaonedigital"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

for chat_id in CHAT_IDS:
    requests.post(
        url,
        data={
            "chat_id": chat_id.strip(),
            "text": MESSAGE
        }
    )
