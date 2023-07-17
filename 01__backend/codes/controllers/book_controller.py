from flask_restful import Resource, request
from services import AuthServices, BookServices


class BookController(Resource):
    """Book controller"""

    def __init__(self, auth_services: AuthServices, book_services: BookServices):
        self.auth_services = auth_services
        self.book_services = book_services
        super().__init__()

    def get(self):
        """Get All Books"""
        authorization = request.headers.get('Authorization')
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', 10, type=int)
        if (self.auth_services.validate_token.execute(authorization)):
            return self.book_services.list_all_book.execute(
                page=1 if page < 1 else page,
                limit=10 if limit < 1 else limit
            )
        else:
            return {'message': 'Invalid token'}, 401

    def post(self):
        """Create a Book"""
        authorization = request.headers.get('Authorization')
        if (self.auth_services.validate_token.execute(authorization)):
            return self.book_services.create_book.execute(request.json)
        else:
            return {'message': 'Invalid token'}, 401

    def put(self, book_id):
        """Update a Book"""
        authorization = request.headers.get('Authorization')
        if (self.auth_services.validate_token.execute(authorization)):
            return self.book_services.update_book.execute(id=book_id, **request.json)
        else:
            return {'message': 'Invalid token'}, 401

    def delete(self, book_id):
        """Delete a Book"""
        authorization = request.headers.get('Authorization')
        if (self.auth_services.validate_token.execute(authorization)):
            return self.book_services.delete_book.execute(id=book_id)
        else:
            return {'message': 'Invalid token'}, 401
