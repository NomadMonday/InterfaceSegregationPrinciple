## Summary
- I created this project as a demonstration of the Interface Segregation Principle (the I in SOLID).
- It is a recreation of this demonstration by Tim Corey, except rewritten in Python: https://youtu.be/y1JiMGP51NE
- I wanted to create a semi-guided exercise where the objective is known, but the exact solution is not due to language differences. In this way, I could create a more challenging and engaging problem to solve, while also learning how to apply SOLID principles in Python.
- The Begin folder contains the starting point of the code before the principle is applied, and the End folder contains the refactored code after.

## Notes
#### The Python standard library does not use interfaces.
- As we learned in the [Open Closed Principle](https://github.com/NomadMonday/OpenClosedPrinciple) project, abstract base classes must be used instead of interfaces.
- One drawback of using multiple inheritance instead of interfaces is that it reduces readability. The inheritance structure adds extra layers, burying some items in a parent multiple levels away.
- For example, the Book class constructor looks like this:
```Python
class Book(ABCBorrowableBook):
    def __init__(self):
        super().__init__()
        self.checkout_duration_in_days = 14
```
- However, the additional attributes aren't immediately apparent, since they are in parent classes multiple levels away:
```Python
class ABCBorrowableBook(ABCBook, ABCBorrowable):
    def __init__(self):
        super().__init__()

class ABCBook(ABCLibraryItem):
    def __init__(self):
        super().__init__()
        self.author: str = None
        self.pages: int = None

class ABCBorrowable(ABC):
    def __init__(self):
        self.borrow_date: datetime = None
        self.borrower: str = None
        self.checkout_duration_in_days: int = None

class ABCLibraryItem(ABC):
    def __init__(self):
        self.library_id: str = None
        self.title: str = None
```
