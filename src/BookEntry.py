import json
from src.Status import Status
from src.Dimension import Dimension
from src.BookType import BookType

class BookEntry:
    
    def __init__(self):

        self._bookID: int = None
        self._box: str = None
        self._weight: float = None
        self._status: Status = None
        self._section: str = None
        self._spine: float = None
        self._threadColor: str = None
        self._headbandColor: str = None
        self._booktype: BookType = None
        self._extra: str = None

        self._pageDim: Dimension = None
        self._pageMaterial: str = None
        self._pages: int = None
        self._signitures: int = None
        self._pagesPerSigniture: int = None

        self._coverDim: Dimension = None
        self._coverColor: str = None
        self._coverMaterial: str = None


    def saveToJSON(self) -> str:
        return json.dumps(self.__dict__)

    def loadFromJSON(self, json_object) -> None:
        self.__dict__.update(json.loads(json_object))
 
    # BookID props

    @property
    def bookID(self):
        return self._bookID

    @bookID.setter
    def bookID(self, value: int):
        self._bookID = value

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

    # coverColor props

    @property
    def coverColor(self):
        return self._coverColor

    @coverColor.setter
    def coverColor(self, value: str):
        self._coverColor = value

    # coverMaterial props

    @property
    def coverMaterial(self):
        return self._coverMaterial

    @coverMaterial.setter
    def coverMaterial(self, value: str):
        self._coverMaterial = value