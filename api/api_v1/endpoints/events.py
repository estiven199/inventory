from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, status, Header, Query
from schemas.event import EventSchema
from db.init_db import connect_to_mongo


from models.event import Event, EvenUpdate
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
        args.update({"status": status})
    if management != None:
        args.update({"management": management})

    data = eventCrud.get_multi_events(db, args)
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

    db = connect_to_mongo(token)
    data = eventCrud.create_event(db, dict(event))
    return data


@router.get("/events/{event_id}", response_model=EventSchema)
def get_event(event_id: str, token: str = Header(default=None, required=True)):
    db = connect_to_mongo(token)
    data = eventCrud.get_event(db, event_id)
    return data if data else "The event does not exist.."


@router.put("/events/{event_id}", response_model=EventSchema)
def updaate_event(event: EvenUpdate, event_id: str, token: str = Header(default=None, required=True)):
    db = connect_to_mongo(token)
    val = eventCrud.get_event(db, event_id)
    if val['status'] == 'revisada':
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The event cannot be modified.",
        )
    event = {k: v for k, v in dict(event).items() if v != None}
    data = eventCrud.update_event(db, event_id, event)
    return data if data else "The event does not exist."


@router.delete("/events/{event_id}")
def delete_event(event_id: str, token: str = Header(default=None, required=True)):
    db = connect_to_mongo(token)
    msg = eventCrud.delete_event(db, event_id)
    return msg


@router.put("/events/mark_as_check/{event_id}", response_model=EventSchema)
def mark_event__as_check(event_id: str, token: str = Header(default=None, required=True)):
    db = connect_to_mongo(token)
    obj_in = {"status": "revisada"}
    data = eventCrud.update_event(db, event_id, obj_in)
    return data
