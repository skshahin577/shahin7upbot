import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = "7336864073:AAF4ETnQZ0TKV61tLP0IHskBPdif-_oMMb4"
CHAT_ID = "6795221305"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route("/", methods=["GET", "POST"])
def index():
    return "7Up Bot is running!"

@app.route("/message", methods=["POST"])
def message():
    data = request.get_json()
    if data and "message" in data:
        text = data["message"].get("text", "")
        if text == "/start":
            send_message("✅ 7Up Prediction Bot is active.\nI’ll send you next round predictions here.")
    return {"ok": True}

def send_message(text):
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(API_URL, json=payload)

if __name__ == "__main__":
    app.run()
