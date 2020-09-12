from PyQt5.QtWidgets import QDialog, QListWidgetItem
from PyQt5 import uic
from src.fs_utils import FsUtils
from src.book_entry import BookEntry
from src.book_type import BookType

class BookDiscription(QDialog):
    
    def __init__(self, parent, active_book: BookEntry):
        super().__init__(parent)
        uic.loadUi(FsUtils.get_resource("ui/discription.ui"), self)
        self.book_entry: BookEntry = active_book
        self.generateDiscription()

    def generateDiscription(self):
        
        spine_type = None
        if self.book_entry.booktype is BookType.TRADITIONAL or self.book_entry.booktype is BookType.LONG:
            spine_type = "Spine"
        elif self.book_entry.booktype is BookType.COPTIC or self.book_entry.booktype is BookType.COPTIC2NEEDLE:
            spine_type = "Thread"
        elif self.book_entry.booktype is BookType.STAB:
            spine_type = "Ribbon"

        self.discription.setPlainText(
        (
        "Cover: {covermaterial}\n"
        "{spine_type}: {spine_color}\n"
        "Paper: {paper_type}\n"
        "Inside covers: {end_page_color}\n"
        "\n"
        "Cover: {coverDimX} in. by {coverDimY} in. with\n"
        "Spine: {spine_dim} in.\n"
        "Page: {pageDimX} in. by {pageDimY} in.\n"
        "{pages} pages / {sides} sides").format(
            covermaterial = self.book_entry.coverMaterial,
            spine_type = spine_type,
            spine_color = self.book_entry.threadColor,
            paper_type = self.book_entry.pageMaterial,
            end_page_color = self.book_entry.endPageColor,
            coverDimX = str(self.book_entry.coverDim.width),
            coverDimY = str(self.book_entry.coverDim.height),
            spine_dim = str(self.book_entry.spine),
            pageDimX = str(self.book_entry.pageDim.width),
            pageDimY = str(self.book_entry.pageDim.height),
            pages = str(self.book_entry.calculatePaperCount()),
            sides = str(self.book_entry.calculatePaperCount() * 2)
        ))

    