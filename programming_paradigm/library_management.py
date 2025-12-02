class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
            return True
        return False

    def _find_book_by_title(self, title):
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        book = self._find_book_by_title(title)
        if book is None:
            return False
        return book.check_out()

    def return_book(self, title):
        book = self._find_book_by_title(title)
        if book is None:
            return False
        return book.return_book()

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
