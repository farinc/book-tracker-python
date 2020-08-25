from src.Status import Status
from src.Dimension import Dimension
from src.BookType import BookType

class BookEntry:
    
    def __init__(self, id: int):
        self.bookID: int = id

        self.box: str = None
        self.wieght: float = None
        self.status: Status = None
        self.section: str = None
        self.spine: float = None
        self.threadColor: str = None
        self.headbandColor: str = None
        self.booktype: BookType = None
        self.extra: str = None

        self.pageDim: Dimension = None
        self.pageMaterial: str = None
        self.pages: int = None
        self.signitures: int = None
        self.pagesPerSigniture: int = None

        self.coverDim: Dimension = None
        self.coverColor: str = None
        self.coverMaterial: str = None

    # BookID props

    @property
    def bookID(self):
        return self.bookID

    @bookID.setter
    def bookID(self, value: int):
        self._bookID = value

    # box props

    @property
    def box(self):
        return self.box

    @box.setter
    def box(self, value: str):
        self._box = value

    # weight props

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, value: float):
        self._weight = value

    # status props

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, value: Status):
        self._status = value

    # section props

    @property
    def section(self):
        return self.section

    @section.setter
    def section(self, value: str):
        self._section = value

    # spine props

    @property
    def spine(self):
        return self.spine

    @spine.setter
    def spine(self, value: str):
        self._spine = value

    # threadColor props

    @property
    def threadColor(self):
        return self.threadColor

    @threadColor.setter
    def threadColor(self, value: str):
        self._threadColor = value

    # headbandColor props

    @property
    def headbandColor(self):
        return self.headbandColor

    @headbandColor.setter
    def headbandColor(self, value: str):
        self._headbandColor = value

    # booktype props

    @property
    def booktype(self):
        return self.booktype

    @booktype.setter
    def booktype(self, value: BookType):
        self._booktype = value

    # extra props

    @property
    def extra(self):
        return self.extra

    @extra.setter
    def extra(self, value: str):
        self._extra = value

    # pageDim prop

    @property
    def pageDim(self):
        return self.pageDim

    @pageDim.setter
    def pageDim(self, value: Dimension):
        self._pageDim = value

    # pageMaterial props

    @property
    def pageMaterial(self):
        return self.pageMaterial

    @pageMaterial.setter
    def pageMaterial(self, value: str):
        self._pageMaterial = value

    # pages props

    @property
    def pages(self):
        return self.pages

    @pages.setter
    def pages(self, value: int):
        self._pages = value

    # signitures props

    @property
    def signitures(self):
        return self.signitures

    @signitures.setter
    def signitures(self, value: int):
        self._signitures = value

    # pagesPerSigniture props

    @property
    def pagesPerSigniture(self):
        return self.pagesPerSigniture

    @pagesPerSigniture.setter
    def pagesPerSigniture(self, value: int):
        self._pagesPerSigniture = value

    # coverDim props

    @property
    def coverDim(self):
        return self.coverDim

    @coverDim.setter
    def coverDim(self, value: Dimension):
        self._coverDim = value

    # coverColor props

    @property
    def coverColor(self):
        return self.coverColor

    @coverColor.setter
    def coverColor(self, value: str):
        self._coverColor = value

    # coverMaterial props

    @property
    def coverMaterial(self):
        return self.coverMaterial

    @coverMaterial.setter
    def coverMaterial(self, value: str):
        self._coverMaterial = value