import csv
from typing import TypeVar
from urllib.parse import quote

from config import Envs
from models import *
from sqlalchemy import Engine, create_engine, text
from sqlalchemy.orm import Session

T = TypeVar('T', Author, Book, Subject)


class Database:
    """Database class."""
    engine: Engine
    session: Session
    base: Base

    def __init__(self, envs: Envs):
        db_uri = "postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB_NAME}".format(
            USER=quote(envs.DB_USER),
            PASS=quote(envs.DB_PASSWORD),
            HOST=quote(envs.DB_HOST),
            PORT=envs.DB_PORT,
            DB_NAME=quote(envs.DB_NAME)
        )
        self.engine = create_engine(db_uri)
        self.session = Session(self.engine)
        self.base = Base()
        self._migrations()

    def _migrations(self):
        """Migrations."""
        self.base.metadata.create_all(self.engine)
        self._insert_data(Author, '../00__database/files/author.csv')
        self._insert_data(Book, '../00__database/files/book.csv')
        self._insert_data(Subject, '../00__database/files/subject.csv')
        self._insert_relation_book_to_subject(
            '../00__database/files/book2subjects.csv')

    def _insert_relation_book_to_subject(self, path) -> None:
        """Insert relation between book and subject."""
        with open(path, 'r') as f:
            data = ['INSERT INTO {table} (book_id, subject_id) VALUES ({book}, {sub_sub_subject});'.format(
                table='book_subjects', **row) for row in csv.DictReader(f)]
            try:
                self.session.execute(
                    text("SET session_replication_role = 'replica';")
                )
                self.session.execute(text('\n'.join(data)))
                self.session.commit()
            except Exception as e:
                self.session.rollback()
            finally:
                self.session.execute(
                    text("SET session_replication_role = DEFAULT;")
                )
                self.session.commit()

    def _insert_data(self, t: T, path) -> None:
        """Insert data."""
        with open(path, 'r') as f:
            data = [t.generate(**row) for row in csv.DictReader(f)]
            try:
                self.session.execute(
                    text("SET session_replication_role = 'replica';")
                )
                self.session.add_all(data)
                self.session.commit()
            except Exception as e:
                self.session.rollback()
            finally:
                self.session.execute(text('ALTER SEQUENCE {table}_id_seq RESTART WITH {id};'.format(
                    table=t.__tablename__, id=len(data) + 1)))
                self.session.execute(
                    text("SET session_replication_role = DEFAULT;")
                )
                self.session.commit()

    @staticmethod
    def create(envs: Envs) -> 'Database':
        return Database(envs)
