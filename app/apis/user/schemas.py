from typing import Optional

from pydantic import BaseModel


class UserProfileResponse(BaseModel):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    message: Optional[str] = None
