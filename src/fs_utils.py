import os
import math
from src.book_entry import BookEntry

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
    def _createBatch(cls, batchID):
        os.mkdir("./Books/{batch_id}/".format(batch_id=batchID))

    @classmethod
    def _createNewBatch(cls) -> int:
        id = cls._getNewBatchID()
        cls._createBatch(id)
        return id

    @classmethod
    def saveBook(cls, book_entry : BookEntry):
        if(not os.path.exists("./Books/{id}/".format(id=book_entry.batchID))):
            cls._createBatch(book_entry.batchID)
        with open("./Books/{batchID}/{bookID}.json".format(batchID=book_entry.batchID, bookID=book_entry.bookID), 'w') as fp:
            book_entry.saveToJSONFile(fp)
            
    @classmethod
    def getBook(cls, batch_id, book_id) -> BookEntry:
        book_entry = BookEntry(book_id, batch_id)
        with open("./Books/{batchID}/{bookID}.json".format(batchID=batch_id, bookID=book_id), 'r') as fp:
            book_entry.loadFromJSONFile(fp)
            return book_entry

    @classmethod
    def createBookCurrentBatch(cls) -> BookEntry:
        book_entry = BookEntry(cls._getNewBookID(), cls.getCurrentBatch())
        cls.saveBook(book_entry)
        return book_entry

    @classmethod
    def createBookNewBatch(cls) -> BookEntry:
        book_entry = BookEntry(cls._getNewBookID(), cls._createNewBatch())
        cls.saveBook(book_entry)
        return book_entry

    @classmethod
    def getCurrentBatch(cls) -> int:
        batches = cls.getBatches()
        batchIDs = [int(b) for b in batches]
        return max(batchIDs)

    @classmethod
    def _getNewBatchID(cls):
        return cls.getCurrentBatch() + 1

    @classmethod
    def _getNewBookID(cls) -> int:
        batchs = cls.getBatches()
        batchIDs = [int(b) for b in batchs] #get batchIDs
        bookIDs = []
        for batchID in batchIDs: #Get books for a given batch
            books_in_batch = cls.getBooksInBatch(batchID)
            bookIDs.extend([int(b.replace(".json", "")) for b in books_in_batch]) #Add to bookIDs to the total
        newID = max(bookIDs) + 1 #From the total list of books, get the max value
        return newID
