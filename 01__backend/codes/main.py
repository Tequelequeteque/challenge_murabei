from config import Envs
from repositories import Repositories
from server import Server
from services import Services


def main():
    """Main function."""
    envs = Envs.create()
    repositories = Repositories.create(envs)
    services = Services.create(repositories=repositories, envs=envs)
    server = Server.create(__name__, envs=envs, services=services)
    server.load_routes()
    server.run()


if __name__ == '__main__':
    main()
