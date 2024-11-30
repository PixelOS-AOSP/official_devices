import requests
import os
import json

bot_api = os.environ["bot_api"]
chat_id = os.environ["chat_id"]


def send_message(message, token=bot_api, chat_id=chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True,
    }
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(
            f"Failed to send message. Status code: {response.status_code}, Response: {response.text}"
        )

    return response


codename = os.environ["codename"]
version_number = os.environ["version_number"]
version_string = os.environ["version_string"]
download_link = f"https://pixelos.net/download/{codename}"

with open(f"API/devices/{codename}.json", "r") as f:
    data = json.load(f)
    model = data["model"]

    maintainers = data["maintainer"]
    maintainers_data = " && ".join(
        f"[{m['display_name']}](https://t.me/{m['telegram']})" for m in maintainers
    )

    upload_date = data["last_updated"]

with open(f"API/updater/{codename}.json", "r") as f:
    data = json.load(f)
    raw_size = data["response"][0]["size"]
    size = raw_size / (1000**3)


post_format = (
    f"*New build available for {model} ({codename})*\n"
    f"*by* {maintainers_data}\n\n"
    f"*Version:* {version_string}\n"
    f"*File size:* {size:.2f}G\n"
    f"*Updated on:* {upload_date}\n"
    f"[Download now]({download_link})\n\n"
    f"#{codename} #{version_string} #TeamPixel #PixelOS"
)

send_message(message=post_format)
