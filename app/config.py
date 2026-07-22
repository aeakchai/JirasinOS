from pathlib import Path
import os
import json
import platform

# =====================================================
# Search Paths
# =====================================================

if platform.system() == "Windows":
    # ใช้ตอนรันบน Windows (สำหรับพัฒนา)
    DEFAULT_SEARCH_PATHS = [
        Path.home() / "Desktop",
        Path(r"C:\JACK\งาน"),
    ]
else:
    # ใช้ตอนรันบน NAS / Linux
    DEFAULT_SEARCH_PATHS = [
        Path("/mnt/windows/Desktop"),
        Path("/mnt/windows/งาน"),
    ]

search_paths_value = os.getenv("SEARCH_PATHS")

if search_paths_value:
    SEARCH_PATHS = [
        Path(path)
        for path in json.loads(search_paths_value)
    ]
else:
    SEARCH_PATHS = DEFAULT_SEARCH_PATHS

# =====================================================
# NAS Destination
# =====================================================

DEFAULT_DESTINATION_FOLDER = Path(
    "\\\\"
    + os.getenv("NAS_HOST", "192.168.0.78")
    + "\\"
    + os.getenv("NAS_SHARE", "jirasin789")
)

DESTINATION_FOLDER = Path(
    os.getenv(
        "DESTINATION_FOLDER",
        str(DEFAULT_DESTINATION_FOLDER),
    )
)