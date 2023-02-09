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
        obj_in['management'] = ""
        new_event = crudbase.create(db.events, obj_in)
        return new_event

    def get_multi_events(self, db: database, arg: dict):
        return crudbase.get_all(db.events, arg)

    def get_event(self, db: database, event_id: str):
        return crudbase.get_one(db.events, event_id)

    def update_event(self, db: database, event_id: str, obj_in: dict):
        return crudbase.update(db.events, event_id, obj_in)

    def delete_event(self, db: database, event_id: str):
        return "The event has been deleted." if crudbase.delete(db.events, event_id) == "Done" else "Error"


eventCrud = CRUDEvent()
