from config import Envs
from repositories import Repositories

from .auth_services import AuthServices
from .author_services import AuthorServices
from .book_services import BookServices
from .subject_services import SubjectServices


class Services:
    auth_services: AuthServices

    def __init__(self, envs: Envs, repositories: Repositories):
        self.auth_services = AuthServices(envs)
        self.author_services = AuthorServices(repositories)
        self.book_services = BookServices(repositories)
        self.subject_services = SubjectServices(repositories)

    @staticmethod
    def create(envs: Envs, repositories: Repositories) -> 'Services':
        return Services(envs, repositories)
