from repositories import SubjectRepository


class ListAllSubjectService:
    def __init__(self, subject_repository: SubjectRepository):
        self.subject_repository = subject_repository

    def execute(self, page=1, limit=10):
        """List all subjects."""
        return [item.to_json() for item in self.subject_repository.list_all(page, limit)]
