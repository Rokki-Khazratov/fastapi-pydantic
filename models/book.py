from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    genre: str
    subgenre: str
    year: int
