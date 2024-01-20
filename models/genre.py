from pydantic import BaseModel

class Genre(BaseModel):
    name: str
    description: str
