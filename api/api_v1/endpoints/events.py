from fastapi import APIRouter, HTTPException, status, Header
from schemas.event import EventCreate
from db.init_db import connect_to_mongo

from models.event import Event
from crud.crud_event import eventCrud

router = APIRouter()


@router.post("/events", response_model=EventCreate)
async def create_event(event: Event, token: str = Header(default=None, required=True)) -> any:
    """
    Crear un nuevo Evento.

    **Parameters**

    * `name`: Es una cadena de texto plano no mayor a 20 caracteres.
    * `type`: Solo estan permitidos los siguientes valores : [solicitud, revision, aprobacion].
    * `description`: Es una cadena de texto plano no mayor a 120 caracteres.
    """
    if token == None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token field required",
        )
    db = connect_to_mongo(token)
    data = eventCrud.create_event(db, dict(event))
    return data
