from typing import Optional
from pydantic import BaseModel
from fastapi import Query

# Shared properties

class EventBase(BaseModel):
    id: str
    name: str 
    type: str 
    description: str
    date:str
    status:str
   


# Properties to receive on event creation
class EventCreate(EventBase):
    pass


# Properties to receive on event creation
class EventUpdates(EventBase):
    pass