from dependency_injector import containers, providers

from app.apis.repositories import get_repository
from app.apis.user import routers as user_router
from app.apis.user.container import UserContainer


class AppContainer(containers.DeclarativeContainer):
    """Container to serve all the containers related to the app"""
    # Set wiring between endpoints and injected repositories
    wiring_config = containers.WiringConfiguration(modules=[user_router])

    repository = providers.Singleton(get_repository, 'user')

    user_container = providers.Container(
        UserContainer,
        repository=repository,
    )
