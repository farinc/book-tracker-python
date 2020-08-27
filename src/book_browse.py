from PyQt5.QtWidgets import QDialog, QListWidgetItem
from PyQt5 import uic
import os
import json
from src.book_entry import BookEntry
from src.book_type import BookType
from src.fs_utils import FsUtils

class bookBrowse(QDialog):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.main = parent
        uic.loadUi("./ui/bookBrowser.ui", self)
        self.buttonOpen.clicked.connect(self.openBook)
        self.buttonCancel.clicked.connect(self.close)
        self.bookSelected = False
        self.book_dir : str = "./Books"
        self.book_id = None
        self.batch_id = None
        """
        discover all batches in the main directory
        """
        batches = FsUtils.getBatches()
        self.batchesList.addItems(batches)
        
        self.batchesList.itemClicked.connect(self.showBooks)
        self.booksList.itemClicked.connect(self.loadBook)

    def showBooks(self, item) :
        self.batch_id : int = item.text()
        while self.booksList.count() > 0:
            self.booksList.takeItem(0)
        books = [n.replace(".json", "") for n in FsUtils.getBooksInBatch(item.text())]
        self.booksList.addItems(books)

    def loadBook(self, item):
        """
        load book entry to show its data in the preview and so it can later pass it to main
        """
        self.book_id = item.text()
        self.book_entry = FsUtils.getBook(self.batch_id, self.book_id)
        self.labelPages.setText(str(self.book_entry.pages))
        self.labelBox.setText(self.book_entry.box)
        self.labelBookType.setText(self.book_entry.booktype.getDisplayText())
        self.labelCoverMaterial.setText(self.book_entry.coverMaterial)
        
    def openBook(self):
        self.main.onEntryLoaded(FsUtils.getBook(self.batch_id, self.book_id))
        self.close()