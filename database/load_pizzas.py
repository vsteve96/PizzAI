import sqlite3
import json


DB = "database/pizza.db"
SOURCE = "data/pizzas/final_pizzas.json"


conn = sqlite3.connect(DB)
cursor = conn.cursor()


with open(SOURCE, encoding="utf-8") as f:
    pizzas = json.load(f)


for pizza in pizzas:

    cursor.execute("""
    INSERT OR IGNORE INTO restaurants
    (name, city, source)
    VALUES (?, ?, ?)
    """,
    (
        pizza["restaurant"],
        pizza["city"],
        pizza["source"]
    ))


    cursor.execute("""
    SELECT id FROM restaurants
    WHERE name=?
    """,
    (pizza["restaurant"],))

    restaurant_id = cursor.fetchone()[0]


    cursor.execute("""
    INSERT INTO pizzas
    (
        restaurant_id,
        name,
        description,
        price
    )
    VALUES (?, ?, ?, ?)
    """,
    (
        restaurant_id,
        pizza["name"],
        pizza["description"],
        pizza["price"]
    ))


conn.commit()
conn.close()

print(f"Betöltve: {len(pizzas)} pizza")