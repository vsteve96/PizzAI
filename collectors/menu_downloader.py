import json
from pathlib import Path
from datetime import datetime

import requests


RESTAURANTS_FILE = Path("data/restaurants.json")
RAW_FOLDER = Path("data/raw")


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64)"
    )
}


def load_restaurants():
    with open(
        RESTAURANTS_FILE,
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)


def download_page(url):
    response = requests.get(
        url,
        headers=HEADERS,
        timeout=15
    )

    response.raise_for_status()

    return response.text


def save_html(name, html):

    RAW_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    filename = (
        name
        .lower()
        .replace(" ", "_")
        .replace("/", "_")
        + ".html"
    )

    path = RAW_FOLDER / filename

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(html)

    return path


def run():

    restaurants = load_restaurants()

    for restaurant in restaurants:

        url = restaurant.get("url")

        if not url:
            continue

        print(
            f"Letöltés: {restaurant['name']}"
        )

        try:
            html = download_page(url)

            path = save_html(
                restaurant["name"],
                html
            )

            print(
                f"Mentve: {path}"
            )

        except Exception as error:

            print(
                f"Hiba: {error}"
            )


if __name__ == "__main__":
    run()