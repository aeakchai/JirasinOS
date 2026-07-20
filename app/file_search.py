from app.indexer import get_index


def search_files(keyword: str):
    """
    ค้นหาไฟล์จาก RAM Index

    รองรับทั้ง dict (เวอร์ชันเดิม)
    และ FileMetadata (เวอร์ชันใหม่)
    """

    keyword = keyword.strip().lower()

    if not keyword:
        return []

    results = []

    for item in get_index():

        # ---------- รองรับ dict ----------
        if isinstance(item, dict):

            name = item.get("name", "")

        # ---------- รองรับ FileMetadata ----------
        else:

            name = getattr(item, "name", "")

        if keyword in name.lower():

            results.append(item)

    return results