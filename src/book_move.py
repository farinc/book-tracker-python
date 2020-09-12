from PyQt5.QtWidgets import QDialog, QListWidgetItem
from PyQt5 import uic
from src.fs_utils import FsUtils

class BookMove(QDialog):
    
    def __init__(self, parent, active_book):
        super().__init__(parent)
        uic.loadUi(FsUtils.get_resource("/ui/bookmove.ui"), self)
        self.accepted.connect(self.moveBook)
        self.bookSelected = None
        self.book_id = None
        self.batch_id = None
        self.active_book = active_book

        batches = FsUtils.get_batches()
        if batches is not None:
            batches.append("New Batch")
            self.batchesList.addItems(batches)

        self.batchesList.itemClicked.connect(self.showBooks)
        self.booksList.itemClicked.connect(self.loadBook)

    def loadBook(self, item):
        """
        show the book entries
        """
        self.book_id = item.text()
        self.bookSelected = FsUtils.get_book(self.book_id, self.batch_id)
        self.labelBox.setText(self.bookSelected.box)
        self.labelBookType.setText(self.bookSelected.booktype.getDisplayText())
        self.labelCoverMaterial.setText(self.bookSelected.coverMaterial)

    def showBooks(self, item) :

        if item.text() == "New Batch":
            self.batch_id: int = FsUtils.get_new_batch_id()
        else:
            self.batch_id : int = item.text()
        while self.booksList.count() > 0:
            self.booksList.takeItem(0)
        books = [n.replace(".json", "") for n in FsUtils.get_books_in_batch(self.batch_id)]

        self.booksList.addItems(books)

    def moveBook(self):
        if self.batch_id is not None:
            FsUtils.move_book(self.active_book, self.batch_id)
            self.close()