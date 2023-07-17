
from datetime import datetime, timedelta

from config import Envs
from jwt import encode


class CreateTokenService:
    def __init__(self, envs: Envs):
        self.envs = envs

    def execute(self, body: any) -> str:
        if (body['user'] == self.envs.APP_USER and body['password'] == self.envs.APP_PASSWORD):
            return {
                'token': encode({'user': body['user'], 'exp': (datetime.utcnow()+timedelta(hours=1))}, self.envs.APP_SECRET)
            }, 201
        return {'message': 'Invalid credentials'}, 401
