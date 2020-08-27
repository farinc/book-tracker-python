import os
from src.BookEntry import BookEntry
class FsUtils:
    @classmethod
    def getBatches(cls) -> list:
        batches = []
        for b in os.listdir("./Books"):
            if os.path.isdir("./Books/" +b):
                batches.append(b)
        return batches

    @classmethod
    def getBooksInBatch(cls, batchID: int) -> list:
        p = "./Books/{batch_id}/".format(batch_id=batchID)
        books = []
        for e in os.listdir(p):
            if os.path.isfile(p+"/"+e):
                books.append(e)
        return books

    @classmethod
    def createBatch(cls, batchID):
        os.mkdir("./Books/{batch_id}/".format(batch_id=batchID))

    @classmethod
    def createBook(cls, book_entry : BookEntry):
        if(not os.path.exists("./Books/{id}/".format(id=book_entry.batchID))):
            cls.createBatch(book_entry.batchID)
        with open("./Books/{batchID}/{bookID}.json".format(batchID=book_entry.batchID, bookID=book_entry.bookID), 'w') as fp:
            book_entry.saveToJSONFile(fp)
    @classmethod
    def getBook(cls, batch_id, book_id) -> BookEntry:
        book_entry = BookEntry()
        with open("./Books/{batchID}/{bookID}.json".format(batchID=batch_id, bookID=book_id), 'r') as fp:
            book_entry.loadFromJSONFile(fp)
            return book_entry