from repositories import AuthorRepository


class ListAllAuthorsService:
    """List all authors service class."""

    def __init__(self, author_repository: AuthorRepository):
        self.author_repository = author_repository

    def execute(self, page=1, limit=10) -> list[dict]:
        """Get all authors."""
        return [item.to_json() for item in self.author_repository.list_all(page=page, limit=limit)]
