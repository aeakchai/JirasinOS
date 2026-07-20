from app.indexer import get_index


def search_files(keyword: str):

    keyword = keyword.strip().lower()

    if not keyword:
        return []

    results = []

    for item in get_index():

        if keyword in item["name"].lower():

            results.append(item)

    return results