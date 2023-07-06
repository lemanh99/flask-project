from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter
from starlette.status import HTTP_200_OK

from app.apis.user.schemas import UserProfileResponse, UserLogin, TokenUser
from app.apis.user.service import UserService


@inject
def get_user_router(user_service: UserService = Provide["user_container.user_service"]):
    router = APIRouter()

    @router.get(
        "/me",
        response_description="Get user profile",
        status_code=HTTP_200_OK,
        response_model=UserProfileResponse
    )
    async def get_user_profile() -> UserProfileResponse:
        return await user_service.get_user_profile()

    @router.post(
        "/login",
        response_description="Login user",
        status_code=HTTP_200_OK,
        response_model=UserLogin
    )
    async def login(req_data: UserLogin) -> TokenUser:
        return await user_service.get_user_profile()

    return router
