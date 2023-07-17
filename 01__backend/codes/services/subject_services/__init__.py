from repositories import Repositories

from .list_all_subject import ListAllSubjectService


class SubjectServices:
    """Subject services."""

    def __init__(self, repositories: Repositories):
        self.list_all_subject = ListAllSubjectService(
            repositories.subject_repository
        )
