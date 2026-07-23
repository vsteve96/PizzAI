import pandas as pd
from utils.models import Pizza


def export_pizzas(pizzas, filename):

    data = []

    for pizza in pizzas:
        data.append({
            "Pizzéria": pizza.restaurant,
            "Pizza": pizza.name,
            "Méret": pizza.size,
            "Ár (Ft)": pizza.price,
            "Kategória": pizza.category,
            "Forrás": pizza.source,
            "Gyűjtés dátuma": pizza.collected_at
        })

    df = pd.DataFrame(data)

    df.to_excel(
        filename,
        index=False
    )

    print(f"Excel elkészült: {filename}")