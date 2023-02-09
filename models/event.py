from pydantic import BaseModel
from typing import Optional


class Event(BaseModel):
    name: str
    type: str
    description: str


class EvenUpdate(BaseModel):
    name: str = None
    type: str = None
    description: str = None
