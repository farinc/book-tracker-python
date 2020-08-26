import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from src.bookBrowse import bookBrowse
from src.BookEntry import BookEntry

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        uic.loadUi("./ui/mainwindow.ui", self)

        self.activeBook = BookEntry()
        
        self.actionNew.triggered.connect(self.onNewEntry)
        self.actionLoad.triggered.connect(self.onLoadEntry)
        self.actionClose.triggered.connect(self.onCloseEntry)

    def onLoadEntry(self):
        dlg = bookBrowse(window)
        dlg.exec()

    def onNewEntry(self):
        pass

    def onCloseEntry(self):
        pass

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
