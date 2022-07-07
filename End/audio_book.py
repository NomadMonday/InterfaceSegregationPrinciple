from abc_borrowable_audio_book import ABCBorrowableAudioBook
import datetime

class AudioBook(ABCBorrowableAudioBook):
    def __init__(self):
        super().__init__()
        self.pages = -1
        self.checkout_duration_in_days = 14
        self.runtime_in_minutes: int = None
    
    def check_out(self, borrower: str) -> None:
        self.borrower = borrower
        self.borrow_date = datetime.now()

    def check_in(self) -> None:
        self.borrower = ""

    def get_due_date(self) -> datetime:
        return self.borrow_date + datetime.timedelta(days=self.checkout_duration_in_days)
