from models import Book

from .database import Database


class BookRepository:
    """Book repository class."""

    def __init__(self, db: Database):
        self.db = db

    def list_all(self, page=1, limit=10) -> list[Book]:
        """List all books."""
        return self.db.session.query(Book).offset((page - 1) * limit).limit(limit).all()

    def get(self, book_id: int) -> Book:
        """Get a book."""
        return self.db.session.query(Book).get(book_id)

    def save(self, book: Book) -> None:
        """Save a book."""
        try:
            self.db.session.add(book)
            self.db.session.commit()
        except Exception as error:
            self.db.session.rollback()
            raise error

    def update(self, book: Book) -> None:
        """Update a book."""
        try:
            self.db.session.merge(book)
            self.db.session.commit()
        except Exception as error:
            self.db.session.rollback()
            raise error

    def delete(self, book: Book) -> None:
        """Delete a book."""
        try:
            self.db.session.delete(book)
            self.db.session.commit()
        except Exception as error:
            self.db.session.rollback()
            raise error
