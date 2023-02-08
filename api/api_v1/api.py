from fastapi import APIRouter
from api.api_v1.endpoints import login, events



api_router = APIRouter()

api_router.include_router(login.router, tags=["login"])
api_router.include_router(events.router, tags=["Events"])

