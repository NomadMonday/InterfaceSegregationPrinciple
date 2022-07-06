from abc_book import ABCBook
from abc_borrowable import ABCBorrowable

class ABCBorrowableBook(ABCBook, ABCBorrowable):
    def __init__(self):
        super().__init__()
