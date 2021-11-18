import os
import pathlib
import telegram

from dotenv import load_dotenv
from time import sleep

from fetch_nasa import fetch_epic_img, fetch_nasa_apod
from fetch_spacex import fetch_spacex_launch


if __name__ == "__main__":
    load_dotenv()

    NASA_API_KEY = os.environ['NASA_API_KEY']
    CHAT_ID = os.environ['CHAT_ID']

    # Create /images directory
    pathlib.Path('images/').mkdir(exist_ok=True)

    bot = telegram.Bot(token=os.environ["TG_BOT_TOKEN"])

    while True:
        fetch_spacex_launch()
        fetch_nasa_apod(NASA_API_KEY)
        fetch_epic_img(NASA_API_KEY)
        imgs_to_send = os.listdir("images")

        for img in imgs_to_send:
            bot.send_photo(chat_id=CHAT_ID, photo=open(f"images/{img}", "rb"))
            sleep(int(os.getenv("DELAY", default=86400)))

