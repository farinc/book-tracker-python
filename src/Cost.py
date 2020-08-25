from src.BookEntry import BookEntry

class Cost:

    # Padding constants
    paddingWidthBoard = 2.0
    paddingHeightBoard = 2.0

    # Pricing constants
    sqInchBoardPrice = 0.02


    def __init__(self, book: BookEntry):
        super().__init__()

        if(canBookBeEvalutated(book)):
            self.book = book

    @staticmethod
    def canBookBeEvalutated(book: BookEntry) -> bool:
        # TODO: Add conditions
        return True

    def getBoardCost(self) -> float:
        paddedWidth = self.book.coverDim.width + self.paddingWidthBoard
        paddedHeigh = self.book.coverDim.height + self.paddingHeightBoard

        sqInchBoard = paddedHeigh * paddedWidth
        priceBoard = sqInchBoard * sqInchBoardPrice
        
        return priceBoard
        




    