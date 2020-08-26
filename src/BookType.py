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
class bookEnumEncoder(json.JSONEncoder):
    def default(self, obj):
        if type(obj) is BookType:
            return {"__book_enum__": obj.name}
        return json.JSONEncoder.default(self, obj)

def bookEnumDecoder(d):
    if "__book_enum__" in d:
        name = d["__book_enum__"]
        return getattr(BookType, name)
    else:
        return d
