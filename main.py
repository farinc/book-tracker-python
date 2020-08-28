import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from src.book_browse import bookBrowse
from src.book_entry import BookEntry
from src.book_type import BookType
from src.cost import Cost
from src.status import Status
from src.fs_utils import FsUtils
from src.price_breakdown import PriceBreakdown

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        uic.loadUi("./ui/mainwindow.ui", self)

        self._book: BookEntry = None
        self._cost: Cost = None
        self._hasActiveEntry = False

        self.setupSlots()

        self.setUiInactive()

    @property
    def activeBook(self):
        return self._book

    @activeBook.setter
    def activeBook(self, value: BookEntry):
        self._book = value

    @property
    def hasActiveEntry(self):
        return self._hasActiveEntry

    @hasActiveEntry.setter
    def hasActiveEntry(self, value: bool):
        self._hasActiveEntry = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value: Cost):
        self._cost = value

    def setupSlots(self):
        # General button push slots

        self.comboMode.currentIndexChanged.connect(self.toggleUi)
        self.actionNewCurrent.triggered.connect(self.onNewEntryOnCurrentBatch)
        self.actionNewNew.triggered.connect(self.onNewEntryOnNewBatch)
        self.actionLoad.triggered.connect(self.onLoadEntry)
        self.actionSaveClose.triggered.connect(self.onCloseSaveEntry)
        self.buttonCostBreakdown.clicked.connect(self.onOpenBreakdown)

        #Setup slots for ui updating

        #Dimensions
        self.spinCoverDimX.valueChanged.connect(lambda value: self.onValueChanges("coverDimX", value))
        self.spinCoverDimY.valueChanged.connect(lambda value: self.onValueChanges("coverDimY", value))
        self.spinPageDimX.valueChanged.connect(lambda value: self.onValueChanges("pageDimX", value))
        self.spinPageDimY.valueChanged.connect(lambda value: self.onValueChanges("pageDimY", value))
        self.spinSignitures.valueChanged.connect(lambda value: self.onValueChanges("signitures", value))
        self.spinSpineDim.valueChanged.connect(lambda value: self.onValueChanges("spine", value))
        self.spinExtra.valueChanged.connect(lambda value: self.onValueChanges("extra_cost", value))
        self.spinWeight.valueChanged.connect(lambda value: self.onValueChanges("weight", value))
        self.spinPagesPerSig.valueChanged.connect(lambda value: self.onValueChanges("pages_per_sig", value))

        #Text
        self.editHeadbandColor.textEdited.connect(lambda text: self.onValueChanges("headband_color", text))
        self.editThreadColor.textEdited.connect(lambda text: self.onValueChanges("thread_color", text))
        self.editCoverMaterial.textEdited.connect(lambda text: self.onValueChanges("cover_material", text))
        self.editPageMaterial.textEdited.connect(lambda text: self.onValueChanges("page_material", text))
        self.editSection.textEdited.connect(lambda text: self.onValueChanges("section", text))
        self.editBox.textEdited.connect(lambda text: self.onValueChanges("box", text))
        self.editExtra.textChanged.connect(lambda: self.onValueChanges("extra", self.editExtra.toPlainText()))

        # Combos 
        self.comboBookType.currentIndexChanged.connect(lambda index: self.onValueChanges("book_type", index))
        self.comboStatus.currentIndexChanged.connect(lambda index: self.onValueChanges("status", index))

    def onValueChanges(self, cost_data_type: str, value):
        """A slot function that updates the book with changes to the ui elements

        Args:
            cost_data_type (str): the data type that was changed
            value (): the data to be changed, either a int, float, or str depending on data type
        """
        if self.activeBook is not None and self.hasActiveEntry:
            if cost_data_type == "coverDimX":
                self.activeBook.coverDim.width = value
            elif cost_data_type == "coverDimY":
                self.activeBook.coverDim.height = value
            elif cost_data_type == "pageDimX":
                self.activeBook.pageDim.width = value
            elif cost_data_type == "pageDimY":
                self.activeBook.pageDim.height = value
            elif cost_data_type == "signitures":
                self.activeBook.signitures = value
            elif cost_data_type == "spine":
                self.activeBook.spine = value
            elif cost_data_type == "weight":
                self.activeBook.weight = value
            elif cost_data_type == "pages_per_sig":
                self.activeBook.pagesPerSigniture = value
            elif cost_data_type == "book_type":
                self.activeBook.booktype = BookType(value)
            elif cost_data_type == "extra_cost":
                self.activeBook.costExtra = value
            elif cost_data_type == "headband_color":
                self.activeBook.headbandColor = value
            elif cost_data_type == "thread_color":
                self.activeBook.threadColor = value
            elif cost_data_type == "cover_material":
                self.activeBook.coverMaterial = value
            elif cost_data_type == "page_material":
                self.activeBook.pageMaterial = value
            elif cost_data_type == "section":
                self.activeBook.section = value
            elif cost_data_type == "box":
                self.activeBook.box = value
            elif cost_data_type == "extra":
                self.activeBook.extra = value
            elif cost_data_type == "status":
                self.activeBook.status = Status(value)

            #Update relavent fields

            self.updateCost()
            self.updatePages()

    def updateCost(self):
        if self.cost.canBookBeEvalutated():
            self.spinCost.setValue(round(self.cost.getTotalCost(), 2))
        else:
            self.spinCost.setValue(0.0)

    def updatePages(self):
        self.spinPages.setValue(self.activeBook.calculatePaperCount())

    def clearEditUI(self):
        """
        Clears the editing portion of the ui, including the bookID and batchID. 
        This is meant to set the ui to a blank state
        """
        self.labelBookID.setText(" <None> ")
        self.labelBatchID.setText(" <None>")

        self.spinPageDimX.setValue(0.0)
        self.spinPageDimY.setValue(0.0)
        self.spinCoverDimX.setValue(0.0)
        self.spinCoverDimY.setValue(0.0)
        self.spinSpineDim.setValue(0.0)
        self.spinWeight.setValue(0.0)
        self.spinSignitures.setValue(0)
        self.spinPagesPerSig.setValue(0)
        self.spinExtra.setValue(0.0)

        self.editHeadbandColor.setText("")
        self.editBox.setText("")
        self.editSection.setText("")
        self.editThreadColor.setText("")
        self.editCoverMaterial.setText("")
        self.editPageMaterial.setText("")
        self.editExtra.setPlainText("")

        self.comboBookType.setCurrentIndex(0)
        self.comboStatus.setCurrentIndex(0)

        self.spinCost.setValue(0.0)
        self.spinPages.setValue(0)

    def populateUi(self):
        """
        Does the opposite of the clearUi function. With a load entry, it fills in all 
        the values that are in the book entry
        """
        self.labelBookID.setText(str(self.activeBook.bookID))
        self.labelBatchID.setText(str(self.activeBook.batchID))

        self.spinPageDimX.setValue(self.activeBook.pageDim.width)
        self.spinPageDimY.setValue(self.activeBook.pageDim.height)
        self.spinCoverDimX.setValue(self.activeBook.coverDim.width)
        self.spinCoverDimY.setValue(self.activeBook.coverDim.height)
        self.spinSpineDim.setValue(self.activeBook.spine)
        self.spinWeight.setValue(self.activeBook.weight)
        self.spinSignitures.setValue(self.activeBook.signitures)
        self.spinExtra.setValue(self.activeBook.costExtra)
        self.spinPagesPerSig.setValue(self.activeBook.pagesPerSigniture)

        self.editHeadbandColor.setText(self.activeBook.headbandColor)
        self.editBox.setText(self.activeBook.box)
        self.editSection.setText(self.activeBook.section)
        self.editThreadColor.setText(self.activeBook.threadColor)
        self.editCoverMaterial.setText(self.activeBook.coverMaterial)
        self.editPageMaterial.setText(self.activeBook.pageMaterial)
        self.editExtra.setPlainText(self.activeBook.extra)
        
        self.comboBookType.setCurrentIndex(self.activeBook.booktype.value)
        self.comboStatus.setCurrentIndex(self.activeBook.status.value)

        self.updateCost()
        self.updatePages()

    def toggleUi(self, flag: int):
        """Sets the editing ui as disabled

        Args:
            floag (int): 0 if enable, 1 if disable
        """
        if flag == 0:
            self.discriptionFrame.setEnabled(True)
        elif flag == 1:
            self.discriptionFrame.setEnabled(False)

    def setUiInactive(self):
        """
        Sets the ui in a state where there is no active book entry
        """
        self.hasActiveEntry = False
        self.clearEditUI() #Clear the ui interface
        self.cost = None
        self.toggleUi(1) #Disable the stuff with props
        self.actionClose.setEnabled(False) #Disable the close feature
        self.comboMode.setEnabled(False)

    def setUiActive(self):
        """
        Sets the ui in a state where the active book entry has been instance
        """
        self.initCost()
        self.populateUi() #Load the book data into ui
        self.toggleUi(0) #Enable the stuff with props
        self.actionClose.setEnabled(True) #Enable the close feature
        self.comboMode.setEnabled(True)
        self.hasActiveEntry = True

    def initCost(self):
        self.cost = Cost(self.activeBook)

    def onLoadEntry(self):
        dlg = bookBrowse(self)
        dlg.exec()

    def onEntryLoaded(self, book: BookEntry):
        self.activeBook = book
        self.setUiActive()

    def onNewEntryOnCurrentBatch(self):
        self.activeBook = FsUtils.createBookCurrentBatch()
        self.setUiActive()

    def onNewEntryOnNewBatch(self):
        self.activeBook = FsUtils.createBookNewBatch()
        self.setUiActive()

    def onCloseSaveEntry(self):
        if self.hasActiveEntry:

            #Save first
            FsUtils.saveBook(self.activeBook)

            #Clear ui
            self.setUiInactive()

    def onOpenBreakdown(self):
        dlg = PriceBreakdown(self)
        dlg.exec()

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
