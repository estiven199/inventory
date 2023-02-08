import pymongo
from pymongo import database
import certifi
from os import getenv
from fastapi import HTTPException, status
from core.security import verify_token
from cryptography.fernet import Fernet

ca = certifi.where()


def connect_to_mongo(token: str) -> database:
    f = Fernet(getenv("SECRET"))
    tokens = verify_token(token)
    data_to_connect_to_mongoDB = {
        "username": f.decrypt(tokens['x_token'].encode('utf-8')).decode('utf-8'),
        "password": f.decrypt(tokens['x_api_key'].encode('utf-8')).decode('utf-8'),
        "cluster": f.decrypt(tokens['x_secret_id'].encode('utf-8')).decode('utf-8'),
    }
    mongo_url = "mongodb+srv://{username}:{password}@{cluster}/retryWrites=true&w=majority".format(**data_to_connect_to_mongoDB)
    client = pymongo.MongoClient(mongo_url, tlsCAFile=ca)
    db = client['fastAPI']
    try:
        db.command("ping")
        return db
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Error connecting to database.",
        )
