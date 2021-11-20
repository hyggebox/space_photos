import requests
from helpers import get_extension, download_img


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
                download_img(link, f"spacex{img_num}{img_extension}")
            break