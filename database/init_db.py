import sqlite3
from pathlib import Path


DB = Path("database/pizza.db")


def main():

    conn = sqlite3.connect(DB)

    cur = conn.cursor()


    cur.execute("""
    CREATE TABLE IF NOT EXISTS restaurants (
        id INTEGER PRIMARY KEY,
        name TEXT,
        city TEXT,
        source TEXT
    )
    """)


    cur.execute("""
    CREATE TABLE IF NOT EXISTS pizzas (
        id INTEGER PRIMARY KEY,
        restaurant_id INTEGER,
        name TEXT,
        description TEXT,
        price INTEGER,
        collected_at TEXT,
        FOREIGN KEY (restaurant_id)
        REFERENCES restaurants(id)
    )
    """)


    conn.commit()
    conn.close()


    print("Adatbázis kész:", DB)


if __name__ == "__main__":
    main()