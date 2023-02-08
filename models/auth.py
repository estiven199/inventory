from pydantic import BaseModel

class Keys(BaseModel):
    x_token: str
    x_api_key: str
    x_secret_id: str