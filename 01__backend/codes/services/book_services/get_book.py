from repositories import BookRepository


class GetBookService:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self, book_id: str) -> tuple[dict, int] or dict:
        has_book = self.book_repository.get(book_id)
        if has_book:
            return has_book.to_json(), 200
        else:
            return {'message': 'Book not found'}, 404
