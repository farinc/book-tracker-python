import os
import math
import sys
import logging
import json
from src.book_entry import BookEntry

class FsUtils:

    base_path = os.path.abspath(".")
    book_path = os.path.abspath("./Books")

    @classmethod
    def get_base_dir(cls) -> str:
        if not os.path.isdir(cls.base_path):
            os.mkdir(cls.base_path)
        return cls.base_path

    @classmethod
    def set_books_dir(cls, path):
        cls.book_path = path

    @classmethod
    def get_book_dir(cls) -> str:
        if not os.path.isdir(cls.book_path):
            os.mkdir(cls.book_path)
        return cls.book_path

    @classmethod
    def get_resource(cls, path):
        return cls.base_path + "/" + path

    @classmethod
    def get_batches(cls) -> list:
        batches = []
        p = cls.get_book_dir()

        if os.path.isdir(p):
            for b in os.listdir(p):
                if os.path.isdir(p+"/"+b):
                    batches.append(b)
            return batches

    @classmethod
    def get_batch(cls, batch_id):
        p = cls.get_book_dir() + "/{batch_id}".format(batch_id=str(batch_id))
        if not os.path.isdir(p):
            os.mkdir(p)
        return p

    @classmethod
    def get_books_in_batch(cls, batch_id: int) -> list:
        p = cls.get_batch(batch_id)
        books = []
        for e in os.listdir(p):
            books.append(e)
        
        return books

    @classmethod
    def load_settings(cls):
        js = None
        if os.path.isfile("settings.json"):
            with open("settings.json", 'r') as fp:
                js = json.load(fp)
            
                if js is not None:
                    f = js["books_path"]
                    cls.set_books_dir(f)

    @classmethod
    def save_settings(cls):
        settings = FsUtils.get_resource("settings.json")
        with open(settings, 'w') as fp:
            json.dump({"books_path": FsUtils.book_path}, fp)

    @classmethod
    def get_book_file(cls, book_id: int, batch_id: int):
        return cls.get_batch(batch_id) + "/" + str(book_id) + ".json"            

    @classmethod
    def move_book(cls, book_entry: BookEntry, new_batch: int):
        os.remove(cls.get_book_file(book_entry.bookID, book_entry.batchID))
        book_entry.batchID = new_batch
        cls.save_book(book_entry)

    @classmethod
    def save_book(cls, book_entry : BookEntry):
        with open(cls.get_book_file(book_entry.bookID, book_entry.batchID), 'w') as fp:
            book_entry.saveToJSONFile(fp)
            
    @classmethod
    def get_book(cls, book_id, batch_id) -> BookEntry:
        book_entry = BookEntry(book_id, batch_id)
        with open(cls.get_book_file(book_id, batch_id), 'r') as fp:
            book_entry.loadFromJSONFile(fp)
            return book_entry

    @classmethod
    def create_book_current_batch(cls) -> BookEntry:
        book_entry = BookEntry(cls.get_new_book_id(),cls.get_current_batch())
        cls.save_book(book_entry)
        return book_entry

    @classmethod
    def create_book_new_batch(cls) -> BookEntry:
        book_entry = BookEntry(cls.get_new_book_id(), cls.get_new_batch_id())
        cls.save_book(book_entry)
        return book_entry

    @classmethod
    def get_current_batch(cls) -> int:
        batches = cls.get_batches()
        if batches is not None:
            batchIDs = [int(b) for b in batches]
            if len(batchIDs) > 0:
                return max(batchIDs)
        return 0

    @classmethod
    def get_new_batch_id(cls):
        return cls.get_current_batch() + 1

    @classmethod
    def get_new_book_id(cls) -> int:
        batchs = cls.get_batches()
        if batchs is not None:
            batchIDs = [int(b) for b in batchs] #get batchIDs
            bookIDs = []
            for batchID in batchIDs: #Get books for a given batch
                books_in_batch = cls.get_books_in_batch(batchID)
                bookIDs.extend([int(b.replace(".json", "")) for b in books_in_batch]) #Add to bookIDs to the total
            if len(bookIDs) > 0: 
                return max(bookIDs) + 1 #From the total list of books, get the max value

        return 0