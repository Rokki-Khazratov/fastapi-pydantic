from pymongo import MongoClient
from pydantic import BaseModel
from bson import ObjectId
from typing import Optional
from config import DATABASE_TOKEN


# client = MongoClient(DATABASE_TOKEN)
# db = client.get_database()

# books_collection = db["books"]
# authors_collection = db["authors"]
# genres_collection = db["genres"]

# subgenres_collection = db["subgenres"]

class Genre(BaseModel):
    name: str
    description: str

class Subgenre(BaseModel):
    name: str
    description: str
    parent_genre_id: str

class BookBase(BaseModel):
    title: str
    author_id: str
    subgenre_id: str
    year: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: str

    class Config:
        orm_mode = True

class Author(BaseModel):
    name: str
    birth_year: int
    nationality: str
