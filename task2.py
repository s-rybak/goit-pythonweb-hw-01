from abc import ABC, abstractmethod
from dataclasses import dataclass
import uuid
import logging

logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
)


@dataclass
class Book:
    """Book class"""

    id: str
    title: str
    author: str
    year: int


class LibraryInterface(ABC):
    """Library interface"""

    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, id: str):
        pass

    @abstractmethod
    def show_books(self):
        pass


class LibraryManager:
    """Library manager class"""

    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, book: Book):
        self.library.add_book(book)

    def remove_book(self, id: str):
        self.library.remove_book(id)

    def show_books(self):
        self.library.show_books()


class Library(LibraryInterface):
    def __init__(self):
        self.books = {}

    def add_book(self, book: Book):
        if book.id in self.books:
            logging.error("Book already exists")
            return
        self.books[book.id] = book

    def remove_book(self, id: str):
        if id not in self.books:
            logging.error("Book not found")
            return
        del self.books[id]

    def show_books(self):
        for book in self.books.values():
            logging.info(
                f"Title: {book.title}, Author: {book.author}, Year: {book.year} (ID: {book.id})"
            )


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                id = str(uuid.uuid4())
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(Book(id, title, author, year))
            case "remove":
                id = input("Enter book id to remove: ").strip()
                manager.remove_book(id)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logging.error("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
