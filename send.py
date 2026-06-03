import requests
import os
import json

BOT_TOKEN = os.environ["BOT_TOKEN"]
GROUPS = json.loads(os.environ["GROUPS_JSON"])

MESSAGE = """High-Quality Guestpost Available 🔥

Metrik kuat, harga tetap ramah di kantong 💸
Konten full English, siap publish profesional 🌍

Cukup Rp 250.000 per post aja

Cocok banget buat boost authority & ranking website kamu 🚀

Langsung order atau tanya detail ke @karyaonedigital"""
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

for group_name, chat_id in GROUPS.items():
    response = requests.post(
        url,
        data={"chat_id": chat_id, "text": MESSAGE}
    )
    print(group_name, response.status_code)
