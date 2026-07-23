import json
from pathlib import Path
from bs4 import BeautifulSoup

from processors.price_cleaner import clean_price


RAW_DIR = Path("data/raw")
OUTPUT = Path("data/pizzas/pizzas.json")


def extract_pizzas(html_file):

    with open(html_file, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "lxml")

    pizzas = []

    products = soup.select(".product")

    print("Termék blokkok:", len(products))

    for product in products:

        name = product.select_one(".product-desc h4 a")

        if not name:
            continue

        name = name.get_text(strip=True)

        # ideiglenesen minden product blokk pizza
        # később kategória alapján szűrjük

        desc = product.select_one(".product-desc p")

        description = ""

        if desc:
            description = desc.get_text(" ", strip=True)


        price = product.select_one(".product-desc > .product-price")

        price_value = None

        if price:
            price_value = clean_price(
                price.get_text(strip=True)
            )


        pizzas.append({
            "source_file": html_file.name,
            "name": name,
            "description": description,
            "price": price_value
        })


    return pizzas



def main():

    all_pizzas = []

    for html in RAW_DIR.glob("*.html"):

        print("Feldolgozás:", html.name)

        pizzas = extract_pizzas(html)

        all_pizzas.extend(pizzas)


    OUTPUT.parent.mkdir(
        exist_ok=True
    )

    with open(
        OUTPUT,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            all_pizzas,
            f,
            ensure_ascii=False,
            indent=2
        )


    print("Talált pizzák:", len(all_pizzas))
    print("Mentve:", OUTPUT)



if __name__ == "__main__":
    main()