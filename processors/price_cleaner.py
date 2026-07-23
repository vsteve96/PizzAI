import re


def clean_price(value):

    value = value.lower()

    value = (
        value
        .replace("ft", "")
        .replace(".", "")
        .replace(" ", "")
        .replace(",", "")
        .replace("-", "")
    )

    numbers = re.findall(
        r"\d+",
        value
    )

    if not numbers:
        return None

    price = int(numbers[0])

    return price


if __name__ == "__main__":

    tests = [
        "1800 Ft",
        "1.800 Ft",
        "3 490 Ft",
        "2990,-"
    ]

    for test in tests:
        print(
            test,
            "→",
            clean_price(test)
        )