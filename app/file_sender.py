import shutil
from pathlib import Path

from app.config import DESTINATION_FOLDER


def send_file(file_path: str):

    source = Path(file_path)

    if not source.exists():
        return False, "ไม่พบไฟล์"

    if not DESTINATION_FOLDER.exists():
        return False, "ปลายทางไม่พร้อมใช้งาน"

    try:

        shutil.copy2(
            source,
            DESTINATION_FOLDER / source.name,
        )

        return True, "ส่งไฟล์สำเร็จ"

    except Exception as e:

        return False, str(e)