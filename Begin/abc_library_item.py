from abc import ABC, abstractmethod
from datetime import datetime

class ABCLibraryItem(ABC):
    def __init__(self):
        self.author: str = None
        self.borrow_date: datetime = None
        self.borrower: str = None
        self.checkout_duration_in_days: int = None
        self.library_id: str = None
        self.pages: int = None
        self.title: str = None
    
    @abstractmethod
    def check_in(self) -> None:
        pass

    @abstractmethod
    def check_out(self, borrower: str) -> None:
        pass

    @abstractmethod
    def get_due_date(self) -> datetime:
        pass
