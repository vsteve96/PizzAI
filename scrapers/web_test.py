import requests
from bs4 import BeautifulSoup


def scrape_title(url):
    """
    Egy weboldal címének lekérése.
    """

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    title = soup.find("title")

    if title:
        return title.text.strip()

    return "Nincs cím"