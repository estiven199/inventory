from datetime import datetime, timedelta

import jwt
from jwt import exceptions
from os import getenv
from passlib.context import CryptContext
from fastapi import HTTPException, status

from core.config import settings
from models.auth import Keys

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def create_access_token(
    data: Keys, expires_delta: timedelta = None
) -> str:

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    encoded_jwt = jwt.encode(
        payload={**data, "exp": expire}, key=settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str) -> None:
    try:
        # if output:
        #     return jwt.decode(token, key=getenv("SECRET"), algorithms=["HS256"])
        jwt.decode(token, key=getenv("SECRET"), algorithms=ALGORITHM)
    except exceptions.DecodeError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token.",
        )
    except exceptions.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not authorized to perform this operation"
        )
