import json
from pathlib import Path
from datetime import date


INPUT = Path("data/pizzas/clean_pizzas.json")
RESTAURANTS = Path("data/restaurants.json")
OUTPUT = Path("data/pizzas/final_pizzas.json")


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main():

    pizzas = load_json(INPUT)
    restaurants = load_json(RESTAURANTS)

    today = str(date.today())


    restaurant_map = {}

    for r in restaurants:
        if "url" in r:
            key = r["url"]
            restaurant_map[key] = r


    enriched = []


    for pizza in pizzas:

        restaurant = {
            "name": "Ismeretlen",
            "city": "Szeged",
            "source": pizza["source_file"]
        }


        if "pizzatorony" in pizza["source_file"]:
            restaurant = {
                "name": "PizzaToronySzeged",
                "city": "Szeged",
                "source": "website"
            }


        enriched.append({

            **pizza,

            "restaurant": restaurant["name"],
            "city": restaurant["city"],
            "source": restaurant["source"],
            "collected_at": today

        })


    with open(
        OUTPUT,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            enriched,
            f,
            ensure_ascii=False,
            indent=2
        )


    print(
        "Mentve:",
        OUTPUT
    )


if __name__ == "__main__":
    main()