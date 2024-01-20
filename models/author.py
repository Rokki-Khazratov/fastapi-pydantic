from pydantic import BaseModel

class Author(BaseModel):
    name: str
    birth_year: int
    nationality: str
