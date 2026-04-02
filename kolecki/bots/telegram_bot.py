import os
import requests


def send_telegram(text: str) -> bool:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token:
        print("TELEGRAM_BOT_TOKEN не найден")
        return False

    if not chat_id:
        print("TELEGRAM_CHAT_ID не найден")
        return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    try:
        response = requests.post(
            url,
            data={
                "chat_id": chat_id,
                "text": text,
                "parse_mode": "HTML",
            },
            timeout=10,
        )

        if response.status_code == 200:
            return True

        print("Ошибка Telegram API:", response.status_code, response.text)
        return False

    except requests.RequestException as e:
        print("Ошибка отправки в Telegram:", e)
        return False