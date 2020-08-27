from enum import Enum
import json

class BookType(Enum):
    UNDEFINED : int = -1
    TRADITIONAL: int = 0
    COPTIC: int = 1
    COPTIC2NEEDLE: int = 2
    STAB: int = 3
    QUARTER: int = 4
    LONG: int = 5