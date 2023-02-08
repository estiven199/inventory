from fastapi import Depends, HTTPException, status
from core.security import verify_token

def get_current_user(token: Depends(verify_token)) -> str:
 
    return "user"
