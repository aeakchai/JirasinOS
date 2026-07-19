from pathlib import Path

SEARCH_PATHS = [
    Path.home() / "Desktop",
]


def search_files(keyword):

    keyword = keyword.strip().lower()

    if keyword == "":
        return []

    results = []

    for folder in SEARCH_PATHS:

        if not folder.exists():
            continue

        for file in folder.rglob("*"):

            if file.is_file() and keyword in file.name.lower():

                results.append({
                    "name": file.name,
                    "folder": str(file.parent),
                    "path": str(file)
                })

    results.sort(key=lambda x: x["name"])

    return results