from flask_restful import Resource, request
from services import AuthServices, SubjectServices


class SubjectController(Resource):
    """Subject controller"""

    def __init__(self, auth_services: AuthServices, subject_services: SubjectServices):
        self.auth_services = auth_services
        self.subject_services = subject_services
        super().__init__()

    def get(self):
        """Get All Authors"""
        authorization = request.headers.get('Authorization')
        page = request.args.get('page', 1, type=int)
        limit = request.args.get('limit', 10, type=int)
        if (self.auth_services.validate_token.execute(authorization)):
            return self.subject_services.list_all_subject.execute(
                page=1 if page < 1 else page,
                limit=10 if limit < 1 else limit
            )
        else:
            return {'message': 'Invalid token'}, 401
