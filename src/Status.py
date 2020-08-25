from enum import Enum

class Status(Enum):
    NOPHOTO: int = 0
    DRAFT: int = 1
    DRAFTNOPHOTO: int = 2
    PUBLISHED: int = 3
    SOLD: int = 4
