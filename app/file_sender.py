import shutil
from pathlib import Path

from app.config import DESTINATION_FOLDER


def send_file(file_path: str):
    source = Path(file_path)

    if not source.exists():
        return False, "ไม่พบไฟล์ต้นฉบับ"

    if not DESTINATION_FOLDER.exists():
        return False, "NAS ไม่พร้อมใช้งาน"

    destination = DESTINATION_FOLDER / source.name

    try:
        shutil.copy2(source, destination)
        return True, f"ส่งไฟล์สำเร็จ → {destination}"

    except Exception as e:
        return False, str(e)