from config import Envs

from .create_token import CreateTokenService
from .validate_token import ValidateTokenService


class AuthServices:
    create_token: CreateTokenService
    validate_token: ValidateTokenService

    def __init__(self, envs: Envs):
        self.create_token = CreateTokenService(envs)
        self.validate_token = ValidateTokenService(envs)
