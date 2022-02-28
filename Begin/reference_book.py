from abc_library_item import ABCLibraryItem
import datetime

class ReferenceBook(ABCLibraryItem):
    def __init__(self):
        super().__init__()
        self.checkout_duration_in_days = 0

    def check_out(self, borrower: str) -> None:
        raise NotImplementedError

    def check_in(self) -> None:
        raise NotImplementedError

    def get_due_date(self) -> datetime:
        raise NotImplementedError
