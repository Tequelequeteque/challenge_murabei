from sqlalchemy import Column, ForeignKey, Integer, Table

from .base import Base

book_subjects = Table(
    'book_subjects',
    Base.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('subject_id', Integer, ForeignKey('subjects.id'))
)
