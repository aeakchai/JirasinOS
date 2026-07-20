from dataclasses import dataclass, field, asdict
from typing import List


@dataclass
class FileMetadata:
    id: str
    name: str
    extension: str
    folder: str
    path: str

    size: int
    modified: float

    customer: str = ""
    project: str = ""
    material: str = ""
    thickness: str = ""

    favorite: bool = False

    tags: List[str] = field(default_factory=list)

    preview: str = ""

    file_hash: str = ""

    def to_dict(self):
        return asdict(self)