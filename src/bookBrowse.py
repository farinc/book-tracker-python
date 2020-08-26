from PyQt5.QtWidgets import QDialog, QListWidgetItem
from PyQt5 import uic
import os
import json
class bookBrowse(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("./ui/bookBrowser.ui", self)
        self.openButton.clicked.connect(self.openBook)
        self.book_path : str = "./Books"
        #discover all batch folders
        batches = []
        for b in os.listdir(self.book_path):
            if os.path.isdir(self.book_path+"/"+b):
                batches.append(b);
        #add batches to list
        self.batchesList.addItems(batches)
        self.batchesList.itemClicked.connect(self.showBooks)
    def showBooks(self, item) :
        books = []
        print(self.booksList.count())
        while self.booksList.count() > 0:
            self.booksList.takeItem(self.booksList.count()-1);
        for b in os.listdir(self.book_path + "/" + item.text()):
            if os.path.isfile(self.book_path + "/" + item.text() + "/" + b):
                books.append(b.replace(".json", ""));
        self.booksList.addItems(books);
    def showBookInfo(self, item):
        with open('data.txt') as book_json:
            data = json.load(book_json)
            
    def openBook(self):
        self.booksList.addItem(QListWidgetItem("test"))