from sqlalchemy import *
from sqlalchemy.orm import *

from .base import Base
from .book_to_subject import book_subjects


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    author = Column(String(255))
    author_id = Column(Integer, ForeignKey('authors.id'))
    author_bio = Column(Text)
    authors = Column(String(255))
    title_slug = Column(String(255))
    author_slug = Column(String(255))
    isbn13 = Column(String(13))
    isbn10 = Column(String(10))
    price = Column(String(10))
    format = Column(String(50))
    publisher = Column(String(255))
    pubdate = Column(String(50))
    edition = Column(String(50))
    lexile = Column(String(50))
    pages = Column(Integer)
    dimensions = Column(String(50))
    overview = Column(Text)
    excerpt = Column(Text)
    synopsis = Column(Text)
    toc = Column(Text)
    editorial_reviews = Column(Text)

    author_rel = relationship('Author', backref='books')
    subjects = relationship(
        'Subject', secondary=book_subjects, backref='books')

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'author_id': self.author_id,
            'author_bio': self.author_bio,
            'authors': self.authors,
            'title_slug': self.title_slug,
            'author_slug': self.author_slug,
            'isbn13': self.isbn13,
            'isbn10': self.isbn10,
            'price': self.price,
            'format': self.format,
            'publisher': self.publisher,
            'pubdate': self.pubdate,
            'edition': self.edition,
            'lexile': self.lexile,
            'pages': self.pages,
            'dimensions': self.dimensions,
            'overview': self.overview,
            'excerpt': self.excerpt,
            'synopsis': self.synopsis,
            'toc': self.toc,
            'editorial_reviews': self.editorial_reviews,
            'subjects': [item.to_json() for item in self.subjects],
            'author_rel': self.author_rel and self.author_rel.to_json()
        }

    @staticmethod
    def generate(**kwargs):
        book = Book()
        book.id = kwargs.get('id')
        book.title = kwargs.get('title')
        book.author = kwargs.get('author')
        book.author_id = kwargs.get('author_id')
        book.author_bio = kwargs.get('author_bio')
        book.authors = kwargs.get('authors')
        book.title_slug = kwargs.get('title_slug')
        book.author_slug = kwargs.get('author_slug')
        book.isbn13 = kwargs.get('isbn13')
        book.isbn10 = kwargs.get('isbn10')
        book.price = kwargs.get('price')
        book.format = kwargs.get('format')
        book.publisher = kwargs.get('publisher')
        book.pubdate = kwargs.get('pubdate')
        book.edition = kwargs.get('edition')
        book.lexile = kwargs.get('lexile')
        book.pages = int(kwargs.get('pages')) if isinstance(
            kwargs.get('pages'), (int, float)) else 0
        book.dimensions = kwargs.get('dimensions')
        book.overview = kwargs.get('overview')
        book.excerpt = kwargs.get('excerpt')
        book.synopsis = kwargs.get('synopsis')
        book.toc = kwargs.get('toc')
        book.editorial_reviews = kwargs.get('editorial_reviews')
        return book
