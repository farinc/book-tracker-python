import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from src.BookBrowse import bookBrowse
from src.BookEntry import BookEntry

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        uic.loadUi("./ui/mainwindow.ui", self)

        self._book: BookEntry = None
        self._hasActiveEntry = False
        
        self.actionNewCurrent.triggered.connect(self.onNewEntryOnCurrentBatch)
        self.actionNewNew.triggered.connect(self.onNewEntryOnNewBatch)
        self.actionLoad.triggered.connect(self.onLoadEntry)
        self.actionClose.triggered.connect(self.onCloseSaveEntry)

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

        self.editCoverColor.setText("")
        self.editHeadbandColor.setText("")
        self.editThreadColor.setText("")
        self.editCoverMaterial.setText("")
        self.editPageMaterial.setText("")
        self.editExtra.setPlainText("")

    def populateUi(self):
        if self.activeBook is None:
            return
        print(self.activeBook.booktype)
        print(self.activeBook.status)
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

        self.editCoverColor.setText(self.activeBook.coverColor)
        self.editHeadbandColor.setText(self.activeBook.headbandColor)
        self.editThreadColor.setText(self.activeBook.threadColor)
        self.editCoverMaterial.setText(self.activeBook.coverMaterial)
        self.editPageMaterial.setText(self.activeBook.pageMaterial)
        self.editExtra.setPlainText(self.activeBook.extra)

    def setUiInactive(self):
        """
        Sets the ui in a state where there is no active book entry
        """
        self.scrollAreaDescription.setEnabled(False) #Disable the stuff with props
        self.actionClose.setEnabled(False) #Disable the close feature
        self.comboMode.setEnabled(False)
        self.hasActiveEntry = False

    def setUiActive(self):
        """
        Sets the ui in a state where the active book entry has been instance
        """
        self.scrollAreaDescription.setEnabled(True) #Enable the stuff with props
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
            #Save first
            if self.activeBook is not None:
                with open("./Books/{batchID}/{bookID}.json".format(batchID=self.activeBook.batchID, bookID=self.activeBook.bookID)) as fp:
                    self.activeBook.saveToJSONFile(fp)

            #Clear ui
            self.clearEditUI()
            self.setUiInactive()

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
