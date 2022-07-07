from abc_library_item import ABCLibraryItem

class ABCAudioBook(ABCLibraryItem):
    def __init__(self):
        super().__init__()
        self.run_time_in_minutes: int = None
        