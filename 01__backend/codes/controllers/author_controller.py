from flask_restful import Resource, request
from services import AuthorServices, AuthServices


class AuthorController(Resource):
    """Author controller"""

    def __init__(self, auth_services: AuthServices, author_services: AuthorServices):
        self.auth_services = auth_services
        self.author_services = author_services
        super().__init__()

    def get(self):
        """Get All Authors"""
        authorization = request.headers.get('Authorization')
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', 10, type=int)
        if (self.auth_services.validate_token.execute(authorization)):
            return self.author_services.list_all_author.execute(
                page=1 if page < 1 else page,
                limit=10 if limit < 10 else limit
            ), 200
        else:
            return {'message': 'Invalid token'}, 401
