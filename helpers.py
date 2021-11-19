import os
import requests

from urllib.parse import urlsplit, unquote


def get_extension(url):
    split_url = urlsplit(unquote(url))
    file_extension = os.path.splitext(split_url.path)[1]
    return file_extension[-1]


def download_img(img_url, img_name):
    response = requests.get(img_url)
    response.raise_for_status()

    with open(f"images/{img_name}", "wb") as file:
        file.write(response.content)