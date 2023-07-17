
from repositories import BookRepository


class ListAllBooksService:
    """List all books service class."""

    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self, page=1, limit=10) -> list[dict]:
        """Get all books."""
        return [item.to_json() for item in self.book_repository.list_all(page=page, limit=limit)]
