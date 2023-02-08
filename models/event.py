from pydantic import BaseModel
from typing import Optional


class Event(BaseModel):
    name: str
    type: str
    description: str


class EvenUpdate(Event):
    status: str
