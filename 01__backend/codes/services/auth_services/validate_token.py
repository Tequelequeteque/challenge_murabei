from config import Envs
from jwt import decode


class ValidateTokenService:
    def __init__(self, envs: Envs):
        self.envs = envs

    def execute(self, authorization: str) -> bool:
        token = authorization.replace('Bearer ', '')
        try:
            decode(token, self.envs.APP_SECRET, algorithms=['HS256'])
            return True
        except Exception as e:
            return False
