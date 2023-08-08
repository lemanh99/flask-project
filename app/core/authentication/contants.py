from app.apis.config.settings import settings

JWT_SECRET_KEY = getattr(settings, 'JWT_SECRET_KEY', '')
JWT_ALGORITHM = getattr(settings, 'JWT_ALGORITHM', 'HS256')
JWT_ACCESS_TOKEN_EXPIRE = getattr(settings, 'JWT_ACCESS_TOKEN_EXPIRE', 'HS256')
JWT_REFRESH_TOKEN_EXPIRE = getattr(settings, 'JWT_REFRESH_TOKEN_EXPIRE', 'HS256')
TOKEN_TYPE_CLAIM = getattr(settings, 'TOKEN_TYPE_CLAIM', 'token_type')
JTI_CLAIM = 'jti'
USER_ID_CLAIM = 'user_id'
