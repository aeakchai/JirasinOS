from pathlib import Path
from datetime import datetime
from app.config import SEARCH_PATHS

# เก็บข้อมูลไฟล์ทั้งหมดไว้ใน RAM
DXF_INDEX = []


def format_size(size: int) -> str:
    """แปลงขนาดไฟล์ให้อ่านง่าย"""
    if size >= 1024 * 1024:
        return f"{size / 1024 / 1024:.2f} MB"
    elif size >= 1024:
        return f"{size / 1024:.2f} KB"
    else:
        return f"{size} Bytes"


def build_index():

    global DXF_INDEX

    DXF_INDEX.clear()

    print("=" * 50)
    print("JirasinOS DXF Index")
    print("=" * 50)

    total = 0

    for folder in SEARCH_PATHS:

        print(f"Scanning : {folder}")

        if not folder.exists():
            print("   Folder not found")
            continue

        for file in folder.rglob("*.dxf"):

            try:

                stat = file.stat()

                DXF_INDEX.append(
                    {
                        "name": file.name,
                        "folder": str(file.parent),
                        "path": str(file),
                        "modified": datetime.fromtimestamp(
                            stat.st_mtime
                        ).strftime("%d/%m/%Y %H:%M"),
                        "timestamp": stat.st_mtime,
                        "size": format_size(stat.st_size),
                    }
                )

                total += 1

            except Exception as e:
                print(f"Skip : {file}")
                print(e)

    DXF_INDEX.sort(
        key=lambda x: x["timestamp"],
        reverse=True,
    )

    print("=" * 50)
    print(f"Indexed : {total:,} DXF Files")
    print("Ready")
    print("=" * 50)


def get_index():
    return DXF_INDEX