from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

from core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def create_access_token(
    subject: str | any, expires_delta: timedelta = None
) -> str:

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_code = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_code, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
