from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, status, Header, Query, Body
from schemas.event import EventSchema
from db.init_db import connect_to_mongo

from models.event import Event
from crud.crud_event import eventCrud

router = APIRouter()


@router.get("/events", response_model=list[EventSchema])
async def read_items(token: str = Header(default=None, required=True),
    status: str | None = Query(
        default=None,
        title="Estado del evento.",
        description="Recuerda utilizar solo estos valores: [solicitud, revision, aprobacion].",
),
    management: bool | None = Query(
            default=None,
            title="Eventos según la gestión.",
            description="Utiliza True para filtrar los eventos que necestian gestión.",
    )
):

    """
    Retrieve Events.

    """

    db = connect_to_mongo(token)

    args = {}
    if status != None:
        args.update ({"status":status})

    if management != None:
        args.update ({"management":management})


    data = eventCrud.get_multi_events(db,args)
    return data


@router.post("/events", response_model=EventSchema)
async def create_event(event: Event, token: str = Header(default=None, required=True)) -> any:
    """
    Crear un nuevo Evento.

    **Parametros**

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
