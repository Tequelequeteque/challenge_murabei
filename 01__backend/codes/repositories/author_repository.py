from models import Author

from .database import Database


class AuthorRepository:
    """Author repository class."""

    def __init__(self, db: Database):
        self.db = db

    def list_all(self, page=1, limit=10, title='') -> list[Author]:
        """List all authors."""
        return self.db.session.query(Author).filter(Author.title.ilike(f"%{title.lower()}%")).limit(limit).offset((page - 1) * limit).all()
