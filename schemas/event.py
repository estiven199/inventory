from pydantic import BaseModel

class EventSchema(BaseModel):
    id: str
    name: str
    type: str
    description: str
    date: str
    status: str

class EventUpdateSchema(EventSchema):
    management: bool
