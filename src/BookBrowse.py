from PyQt5.QtWidgets import QDialog, QListWidgetItem
from PyQt5 import uic
import os
import json
from src.BookEntry import BookEntry
class bookBrowse(QDialog):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.main = parent
        uic.loadUi("./ui/bookBrowser.ui", self)
        self.buttonOpen.clicked.connect(self.openBook)
        self.buttonCancel.clicked.connect(self.close)
        self.bookSelected = False
        self.book_dir : str = "./Books"
        self.book_file : str = None
        """
        discover all batches in the main directory
        """
        batches = []
        for b in os.listdir(self.book_dir):
            if os.path.isdir(self.book_dir+"/"+b):
                batches.append(b)

        """
        put all the batches in the list
        """
        self.batchesList.addItems(batches)
        self.batchesList.itemClicked.connect(self.showBooks)

        self.booksList.itemClicked.connect(self.showBookInfo)
    def showBooks(self, item) :
        """
        find all books in a batch folder
        """
        books = []
        self.book_file : str = self.book_dir + "/" + item.text()
        while self.booksList.count() > 0:
            self.booksList.takeItem(self.booksList.count()-1)
        for b in os.listdir(self.book_dir + "/" + item.text()):
            if os.path.isfile(self.book_dir + "/" + item.text() + "/" + b):
                books.append(b.replace(".json", ""))
        self.booksList.addItems(books)
    def showBookInfo(self, item):
        """
        load book entry to show its data in the preview and so it can later pass it to main
        """
        self.book_entry = BookEntry()
        with open(self.book_file + "/" + item.text() + ".json", 'r') as book_json_fp:
            self.book_entry.loadFromJSONFile(book_json_fp)
    def openBook(self):
        self.main.onEntryLoaded(self.book_entry)
        self.close()