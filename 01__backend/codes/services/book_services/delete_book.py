from repositories import BookRepository


class DeleteBookService:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self, id: int) -> dict or tuple[dict, int]:
        """Delete a book"""
        hasBook = self.book_repository.get(id)
        if hasBook:
            self.book_repository.delete(hasBook)
            return {'message': 'Book deleted successfully'}, 200
        return {'message': 'Book not found'}, 404
