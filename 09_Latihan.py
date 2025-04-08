# File: 09_Latihan.py
# Author: Reza Chairul Manam
# NIM: 120140086
# Class: PBO-RC
# ===================================================================================================
# Latihan 1

from abc import ABC, abstractmethod

# --- Abstract Base Class ---
class LibraryItem(ABC):
    def __init__(self, title: str, item_id: str):
        self.__title = title  # Private attribute
        self.__item_id = item_id  # Private attribute
        self.checked_out = False

    @property # getter untuk title fungsi untuk mendapatkan title
    def title(self): 
        return self.__title

    @property
    def item_id(self):
        return self.__item_id

    @abstractmethod
    def check_out(self):  # Abstract method for checkout
        pass

    @abstractmethod
    def return_item(self):
        pass

    def __str__(self) -> str:  # String representation
        return f"{self.__class__.__name__}: {self.title} (ID: {self.item_id})"

# --- Book Subclass ---
class Book(LibraryItem):
    def __init__(self, title: str, item_id: str, author: str):
        LibraryItem(self, title, item_id) 
        self.__author = author  # Private attribute

    @property
    def author(self):
        return self.__author

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"Book '{self.title}' checked out.")
        else:
            print("Book already checked out.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"Book '{self.title}' returned.")

# --- DVD Subclass ---
class DVD(LibraryItem):
    def __init__(self, title: str, item_id: str, duration: int):
        super().__init__(title, item_id)
        self.__duration = duration  # Private attribute

    def check_out(self):
        if not self.checked_out:
            print(f"DVD '{self.title}' checked out for {self.__duration} minutes.")
            self.checked_out = True
        else:
            print("DVD already checked out.")

    def __str__(self):
        return f"DVD: {self.title} (Duration: {self.__duration} mins)"

# --- Library Class (Composition) ---
class Library:
    def __init__(self):
        self.items = []  # List of LibraryItem objects

    def add_item(self, item: LibraryItem):
        self.items.append(item)
        print(f"Added {item.title} to the library.")

    def search_by_title(self, title: str) -> list:
        return [item for item in self.items if title.lower() in item.title.lower()]

    def total_items(self) -> int:  # Total items in library
        return len(self.items)

    def __add__(self, other: 'Library') -> 'Library':
        new_library = Library()
        new_library.items = self.items + other.items
        return new_library

# --- Test Code ---
if __name__ == "__main__":
    book1 = Book("The Python Guide", "BK001", "Alice Smith")
    dvd1 = DVD("Learn OOP in 30 Days", "DVD001", 120)

    library = Library()
    library.add_item(book1)
    library.add_item(dvd1)

    book1.check_out()
    dvd1.check_out()
    dvd1.__str__()

    print(f"Total items: {library.total_items()}")