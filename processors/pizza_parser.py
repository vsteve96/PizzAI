from pathlib import Path
from bs4 import BeautifulSoup
import re


RAW_FOLDER = Path("data/raw")


def html_to_text(path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:
        html = file.read()

    soup = BeautifulSoup(
        html,
        "lxml"
    )

    return soup.get_text(
        " ",
        strip=True
    )


def find_prices(text):

    patterns = [
        r"\b\d{3,5}\s?Ft\b",
        r"\b\d{3,5}\s?ft\b",
        r"\b\d{1,2}[ .]?\d{3}\s?Ft\b",
        r"\b\d{3,5},-\b"
    ]

    prices = []

    for pattern in patterns:
        matches = re.findall(
            pattern,
            text
        )

        prices.extend(matches)

    return prices


def find_pizza_mentions(text):

    keywords = [
        "pizza",
        "margherita",
        "sonkás",
        "hawaii",
        "capricciosa",
        "prosciutto",
        "salami",
        "szalámi"
    ]

    found = []

    lower = text.lower()

    for word in keywords:
        if word in lower:
            found.append(word)

    return found


def analyze_file(path):

    text = html_to_text(path)

    prices = find_prices(text)

    print("=" * 40)
    print(path.name)
    print("Karakterek:", len(text))
    print("Talált árak:", prices)
    print("Pizza kulcsszavak:", find_pizza_mentions(text))


if __name__ == "__main__":

    for file in RAW_FOLDER.glob("*.html"):
        analyze_file(file)