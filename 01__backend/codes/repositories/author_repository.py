from models import Author

from .database import Database


class AuthorRepository:
    """Author repository class."""

    def __init__(self, db: Database):
        self.db = db

    def list_all(self, page=1, limit=10) -> list[Author]:
        """List all authors."""
        return self.db.session.query(Author).limit(limit).offset((page - 1) * limit).all()
