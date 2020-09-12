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
        uic.loadUi(FsUtils.get_resource("/ui/bookbrowser.ui"), self)
        self.accepted.connect(self.openBook)
        self.bookSelected = None
        self.book_id = None
        self.batch_id = None
        """
        discover all batches in the main directory
        """
        batches = FsUtils.get_batches()
        self.batchesList.addItems(batches)
        
        self.batchesList.itemClicked.connect(self.showBooks)
        self.booksList.itemClicked.connect(self.loadBook)

    def showBooks(self, item) :
        self.batch_id : int = item.text()
        while self.booksList.count() > 0:
            self.booksList.takeItem(0)
        books = [n.replace(".json", "") for n in FsUtils.get_books_in_batch(item.text())]
        self.booksList.addItems(books)

    def loadBook(self, item):
        """
        load book entry to show its data in the preview and so it can later pass it to main
        """
        self.book_id = item.text()
        self.bookSelected = FsUtils.get_book(self.book_id, self.batch_id)
        self.labelBox.setText(self.bookSelected.box)
        self.labelBookType.setText(self.bookSelected.booktype.getDisplayText())
        self.labelCoverMaterial.setText(self.bookSelected.coverMaterial)
        
    def openBook(self):
        if self.bookSelected is not None:
            self.main.onEntryLoaded(FsUtils.get_book(self.book_id, self.batch_id))
            self.close()