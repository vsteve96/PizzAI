from ddgs import DDGS


def search_web(query, max_results=10):
    results = []

    with DDGS() as ddgs:
        for result in ddgs.text(
            query,
            max_results=max_results
        ):
            results.append(
                {
                    "title": result.get("title"),
                    "url": result.get("href"),
                    "description": result.get("body")
                }
            )

    return results


if __name__ == "__main__":

    query = "Szeged pizza pizzéria"

    hits = search_web(query)

    for hit in hits:
        print("----------------")
        print(hit["title"])
        print(hit["url"])