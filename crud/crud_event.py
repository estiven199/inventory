from models.event import Event
from crud.base import crudbase
from pymongo import database

from fastapi import HTTPException, status


from schemas.event import EventCreate, EventUpdates


class CRUDEvent():
    def create_event(self, db: database, obj_in: Event):
        obj_in = dict(obj_in)
        if obj_in['type'].lower() not in ['solicitud', 'revision', 'aprobacion']:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Value not allowed.",
            )
        obj_in['status'] = "pendiente"
        obj_in['date'] = ""

        new_event = crudbase.create(db.event, obj_in)

        return new_event


eventCrud = CRUDEvent()
