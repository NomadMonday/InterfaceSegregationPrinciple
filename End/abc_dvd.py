from abc_library_item import ABCLibraryItem

class ABC_DVD(ABCLibraryItem):
    def __init__(self):
        self.actors: list = None
        self.run_time_in_minutes: int = None
