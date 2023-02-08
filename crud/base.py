from pymongo import database

from typing import TypeVar

from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from bson import ObjectId


class CRUDBase():
    def create(self, db: database, obj_in):
        obj_in_data = jsonable_encoder(obj_in)
        id = db.insert_one(obj_in_data).inserted_id
        db_obj = db.find_one({"_id": ObjectId(id)})
        db_obj['id'] = str(db_obj['_id'])
        del db_obj['_id']
        return db_obj
crudbase = CRUDBase()