from config import Envs
from controllers import (AuthController, AuthorController, BookController,
                         SubjectController)
from flask import Flask
from flask_restful import Api
from services import Services


class Server:
    """Server class."""

    def __init__(self, name: str, envs: Envs, services: Services):
        self.app = Flask(name)
        self.api = Api(self.app)
        self.envs = envs
        self.services = services

        self.app.register_error_handler(Exception, self.handle_exception)

    def load_routes(self) -> None:
        """Load all routes here."""
        self.api.add_resource(
            AuthController, '/auth', resource_class_kwargs={'auth_services': self.services.auth_services}
        )
        self.api.add_resource(
            AuthorController, '/authors', resource_class_kwargs={
                'auth_services': self.services.auth_services,
                'author_services': self.services.author_services
            }
        )
        self.api.add_resource(
            BookController, '/books', resource_class_kwargs={
                'auth_services': self.services.auth_services,
                'book_services': self.services.book_services
            }, endpoint='books'
        )
        self.api.add_resource(
            BookController, '/books/<int:book_id>', resource_class_kwargs={
                'auth_services': self.services.auth_services,
                'book_services': self.services.book_services
            }, endpoint='book'
        )
        self.api.add_resource(
            SubjectController, '/subjects', resource_class_kwargs={
                'auth_services': self.services.auth_services,
                'subject_services': self.services.subject_services
            }
        )

    def run(self) -> None:
        """Run the server."""
        self.app.run(debug=True, port=self.envs.APP_PORT)

    @staticmethod
    def create(name: str, envs: Envs,  services: Services) -> 'Server':
        """Create a new server."""
        return Server(name, envs=envs, services=services)

    def handle_exception(self, error: Exception):
        """Handle exception."""
        print(error)
        return {"message": "Internal server error", }, 500
