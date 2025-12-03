# library_system.py

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def info(self) -> str:
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)      # call Book.__init__
        self.file_size = file_size

    def info(self) -> str:
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)      # call Book.__init__
        self.page_count = page_count

    def info(self) -> str:
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []  # composition: Library has a list of Book objects

    def add_book(self, book: Book):
        # simple check to ensure we add Book or subclass
        if not isinstance(book, Book):
            raise TypeError("Only Book or its subclasses can be added")
        self.books.append(book)

    def list_books(self):
        for b in self.books:
            print(b.info())
