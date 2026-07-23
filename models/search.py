import sqlite3


DB = "database/pizza.db"


def search(term):

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        restaurants.name,
        pizzas.name,
        pizzas.description,
        pizzas.price
    FROM pizzas
    JOIN restaurants
    ON pizzas.restaurant_id = restaurants.id
    WHERE pizzas.name LIKE ?
    OR pizzas.description LIKE ?
    """,
    (
        f"%{term}%",
        f"%{term}%"
    ))

    results = cursor.fetchall()

    conn.close()

    return results


if __name__ == "__main__":

    query = input("Pizza kereső: ")

    results = search(query.lower())

    print()

    for r in results:
        print("-" * 30)
        print("Pizzéria:", r[0])
        print("Pizza:", r[1])
        print("Leírás:", r[2])
        print("Ár:", r[3], "Ft")