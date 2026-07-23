import json
from pathlib import Path


FILE = Path("data/restaurants.json")


def load():
    if FILE.exists():
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    return []


def save(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )


def add_candidate(title, url):

    restaurants = load()

    name = title.split("-")[0].strip()

    exists = any(
        r["name"].lower() == name.lower()
        for r in restaurants
    )

    if exists:
        print("Már létezik:", name)
        return


    restaurants.append(
        {
            "name": name,
            "city": "Szeged",
            "url": url,
            "sources": [
                "web_search"
            ],
            "status": "candidate"
        }
    )

    save(restaurants)

    print("Hozzáadva:", name)


if __name__ == "__main__":

    add_candidate(
        "PizzaToronySzeged - Kezdőlap",
        "https://pizzatoronyszeged.hu/"
    )

    add_candidate(
        "Görög Pizzéria Szeged",
        "https://gorogpizzeria.hu/"
    )