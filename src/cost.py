from src.book_entry import BookEntry
from src.book_type import BookType
import math as Math
import json
import os

class Cost:

    def __init__(self, book: BookEntry):

        # Padding constants
        self.paddingWidthBoard: float = 2.0
        self.paddingHeightBoard: float = 2.0
        self.paddingSpineLongTrad: float = 3.0
        self.paddingSpineQuarter: float = 5.0
        self.paddingSpineForSuper: float = 2.0

        # Pricing constants
        self.sqInchBoardPrice: float = 0.02
        self.sheetPrice: float = 0.05
        self.sqInchClothPrice: float = 0.02
        self.threadLengthPrice: float = 0.002
        self.headbandPrice: float = 0.1
        self.superPrice: float = 0.02
        self.ribbonPrice: float = 0.10
        self.pvaCost: float = 0.5
        self.endpageCost: float = 0.5

        self._book: BookEntry = book

    def saveToJSONFile(self, fp) -> str:
        return json.dump(self.__dict__, fp)

    def loadFromJSONFile(self, fp) -> None:
        self.__dict__.update(json.load(fp))

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value: BookEntry):
        self._book = value

    def canBookBeEvalutated(self) -> bool:
        """Determines if the book instance can be evaluted using this class.
        If true, then it is safe to allow the given instance to be set.

        Returns:
            bool: True if the book can be evaluated and False otherwise
        """
        if self.book is not None:

            hasCoverDim = self.book.coverDim.width > 0 and self.book.coverDim.height > 0
            hasPageDim = self.book.pageDim.width > 0 and self.book.pageDim.height > 0
            hasSpine = self.book.spine > 0
            hasPageCount = self.book.calculatePaperCount() > 0
            hasBookType = self.book.booktype is not BookType.UNDEFINED

            flag = hasCoverDim and hasPageDim and hasSpine and hasPageCount and hasBookType
            return flag
        return False

    def getTotalCost(self) -> float:
        total: float = 0

        total += self.getBoardCost()
        total += self.getPageCost()
        total += self.getThreadRibbonCost()
        total += self.getClothCost()
        total += self.getHeadbandCost()
        total += self.getSuperCost()
        total += self.getExtraCosts()

        return total

    def getExtraCosts(self) -> float:
        return self.book.costExtra + self.pvaCost + self.endpageCost
        
    def getBoardCost(self) -> float:
        """Gets the cost for the board (used for the cover)

        Books: ALL

        Returns:
            float: the price for board for this book
        """
        paddedWidth = self.book.coverDim.width + self.paddingWidthBoard
        paddedHeight = self.book.coverDim.height + self.paddingHeightBoard

        sqInchBoard = paddedHeight * paddedWidth
        priceBoard = sqInchBoard * self.sqInchBoardPrice
        
        return priceBoard

    def getPageCost(self) -> float:
        """Calculates the cost associated with the number of 
        paper sheets used and the size of the paper. This is
        seperate from the cost of the paper material (added as 
        extra) and the cost of the signitures

        Books: ALL

        Returns:
            float: the cost for pages
        """
        sheets = Math.ceil(self.book.calculatePaperCount() / 2) #If it is a odd number, we round up...
        ishalfSheet = self.book.pageDim.width <= 4.25 or self.book.pageDim.height <= 5

        pricePages = sheets * self.sheetPrice

        if ishalfSheet:
            return pricePages / 2
        else:
            return pricePages

    def getThreadRibbonCost(self) -> float:
        """Calculates the thread or ribbon cost

        Books: All
        """

        if(self.book.booktype is BookType.TRADITIONAL or self.book.booktype is BookType.QUARTER or self.book.booktype is BookType.COPTIC or self.book.booktype is BookType.COPTIC2NEEDLE or self.book.booktype is BookType.LONG):
            # added height is the padding for the thread length
            threadLength = (self.book.signitures * self.book.coverDim.height) + self.book.coverDim.height
            priceThread = threadLength * self.threadLengthPrice

            if self.book.booktype == BookType.COPTIC2NEEDLE:
                priceThread = priceThread * 2
            
            return priceThread
        elif self.book.booktype is BookType.STAB:
            return self.book.coverDim.height * self.ribbonPrice

        return 0

    def getHeadbandCost(self) -> float:
        """Calculates the headband cost

        Books: TRAD	and QUARTER
        """

        if(self.book.booktype is BookType.TRADITIONAL or self.book.booktype is BookType.QUARTER):
            return self.book.spine * 2 * self.headbandPrice
        return 0

    def getSuperCost(self) -> float:
        """Calculates the super (mall) cost

        Books: TRAD and QUARTER
        """

        if(self.book.booktype is BookType.TRADITIONAL or self.book.booktype is BookType.QUARTER):
            paddedSpine = self.book.spine + self.paddingSpineForSuper
            sqInchSuper = paddedSpine * self.book.coverDim.height
            return sqInchSuper * self.superPrice
        return 0

    def getClothCost(self) -> float:
        """Calculates the bookcloth cost for different style books

        Books: COPTIC, COPTIC2NEEDLE, STAB, QUARTER, LONG

        """
        if self.book.booktype is BookType.COPTIC or self.book.booktype is BookType.COPTIC2NEEDLE or self.book.booktype is BookType.STAB:
            paddedWidth = self.book.coverDim.width + self.paddingWidthBoard
            paddedHeight = self.book.coverDim.height + self.paddingHeightBoard

            sqInchCloth = paddedHeight * paddedWidth * 2 # Same thing, two covers, twice the amount in cloth
            
            return sqInchCloth * self.sqInchClothPrice

        elif self.book.booktype is BookType.LONG or self.book.booktype is BookType.QUARTER or BookType.TRADITIONAL:
            paddedHeight = self.book.coverDim.height + self.paddingHeightBoard
            
            paddedSpine: float = self.book.spine
            if self.book.booktype == BookType.QUARTER:
                paddedSpine += self.paddingSpineQuarter
            elif self.book.booktype == BookType.LONG or self.book.booktype == BookType.TRADITIONAL:
                paddedSpine += self.paddingSpineLongTrad


            paddedWidth = self.book.coverDim.width + self.paddingWidthBoard + paddedSpine
            sqInchCloth = float(paddedWidth * paddedHeight)
            return sqInchCloth * self.sqInchClothPrice
        return 0