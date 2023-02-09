from pymongo import database

import bson
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from bson import ObjectId


class CRUDBase():

    def validate_id(self, id):
        if not bson.ObjectId.is_valid(id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid id",
            )

    def find_and_delete_id(self, db: database, id: str):
        db_obj = db.find_one({"_id": ObjectId(id)})
        if not db_obj:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The event does not exist.",
            )
        db_obj['id'] = str(db_obj['_id'])
        del db_obj['_id']
        return db_obj

    def create(self, db: database, obj_in: dict):
        obj_in_data = jsonable_encoder(obj_in)
        id = db.insert_one(obj_in_data).inserted_id
        return self.find_and_delete_id(db, id)

    def get_all(self, db: database, arg):
        data = []
        extre_param = {"$and": [arg]} if arg else {}
        for doc in db.find(extre_param):
            doc['id'] = str(doc['_id'])
            del doc['_id']
            data.append(doc)
        return data

    def get_one(self, db: database, id: str):
        self.validate_id(id)
        return self.find_and_delete_id(db, id)

    def update(self, db: database, id: str, obj_in: dict):
        self.validate_id(id)
        db.find_one_and_update({"_id": ObjectId(id)}, {"$set": obj_in})
        return self.find_and_delete_id(db, id)

    def delete(self, db: database, id: str):
        self.validate_id(id)
        self.find_and_delete_id(db, id)
        db.find_one_and_delete({"_id": ObjectId(id)})
        return "Done"



crudbase = CRUDBase()
