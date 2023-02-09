from models.event import Event
from crud.base import crudbase
from pymongo import database
import datetime as dt

from fastapi import HTTPException, status


class CRUDEvent():
    def create_event(self, db: database, obj_in: Event):
        obj_in = dict(obj_in)
        if obj_in['type'].lower() not in ['solicitud', 'revision', 'aprobacion']:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Value not allowed.",
            )
        obj_in['status'] = "pendiente"
        obj_in['date'] = dt.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        new_event = crudbase.create(db.events, obj_in)
        return new_event

    def get_multi_events(self, db: database, arg):
        return crudbase.get_all(db.events, arg)


eventCrud = CRUDEvent()
