from fastapi import APIRouter

from app.apis.user.routers import get_user_router


def get_app_router():
    router = APIRouter()
    router.include_router(router=get_user_router(), prefix="/user", tags=["user"])
    return router
