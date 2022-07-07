from abc_borrowable import ABCBorrowable
from abc_dvd import ABC_DVD

class ABCBorrowableDVD(ABCBorrowable, ABC_DVD):
    def __init__(self):
        super().__init__()
