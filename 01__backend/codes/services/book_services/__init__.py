from repositories import Repositories

from .create_book import CreateBookService
from .delete_book import DeleteBookService
from .get_book import GetBookService
from .list_all_book import ListAllBooksService
from .update_book import UpdateBookService


class BookServices:
    def __init__(self, repositories: Repositories):
        self.list_all_book = ListAllBooksService(
            repositories.book_repository
        )
        self.create_book = CreateBookService(
            repositories.book_repository
        )
        self.update_book = UpdateBookService(
            repositories.book_repository
        )
        self.delete_book = DeleteBookService(
            repositories.book_repository
        )
        self.get_book = GetBookService(
            repositories.book_repository
        )
