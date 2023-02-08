from datetime import timedelta

from fastapi import APIRouter, Header, HTTPException, status

from schemas import token
from core import security
from core.config import settings
router = APIRouter()


@router.post("/login/access-token", response_model=token.Token)
def login_access_token(x_token: str = Header(default=None, required=True),
                       x_api_key: str = Header(default=None, required=True),
                       x_secret_id: str = Header(default=None, required=True),
                       user_id: str = Header(default=None, required=True)
                       ) -> any:
    
    if not x_token or not x_api_key or not x_secret_id or not user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST
        )

    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            {
                "x_token": x_token,
                "x_api_key": x_api_key,
                "x_secret_id": x_secret_id,
                "user_id": user_id,
            },
            expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }
