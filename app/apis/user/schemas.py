from typing import Optional

from pydantic import BaseModel


class UserProfileResponse(BaseModel):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    message: Optional[str] = None


class UserLogin(BaseModel):
    email: str
    password: str


class TokenUser(BaseModel):
    access_token: str
    refresh_token: str
