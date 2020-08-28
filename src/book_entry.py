import json
from src.status import Status
from src.dimension import Dimension
from src.book_type import BookType

class bookEncoder(json.JSONEncoder):
    def default(self, obj):
        if type(obj) is BookType:
            return {"__type_enum__": obj.name}
        if type(obj) is Status:
            return {"__status_enum__": obj.name}
        if type(obj) is Dimension:
            return {"__dimension__" : obj.__dict__} 
        return json.JSONEncoder.default(self, obj)

def bookDecoder(d):
    if "__type_enum__" in d:
        name = d["__type_enum__"]
        return getattr(BookType, name)
    if "__status_enum__" in d:
        name = d["__status_enum__"]
        return getattr(Status, name)
    if "__dimension__" in d:
        new_dict = d["__dimension__"]
        dimension = Dimension()
        dimension.__dict__.update(new_dict)
        return dimension
    return d


class BookEntry:
    
    def __init__(self):

        self._bookID: int = 0
        self._batchID: int = 0
        self._box: str = str()
        self._weight: float = float()
        self._status: Status = Status.UNDEFINED
        self._section: str = str()
        self._spine: float = float()
        self._threadColor: str = str()
        self._headbandColor: str = str()
        self._booktype: BookType = BookType.UNDEFINED
        self._extra: str = str()
        self._costExtra: float = float()

        self._pageDim: Dimension = Dimension()
        self._pageMaterial: str = str()
        self._signitures: int = int()
        self._pagesPerSigniture: int = int()

        self._coverDim: Dimension = Dimension()
        self._coverMaterial: str = str()


    def saveToJSONFile(self, fp) -> str:
        return json.dump(self.__dict__, fp, cls=bookEncoder)

    def loadFromJSONFile(self, fp) -> None:
        self.__dict__.update(json.load(fp, object_hook=bookDecoder))
 
    def calculatePaperCount(self):
        return self.signitures * self.pagesPerSigniture
    
    # BookID props

    @property
    def bookID(self):
        return self._bookID

    @bookID.setter
    def bookID(self, value: int):
        self._bookID = value

    # batchID props
    @property
    def batchID(self):
        return self._bookID

    @batchID.setter
    def batchID(self, value: int):
        self._batchID = value
    # box props

    @property
    def box(self):
        return self._box

    @box.setter
    def box(self, value: str):
        self._box = value

    # weight props

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value: float):
        self._weight = value

    # status props

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: Status):
        self._status = value

    # section props

    @property
    def section(self):
        return self._section

    @section.setter
    def section(self, value: str):
        self._section = value

    # spine props

    @property
    def spine(self):
        return self._spine

    @spine.setter
    def spine(self, value: str):
        self._spine = value

    # threadColor props

    @property
    def threadColor(self):
        return self._threadColor

    @threadColor.setter
    def threadColor(self, value: str):
        self._threadColor = value

    # headbandColor props

    @property
    def headbandColor(self):
        return self._headbandColor

    @headbandColor.setter
    def headbandColor(self, value: str):
        self._headbandColor = value

    # booktype props

    @property
    def booktype(self):
        return self._booktype

    @booktype.setter
    def booktype(self, value: BookType):
        self._booktype = value

    # extra props

    @property
    def extra(self):
        return self._extra

    @extra.setter
    def extra(self, value: str):
        self._extra = value

    # pageDim prop

    @property
    def pageDim(self):
        return self._pageDim

    @pageDim.setter
    def pageDim(self, value: Dimension):
        self._pageDim = value

    # pageMaterial props

    @property
    def pageMaterial(self):
        return self._pageMaterial

    @pageMaterial.setter
    def pageMaterial(self, value: str):
        self._pageMaterial = value

    # pages props

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        self._pages = value

    # signitures props

    @property
    def signitures(self):
        return self._signitures

    @signitures.setter
    def signitures(self, value: int):
        self._signitures = value

    # pagesPerSigniture props

    @property
    def pagesPerSigniture(self):
        return self._pagesPerSigniture

    @pagesPerSigniture.setter
    def pagesPerSigniture(self, value: int):
        self._pagesPerSigniture = value

    # coverDim props

    @property
    def coverDim(self):
        return self._coverDim

    @coverDim.setter
    def coverDim(self, value: Dimension):
        self._coverDim = value

    # coverMaterial props

    @property
    def coverMaterial(self):
        return self._coverMaterial

    @coverMaterial.setter
    def coverMaterial(self, value: str):
        self._coverMaterial = value

    @property
    def costExtra(self):
        return self._costExtra

    @costExtra.setter
    def costExtra(self, value: float):
        self._costExtra = value