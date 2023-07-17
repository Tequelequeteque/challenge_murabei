from models import Subject

from .database import Database


class SubjectRepository:
    def __init__(self, db: Database):
        self.db = db

    def list_all(self, page=1, limit=10) -> list[Subject]:
        """List all subjects."""
        return self.db.session.query(Subject).offset((page - 1) * limit).limit(limit).all()
