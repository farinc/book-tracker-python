from enum import Enum

class Status(Enum):
    UNDEFINED: int = -1
    NOPHOTO: int = 0
    DRAFT: int = 1
    DRAFTPHOTO: int = 2
    PUBLISHED: int = 3
    SOLD: int = 4

