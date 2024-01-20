from pydantic import BaseModel

class Subgenre(BaseModel):
    name: str
    description: str
    parent_genre: str
