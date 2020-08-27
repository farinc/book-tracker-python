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

    def getDisplayText(self) -> str:
        if self is BookType.COPTIC:
            return "Coptic"
        elif self is BookType.COPTIC2NEEDLE:
            return "Copic with 2 needles"
        elif self is BookType.LONG:
            return "Long stich"
        elif self is BookType.QUARTER:
            return "Quarter"
        elif self is BookType.STAB:
            return "Stab stich"
        elif self is BookType.TRADITIONAL:
            return "Traditional"
        return None