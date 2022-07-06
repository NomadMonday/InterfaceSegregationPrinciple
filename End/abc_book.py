from abc_library_item import ABCLibraryItem

class ABCBook(ABCLibraryItem):
    def __init__(self):
        super().__init__()
        self.author: str = None
        self.pages: int = None
