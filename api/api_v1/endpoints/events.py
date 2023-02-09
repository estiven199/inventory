from fastapi import APIRouter, HTTPException, status, Header, Query
from schemas.event import EventSchema, EventUpdateSchema
from db.init_db import connect_to_mongo

import json

from models.event import Event, EvenUpdate
from crud.crud_event import eventCrud

router = APIRouter()


@router.get("/events", response_model=list[EventSchema])
async def read_events(token: str = Header(default=None, required=True), status: str = Query(
        default=None,
        title="Estado del evento.",
        description="Recuerda utilizar solo estos valores: [solicitud, revision, aprobacion].",
),
    management: bool = Query(
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
async def create_event(event: Event = None, token: str = Header(default=None, required=True)) -> any:
    """
    Crear un nuevo Evento.

    **Parametros**

    * `name`: Es una cadena de texto plano no mayor a 20 caracteres.
    * `type`: Solo estan permitidos los siguientes valores : [solicitud, revision, aprobacion].
    * `description`: Es una cadena de texto plano no mayor a 120 caracteres.
    """
    db = connect_to_mongo(token)
    if event == None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The json is required.",
        )
    data = eventCrud.create_event(db, dict(event))
    return data


@router.get("/events/{event_id}", response_model=EventSchema)
async def get_event(event_id: str, token: str = Header(default=None, required=True)):
    db = connect_to_mongo(token)
    data = eventCrud.get_event(db, event_id)
    return data if data else "The event does not exist.."


@router.put("/events/{event_id}", response_model=EventSchema)
async def updaate_event(event: EvenUpdate, event_id: str, token: str = Header(default=None, required=True)):
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
async def delete_event(event_id: str, token: str = Header(default=None, required=True)):
    db = connect_to_mongo(token)
    msg = eventCrud.delete_event(db, event_id)
    return msg


@router.put("/events/mark_as_check/{event_id}", response_model=EventUpdateSchema)
async def mark_event__as_check(event_id: str, token: str = Header(default=None, required=True)):
    db = connect_to_mongo(token)
    val = eventCrud.get_event(db, event_id)
    if val['status'] == 'revisada':
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The event is already reviewed.",
        )
    management = True if val['type'] in ['solicitud', 'revision'] else False
    obj_in = {"status": "revisada", "management": management}
    data = eventCrud.update_event(db, event_id, obj_in)
    return data


@router.post("/genetare_data")
async def generate_data_of_example(token: str = Header(default=None, required=True)):
    db = connect_to_mongo(token)
    with open("data_example.json", "r") as file:
        data = json.load(file)
    for doc in data:
        eventCrud.create_event(db, doc)
    return str(data)
