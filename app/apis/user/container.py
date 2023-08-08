"""Module to provide the containers with injected services for the app"""

from dependency_injector import containers, providers

from app.apis.user.service import UserService


class UserContainer(containers.DeclarativeContainer):
    """Container to serve the User service with the configured repository"""
    repository = providers.Dependency()

    # Configure repository to use
    user_repository = providers.Singleton(
        repository
    )
    # Configure service with repository
    user_service = providers.Singleton(UserService, entity_repo=user_repository)
