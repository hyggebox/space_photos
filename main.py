import os
import pathlib
import telegram

from dotenv import load_dotenv
from time import sleep

from fetch_nasa import fetch_epic_img, fetch_nasa_apod
from fetch_spacex import fetch_spacex_launch


if __name__ == "__main__":
    load_dotenv()

    nasa_api_key = os.environ['NASA_API_KEY']
    chat_id = os.environ['CHAT_ID']

    pathlib.Path('images/').mkdir(exist_ok=True)

    bot = telegram.Bot(token=os.environ["TG_BOT_TOKEN"])

    while True:
        fetch_spacex_launch()
        fetch_nasa_apod(nasa_api_key)
        fetch_epic_img(nasa_api_key)
        imgs_to_send = os.listdir("images")

        for img in imgs_to_send:
            with open(f"images/{img}", "rb") as image:
                bot.send_photo(chat_id=chat_id, photo=image)
            sleep(int(os.getenv("DELAY", default=86400)))

