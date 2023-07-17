
from flask_restful import Resource, request
from services import AuthServices


class AuthController(Resource):
    """Auth controller"""

    def __init__(self, auth_services: AuthServices):
        self.auth_services = auth_services
        super().__init__()

    def post(self):
        """Create a token"""
        body = request.get_json()
        return self.auth_services.create_token.execute(body)
