import os
import pathlib
import random
import requests
import telegram

from datetime import datetime
from dotenv import load_dotenv
from urllib.parse import urlsplit, unquote


def get_extension(url):
    split_url = urlsplit(unquote(url))
    split_path = os.path.split(split_url.path)
    file_extension = os.path.splitext(split_path[-1])
    return file_extension[-1]


def download_img(img_url, img_name):
    response = requests.get(img_url)
    response.raise_for_status()

    with open(f"images/{img_name}", "wb") as file:
        file.write(response.content)


def fetch_spacex_launch():
    spacex_endpoint = "https://api.spacexdata.com/v4/launches/"

    response = requests.get(spacex_endpoint)
    response.raise_for_status()
    flights = response.json()

    for flight in flights:
        img_links = flight["links"]["flickr"]["original"]
        if img_links:
            for img_num, link in enumerate(img_links):
                img_extension = get_extension(link)
                download_img(link, f"spacex{str(img_num)}{img_extension}")
                break


def fetch_nasa_apod():
    nasa_apod_endpoint = "https://api.nasa.gov/planetary/apod"
    apod_params = {
        "api_key": NASA_API_KEY,
        "count": 30
    }

    response = requests.get(nasa_apod_endpoint, params=apod_params)
    response.raise_for_status()
    fetched_imgs = response.json()

    for img_num, img in enumerate(fetched_imgs):
        img_url = img["url"]
        img_extension = get_extension(img_url)
        download_img(img_url, f"nasa_apod{str(img_num)}{img_extension}")


def fetch_epic_img():
    epic_endpoint = f"https://epic.gsfc.nasa.gov/api/natural?api_key={NASA_API_KEY}"
    img_url_template = "https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/png/{img_name}.png"
    response = requests.get(epic_endpoint)
    response.raise_for_status()

    for img_num, img in enumerate(response.json()):
        img_date = datetime.strptime(img["date"], "%Y-%m-%d %H:%M:%S")
        epic_img_url = img_url_template.format(
            year=img_date.year,
            month=img_date.month,
            day=img_date.day,
            img_name=img["image"]
        )
        download_img(epic_img_url, f"epic{str(img_num)}.png")


if __name__ == "__main__":
    load_dotenv()

    NASA_API_KEY = os.environ['NASA_API_KEY']
    CHAT_ID = "@GreatSpacePics"
    tg_msg = "Hello everybody!"
    tg_img_to_send = random.choice(os.listdir("images"))

    # Create /images directory
    pathlib.Path('images/').mkdir(exist_ok=True)

    # fetch_spacex_launch()
    # fetch_nasa_apod()
    # fetch_epic_img()

    # Telegram bot
    bot = telegram.Bot(token=os.environ["TG_BOT_TOKEN"])
    # bot.send_message(text=tg_msg, chat_id=CHAT_ID)
    bot.send_photo(chat_id=CHAT_ID, photo=open(f"images/{tg_img_to_send}", "rb"))

