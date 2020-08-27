import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from src.book_browse import bookBrowse
from src.book_entry import BookEntry
from src.book_type import BookType
from src.status import Status

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        uic.loadUi("./ui/mainwindow.ui", self)

        self._book: BookEntry = None
        self._hasActiveEntry = False

        self.comboMode.currentIndexChanged.connect(self.toggleUi)
        
        self.actionNewCurrent.triggered.connect(self.onNewEntryOnCurrentBatch)
        self.actionNewNew.triggered.connect(self.onNewEntryOnNewBatch)
        self.actionLoad.triggered.connect(self.onLoadEntry)
        self.actionSaveClose.triggered.connect(self.onCloseSaveEntry)

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

    def clearEditUI(self):
        """
        Clears the editing portion of the ui, including the bookID and batchID. 
        This is meant to set the ui to a blank state
        """
        self.labelBookID.setText(" <None> ")
        self.labelBatchID.setText(" <None>")
        self.lineCost.setText("")

        self.spinPageDimX.setValue(0.0)
        self.spinPageDimY.setValue(0.0)
        self.spinCoverDimX.setValue(0.0)
        self.spinCoverDimY.setValue(0.0)
        self.spinSpineDim.setValue(0.0)
        self.spinWeight.setValue(0.0)
        self.spinPageCount.setValue(0)
        self.spinSignitures.setValue(0)
        self.spinPagesPerSig.setValue(0)

        self.editHeadbandColor.setText("")
        self.editBox.setText("")
        self.editSection.setText("")
        self.editThreadColor.setText("")
        self.editCoverMaterial.setText("")
        self.editPageMaterial.setText("")
        self.editExtra.setPlainText("")

    def populateUi(self):
        """
        Does the opposite of the clearUi function. With a load entry, it fills in all 
        the values that are in the book entry
        """
        if self.activeBook is None:
            return
        self.labelBookID.setText(str(self.activeBook.bookID))
        self.labelBatchID.setText(str(self.activeBook.batchID))
        self.lineCost.setText("")

        self.spinPageDimX.setValue(self.activeBook.pageDim.width)
        self.spinPageDimY.setValue(self.activeBook.pageDim.height)
        self.spinCoverDimX.setValue(self.activeBook.coverDim.width)
        self.spinCoverDimY.setValue(self.activeBook.coverDim.height)
        self.spinSpineDim.setValue(self.activeBook.spine)
        self.spinWeight.setValue(self.activeBook.weight)
        self.spinPageCount.setValue(self.activeBook.pages)
        self.spinSignitures.setValue(self.activeBook.signitures)
        self.spinPagesPerSig.setValue(self.activeBook.pagesPerSigniture)

        self.editHeadbandColor.setText(self.activeBook.headbandColor)
        self.editBox.setText(self.activeBook.box)
        self.editSection.setText(self.activeBook.section)
        self.editThreadColor.setText(self.activeBook.threadColor)
        self.editCoverMaterial.setText(self.activeBook.coverMaterial)
        self.editPageMaterial.setText(self.activeBook.pageMaterial)
        self.editExtra.setPlainText(self.activeBook.extra)
        
        #Sets book type
        self.comboBookType.setCurrentIndex(self.activeBook.booktype.value)
        
        #Sets the radio button
        status = self.activeBook.status
        if status is Status.NOPHOTO:
            self.radioButtonNoPhoto.setChecked(True)
        elif status is Status.DRAFT:
            self.radioButtonDrafted.setChecked(True)
        elif status is Status.DRAFTPHOTO:
            self.radioButtonDraftedPhoto.setChecked(True)
        elif status is Status.PUBLISHED:
            self.radioButtonPublished.setChecked(True)
        elif status is Status.SOLD:
            self.radioButtonSold.setChecked(True)
    
    def saveToBook(self):
        """
        Saves what is in the ui to the book for preperation for serialize
        """
        # self.activeBook.cost = self.lineCost.text()

        self.activeBook.pageDim.width = self.spinPageDimX.value()
        self.activeBook.pageDim.height = self.spinPageDimY.value()

        self.activeBook.coverDim.width = self.spinCoverDimX.value()
        self.activeBook.coverDim.height = self.spinCoverDimY.value()

        self.activeBook.spine = self.spinSpineDim.value()
        self.activeBook.weight = self.spinWeight.value()
        self.activeBook.pages = self.spinPageCount.value()
        self.activeBook.signitures = self.spinSignitures.value()
        self.activeBook.pagesPerSigniture = self.spinPagesPerSig.value()

        self.activeBook.headbandColor = self.editHeadbandColor.text()
        self.activeBook.box = self.editBox.text()
        self.activeBook.section = self.editSection.text()
        self.activeBook.threadColor = self.editThreadColor.text()
        self.activeBook.coverMaterial = self.editCoverMaterial.text()
        self.activeBook.pageMaterial = self.editPageMaterial.text()
        self.activeBook.extra = self.editExtra.toPlainText()

        #Sets the book type
        self.activeBook.booktype = BookType.getType(self.comboBookType.currentIndex())
        
        #Sets the radio button
        if self.radioButtonNoPhoto.isChecked():
            self.activeBook.status = Status.NOPHOTO
        elif self.radioButtonDrafted.isChecked():
            self.activeBook.status = Status.DRAFT
        elif self.radioButtonDraftedPhoto.isChecked():
            self.activeBook.status = Status.DRAFTPHOTO
        elif self.radioButtonPublished.isChecked():
            self.activeBook.status = Status.PUBLISHED
        elif self.radioButtonSold.isChecked():
            self.activeBook.status = Status.SOLD

    def toggleUi(self, index):
        if index == 0:
            self.discriptionFrame.setEnabled(True)
        elif index == 1:
            self.discriptionFrame.setEnabled(False)

    def setUiInactive(self):
        """
        Sets the ui in a state where there is no active book entry
        """
        self.toggleUi(1) #Disable the stuff with props
        self.actionClose.setEnabled(False) #Disable the close feature
        self.comboMode.setEnabled(False)
        self.hasActiveEntry = False

    def setUiActive(self):
        """
        Sets the ui in a state where the active book entry has been instance
        """
        self.toggleUi(0) #Enable the stuff with props
        self.actionClose.setEnabled(True) #Enable the close feature
        self.comboMode.setEnabled(True)
        self.hasActiveEntry = True

    def onLoadEntry(self):
        dlg = bookBrowse(self)
        dlg.exec()

    def onEntryLoaded(self, book: BookEntry):
        self.setUiActive()
        self.hasActiveEntry = True
        self.activeBook = book
        self.populateUi()

    def onNewEntryOnCurrentBatch(self):
        pass

    def onNewEntryOnNewBatch(self):
        pass

    def onCloseSaveEntry(self):
        if self.hasActiveEntry:
            self.saveToBook()

            #Save first
            with open("./Books/{batchID}/{bookID}.json".format(batchID=self.activeBook.batchID, bookID=self.activeBook.bookID), 'w') as fp:
                self.activeBook.saveToJSONFile(fp)

            #Clear ui
            self.clearEditUI()
            self.setUiInactive()

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
