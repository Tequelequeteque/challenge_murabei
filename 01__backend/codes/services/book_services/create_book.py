from models import Book
from repositories import BookRepository


class CreateBookService:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self, dict: dict) -> dict or tuple[dict, int]:
        """Create a new book"""
        book = Book.generate(**dict)
        try:
            self.book_repository.save(book)
        except Exception as error:
            return {'message': 'Bad Request', 'cause': error.__cause__}, 400
        return book.to_json()
