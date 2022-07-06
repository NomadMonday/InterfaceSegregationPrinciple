from abc import ABC

class ABCLibraryItem(ABC):
    def __init__(self):
        self.library_id: str = None
        self.title: str = None
