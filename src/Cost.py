from src.BookEntry import BookEntry
from src.BookType import BookType
import math as Math
import json
import os
class Cost:

    def __init__(self):
        super().__init__()

        def __init__(self):
            # Padding constants
            self.paddingWidthBoard = 2.0
            self.paddingHeightBoard = 2.0
            self.paddingSpineLong = 3.0
            self.paddingSpineQuarter = 5.0
            self.paddingSpineForSuper = 2.0

            # Pricing constants
            self.sqInchBoardPrice = 0.02
            self.sheetPrice = 0.05
            self.sqInchClothPrice = 0.02
            self.threadLengthPrice = 0.002
            self.headbandPrice = 0.1
            self.superPrice = 0.02
            self.ribbonPrice = 0.10
            if(os.path.)
            self.saveToJSON()
            self.loadFromJSON()

    def saveToJSONFile(self, fp) -> str:
        return json.dump(self.__dict__, fp)

    def loadFromJSONFile(self, fp) -> None:
        self.__dict__.update(json.load(fp))

    @property
    def book(self):
        return self.book
    
    def setBook(self, value: BookEntry) -> bool:
        """Sets the active book entry 

        Args:
            value (BookEntry): the book entry

        Returns:
            bool: True if this value is either None or this 
            entry can be evaluated.
        """
        if value is None:
            self._book = None
            return True
        elif Cost.canBookBeEvalutated(value):
            self._book = value
            return True
        else:
            return False

    @staticmethod
    def canBookBeEvalutated(value: BookEntry) -> bool:
        """Determines if a given book can be evaluted using this class.
        If true, then it is safe to allow the given instance to be set.

        Args:
            book (BookEntry): a book entry object

        Returns:
            bool: True if the book can be evaluated and False otherwise
        """
        isCoverDim = value.coverDim is not None
        isSpine = value.spine is not None
        isSignitures = value.signitures is not None
        isBookType = value.booktype is not None

        return isCoverDim and isSpine and isSignitures and isBookType


    def getBoardCost(self) -> float:
        """Gets the cost for the board (used for the cover)

        Returns:
            float: the price for board for this book
        """
        paddedWidth = self.book.coverDim.width + self.paddingWidthBoard
        paddedHeight = self.book.coverDim.height + self.paddingHeightBoard

        sqInchBoard = paddedHeight * paddedWidth * 2 # the 2 is because there is always two boards for one book
        priceBoard = sqInchBoard * self.sqInchBoardPrice
        
        return priceBoard

    def getPageCost(self) -> float:
        """Calculates the cost associated with the number of 
        paper sheets used and the size of the paper. This is
        seperate from the cost of the paper material (added as 
        extra) and the cost of the signitures

        Returns:
            float: the cost for pages
        """
        sheets = Math.ceil(self.book.pages / 2) #If it is a odd number, we round up...
        ishalfSheet = self.book.pageDim.width <= 4.25 or self.book.pageDim.height <= 5

        pricePages = sheets * self.sheetPrice

        if ishalfSheet:
            return pricePages / 2
        else:
            return pricePages

    def getThreadCost(self) -> float:
        
        # added height is the padding for the thread length
        threadLength = self.book.signitures * self.book.coverDim.height + self.book.coverDim.height
        priceThread = threadLength * self.threadLengthPrice

        if self.book.booktype == BookType.COPTIC2NEEDLE:
            priceThread = priceThread * 2
        
        return priceThread

    def getHeadbandCost(self) -> float:
        return self.book.spine * 2 * self.headbandPrice

    def getSuperCost(self) -> float:
        paddedSpine = self.book.spine + self.paddingSpineForSuper
        sqInchSuper = paddedSpine * self.book.coverDim.height
        return sqInchSuper * self.superPrice

    def getCoptic_StabClothCost(self) -> float:
        """ Gets the cost associated with the coptic and stab-stich 
        styles for bookcloth. This is mostly the same as the book 
        board calculations except its a different price multiplier.

        Returns:
            float: the cost of bookcloth
        """

        paddedWidth = self.book.coverDim.width + self.paddingWidthBoard
        paddedHeight = self.book.coverDim.height + self.paddingHeightBoard

        sqInchCloth = paddedHeight * paddedWidth * 2 # Same thing, two covers, twice the amount in cloth
        priceCloth = sqInchCloth * self.sqInchClothPrice
        
        return priceCloth

    def getLong_QuaterBoundClothCost(self) -> float:
        """Calculates the bookcloth cost for long and quater style books

        Raises:
            ValueError: raised if book is not a long or quater style

        Returns:
            float: the cost for the bookcloth
        """

        paddedHeight = self.book.coverDim.height + self.paddingHeightBoard
        
        paddedSpine = None
        if self.book.booktype == BookType.QUARTER:
            paddedSpine = self.paddingSpineQuarter
        elif self.book.booktype == BookType.LONG:
            paddedSpine = self.paddingSpineLong
        else:
            raise ValueError("Called when book is neither quarter or long")

        paddedWidth = self.book.coverDim.width + self.paddingWidthBoard + paddedSpine
        sqInchCloth = paddedWidth * paddedHeight
        return sqInchCloth * self.sqInchClothPrice

    def getRibbonCost(self) -> float:
        return self.book.coverDim.height * self.ribbonPrice




    