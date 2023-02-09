from typing import Optional
from pydantic import BaseModel
from fastapi import Query

# Shared properties


class EventSchema(BaseModel):
    id: str
    name: str
    type: str
    description: str
    date: str
    status: str


class EventUpdateSchema(EventSchema):
    management: bool
