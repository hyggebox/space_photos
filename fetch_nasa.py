import requests

from datetime import datetime
from helpers import get_extension, download_img


def fetch_nasa_apod(api_key):
    nasa_apod_endpoint = "https://api.nasa.gov/planetary/apod"
    apod_params = {
        "api_key": api_key,
        "count": 30
    }

    response = requests.get(nasa_apod_endpoint, params=apod_params)
    response.raise_for_status()

    for number, record in enumerate(response.json()):
        if record["media_type"] == "image":
            img_url = record["url"]
            img_extension = get_extension(img_url)
            download_img(img_url, f"nasa_apod{number}{img_extension}")


def fetch_epic_img(api_key):
    epic_params = {
        "api_key": api_key
    }
    epic_endpoint = f"https://epic.gsfc.nasa.gov/api/natural"

    img_url_template = "https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/png/{img_name}.png"
    response = requests.get(epic_endpoint, params=epic_params)
    response.raise_for_status()

    for number, record in enumerate(response.json()):
        img_date = datetime.strptime(record["date"], "%Y-%m-%d %H:%M:%S")
        epic_img_url = img_url_template.format(
            year=img_date.year,
            month=img_date.month,
            day=img_date.day,
            img_name=record["image"]
        )
        download_img(epic_img_url, f"epic{number}.png")