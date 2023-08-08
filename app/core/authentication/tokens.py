import datetime
from typing import Union, Any
from uuid import uuid4

import jwt
from passlib.context import CryptContext

from app.core.authentication.contants import JWT_SECRET_KEY, JWT_ALGORITHM, TOKEN_TYPE_CLAIM, JTI_CLAIM, USER_ID_CLAIM, \
    JWT_ACCESS_TOKEN_EXPIRE, JWT_REFRESH_TOKEN_EXPIRE
from app.core.authentication.exceptions import TokenError
from app.core.utils.datetime import convert_datetime_to_epoch, convert_epoch_to_datetime

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Token:
    token_type = None
    lifetime = None

    def __init__(self, token=None):
        if self.token_type is None or self.lifetime is None:
            raise TokenError('Cannot create token with no type or lifetime')

        self.token = token
        self.current_time = datetime.datetime.utcnow()
        self.payload = {TOKEN_TYPE_CLAIM: self.token_type}

        # Set "exp" claim with default value
        self.set_exp(from_time=self.current_time, lifetime=self.lifetime)

        # Set "jti" claim
        self.set_jti()

    def get_payload(self, key, default=None):
        return self.payload.get(key, default)

    def set_jti(self):
        self.payload[JTI_CLAIM] = uuid4().hex

    def set_exp(self, claim='exp', from_time=None, lifetime=None):
        if from_time is None:
            from_time = self.current_time

        if lifetime is None:
            lifetime = self.lifetime

        self.payload[claim] = convert_datetime_to_epoch(from_time + lifetime)

    def check_exp(self, claim='exp', current_time=None):
        if current_time is None:
            current_time = self.current_time

        try:
            claim_value = self.payload[claim]
        except KeyError:
            raise TokenError(f"Token has no '{claim}' claim")

        claim_time = convert_epoch_to_datetime(claim_value)
        if claim_time <= current_time:
            raise TokenError(f"Token '{claim}' claim has expired")

    def for_user(self, user):
        user_id = getattr(user, 'user_id', None)
        if not isinstance(user_id, int):
            user_id = str(user_id)

        payload = self.payload
        payload[USER_ID_CLAIM] = user_id

        return payload

    def get_token(self):
        if not self.payload:
            self.payload = {}

        return jwt.encode(self.payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

    def verify_token(self, token):
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
            return payload
        except jwt.PyJWTError:
            return None


class AccessToken(Token):
    token_type = 'access'
    lifetime = JWT_ACCESS_TOKEN_EXPIRE


class RefreshAccessToken(Token):
    token_type = 'refresh'
    lifetime = JWT_REFRESH_TOKEN_EXPIRE
