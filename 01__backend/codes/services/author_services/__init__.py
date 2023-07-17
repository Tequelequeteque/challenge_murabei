from repositories import Repositories

from .list_all_author import ListAllAuthorsService


class AuthorServices:
    """Author services class."""

    def __init__(self, repositories: Repositories):
        self.list_all_author = ListAllAuthorsService(
            repositories.author_repository
        )
