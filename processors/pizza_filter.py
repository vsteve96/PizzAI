import json
from pathlib import Path


INPUT = Path("data/pizzas/pizzas.json")
OUTPUT = Path("data/pizzas/clean_pizzas.json")


PIZZA_WORDS = [
    "pizza",
    "sonka",
    "sajtos",
    "szalámi",
    "kukorica",
    "négy évszak",
    "húshegy"
]


IGNORE_WORDS = [
    "tál",
    "rántott",
    "hús -",
    "hamburger"
]


def is_pizza(item):

    text = (
        item["name"] + " " +
        item["description"]
    ).lower()


    if any(word in text for word in IGNORE_WORDS):
        return False


    return any(
        word in text
        for word in PIZZA_WORDS
    )



def main():

    with open(
        INPUT,
        encoding="utf-8"
    ) as f:
        pizzas = json.load(f)


    clean = [
        pizza
        for pizza in pizzas
        if is_pizza(pizza)
    ]


    with open(
        OUTPUT,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            clean,
            f,
            ensure_ascii=False,
            indent=2
        )


    print(
        "Tiszta pizzák:",
        len(clean)
    )


if __name__ == "__main__":
    main()