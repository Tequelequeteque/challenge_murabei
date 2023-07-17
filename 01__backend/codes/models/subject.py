from sqlalchemy import *
from sqlalchemy.orm import *

from .base import Base


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    slug = Column(String(255))

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug
        }

    @staticmethod
    def generate(**kwargs):
        subject = Subject()
        subject.id = kwargs['id']
        subject.title = kwargs['title']
        subject.slug = kwargs['slug']
        return subject
