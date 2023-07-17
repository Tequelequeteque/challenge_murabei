from config import Envs

from .author_repository import AuthorRepository
from .book_repository import BookRepository
from .database import Database
from .subject_repository import SubjectRepository


class Repositories:
    """Repositories class."""

    def __init__(self, envs: Envs):
        self.db = Database.create(envs)
        self.author_repository = AuthorRepository(self.db)
        self.book_repository = BookRepository(self.db)
        self.subject_repository = SubjectRepository(self.db)

    @staticmethod
    def create(envs: Envs) -> 'Repositories':
        """Create a new repositories."""
        return Repositories(envs)
