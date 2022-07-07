from abc_audio_book import ABCAudioBook
from abc_borrowable import ABCBorrowable

class ABCBorrowableAudioBook(ABCAudioBook, ABCBorrowable):
    def __init__(self):
        super().__init__()
