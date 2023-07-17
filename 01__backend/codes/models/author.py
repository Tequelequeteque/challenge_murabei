from sqlalchemy import *
from sqlalchemy.orm import *

from .base import Base


class Author(Base):
    """Author model class."""
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30))
    slug = Column(String(255))
    biography = Column(Text)

    def to_json(self) -> dict:
        """Converts the object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'biography': self.biography
        }

    @staticmethod
    def generate(**kwargs) -> 'Author':
        """Generate a new author."""
        author = Author()
        author.id = kwargs['id']
        author.title = kwargs['title']
        author.slug = kwargs['slug']
        author.biography = kwargs['biography']
        return author
