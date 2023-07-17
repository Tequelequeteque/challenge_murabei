
from os import getenv

from dotenv import load_dotenv


class Envs:
    """Envs class."""
    @staticmethod
    def create(path='.env') -> 'Envs':
        """Create a new envs."""
        return Envs(path)

    def __init__(self, path):
        load_dotenv(dotenv_path=path)

    @property
    def APP_PORT(self) -> int:
        """Get the app port."""
        return int(getenv('APP_PORT', 8000))

    @property
    def APP_USER(self) -> str:
        """Get the app user."""
        return getenv('APP_USER', 'admin')

    @property
    def APP_PASSWORD(self) -> str:
        """Get the app password."""
        return getenv('APP_PASSWORD', 'admin')

    @property
    def APP_SECRET(self) -> str:
        """Get the app secret."""
        return getenv('APP_SECRET', 'secret')

    @property
    def DB_HOST(self) -> str:
        """Get the db host."""
        return getenv('DB_HOST', 'localhost')

    @property
    def DB_PORT(self) -> int:
        """Get the db port."""
        return int(getenv('DB_PORT', 5432))

    @property
    def DB_USER(self) -> str:
        """Get the db user."""
        return getenv('DB_USER', 'postgres')

    @property
    def DB_PASSWORD(self) -> str:
        """Get the db password."""
        return getenv('DB_PASSWORD', 'postgres')

    @property
    def DB_NAME(self) -> str:
        """Get the db name."""
        return getenv('DB_NAME', 'postgres')
