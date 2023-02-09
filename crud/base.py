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

    def get_all(self, db: database, arg):
        data = []
        print(arg)
        extre_param = {"$and": [arg]} if arg else {}
        for doc in db.find(extre_param):
            doc['id'] = str(doc['_id'])
            del doc['_id']
            data.append(doc)
        return data


crudbase = CRUDBase()
