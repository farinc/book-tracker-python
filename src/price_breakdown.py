from PyQt5.QtWidgets import QDialog, QListWidgetItem
from PyQt5 import uic
from src.book_type import BookType
from src.fs_utils import FsUtils

class PriceBreakdown(QDialog):

    def __init__(self, parent):
        super().__init__(parent)
        cost = parent.cost
        book = parent.activeBook
        uic.loadUi(FsUtils.get_resource("ui/costbreakdown.ui"), self)

        if cost.canBookBeEvalutated() :
            self.spinDisplayCover.setValue(cost.getBoardCost())
            self.spinDisplayPaper.setValue(cost.getPageCost())
            self.spinDisplaySew.setValue(cost.getThreadRibbonCost())
            self.spinDisplaySuper.setValue(cost.getSuperCost())
            self.spinDisplayCloth.setValue(cost.getClothCost())
            self.spinDisplayHeadband.setValue(cost.getHeadbandCost())
            self.spinDisplayExtra.setValue(cost.getExtraCosts())

            if book.booktype is BookType.STAB:
                self.labelSewType.setText("Ribbon")
            else:
                self.labelSewType.setText("Thread")

        