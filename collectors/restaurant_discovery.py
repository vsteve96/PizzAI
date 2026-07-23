import json
from pathlib import Path


RESTAURANT_FILE = Path("data/restaurants.json")


def load_restaurants():
    if not RESTAURANT_FILE.exists():
        return []

    with open(RESTAURANT_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_restaurants(restaurants):
    with open(RESTAURANT_FILE, "w", encoding="utf-8") as file:
        json.dump(
            restaurants,
            file,
            ensure_ascii=False,
            indent=2
        )


def add_restaurant(
    name,
    sources=None
):
    restaurants = load_restaurants()

    existing = [
        r["name"].lower()
        for r in restaurants
    ]

    if name.lower() in existing:
        print(f"Már létezik: {name}")
        return

    restaurants.append(
        {
            "name": name,
            "city": "Szeged",
            "sources": sources or [],
            "status": "candidate"
        }
    )

    save_restaurants(restaurants)

    print(f"Hozzáadva: {name}")


if __name__ == "__main__":

    add_restaurant(
        "Teszt Pizza Szeged",
        [
            "website",
            "wolt"
        ]
    )