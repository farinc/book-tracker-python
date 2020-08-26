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

        self._book: BookEntry = BookEntry()
        self._hasActiveEntry = False
        
        self.actionNewCurrent.triggered.connect(self.onNewEntryOnCurrentBatch)
        self.actionNewNew.triggered.connect(self.onNewEntryOnNewBatch)
        self.actionLoad.triggered.connect(self.onLoadEntry)
        self.actionClose.triggered.connect(self.onCloseEntry)

        self.setUiInactive()

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value: BookEntry):
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

    def setUiInactive(self):
        """
        Sets the ui in a state where there is no active book entry
        """
        self.scrollAreaDescription.setEnabled(False) #Disable the stuff with props
        self.actionClose.setEnabled(False) #Disable the close feature
        self.comboMode.setEnabled(False)

    def setUiActive(self):
        """
        Sets the ui in a state where the active book entry has been instance
        """
        self.scrollAreaDescription.setEnabled(True) #Enable the stuff with props
        self.actionClose.setEnabled(True) #Enable the close feature
        self.comboMode.setEnabled(True)

    def onLoadEntry(self):
        dlg = bookBrowse(self)
        dlg.exec()

    def onEntryLoaded(self, book: BookEntry):
        self.setUiActive()
        self.activeBook = book
    def onNewEntryOnCurrentBatch(self):
        pass

    def onNewEntryOnNewBatch(self):
        pass

    def onCloseEntry(self):
        if not self.hasActiveEntry:
            self.clearEditUI()
        else:
            pass

    def createBatch(self):
        pass

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
