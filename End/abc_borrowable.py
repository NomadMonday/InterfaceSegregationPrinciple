from abc import ABC, abstractmethod
from datetime import datetime

class ABCBorrowable(ABC):
    def __init__(self):
        self.borrow_date: datetime = None
        self.borrower: str = None
        self.checkout_duration_in_days: int = None

    @abstractmethod
    def CheckIn(self) -> None:
        pass

    @abstractmethod
    def Checkout(self, borrower: str) -> None:
        pass

    @abstractmethod
    def GetDueDate(self) -> datetime:
        pass
