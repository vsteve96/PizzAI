from utils.models import Pizza
from excel.exporter import export_pizzas


def main():

    pizzak = [

        Pizza(
            restaurant="Teszt Pizzéria",
            name="Margherita",
            size="32 cm",
            price=2990,
            category="klasszikus",
            source="teszt"
        ),

        Pizza(
            restaurant="Teszt Pizzéria",
            name="Sonkás",
            size="32 cm",
            price=3490,
            category="klasszikus",
            source="teszt"
        ),

        Pizza(
            restaurant="Teszt Pizzéria",
            name="Négysajtos",
            size="32 cm",
            price=3690,
            category="sajtos",
            source="teszt"
        )
    ]


    export_pizzas(
        pizzak,
        "output/szegedi_pizzak.xlsx"
    )


if __name__ == "__main__":
    main()