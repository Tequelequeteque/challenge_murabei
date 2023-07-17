from models import Book
from repositories import BookRepository


class UpdateBookService:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self, **kwargs) -> dict or tuple(dict, int):
        book = Book.generate(**kwargs)
        hasBook = self.book_repository.get(book.id)
        if hasBook:
            self.book_repository.update(book)
            return book.to_json()
        else:
            return {'message': 'Book not found'}, 404
