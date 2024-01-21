from pymongo import MongoClient
from bson import ObjectId
from config import DATABASE_TOKEN
from models.book import Book as DBBook, Author as DBAuthor, Genre as DBGenre, Subgenre as DBSubgenre
from pydantic import BaseModel
from typing import List

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

class AuthorBase(BaseModel):
    name: str
    birth_year: int
    nationality: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: str

    class Config:
        orm_mode = True

class GenreBase(BaseModel):
    name: str
    description: str

class GenreCreate(GenreBase):
    pass

class Genre(GenreBase):
    id: str

    class Config:
        orm_mode = True

class SubgenreBase(BaseModel):
    name: str
    description: str
    parent_genre_id: str

class SubgenreCreate(SubgenreBase):
    pass

class Subgenre(SubgenreBase):
    id: str

    class Config:
        orm_mode = True

client = MongoClient(DATABASE_TOKEN)
db = client.get_database()

# collections
books_collection = db.get_collection("books")
authors_collection = db.get_collection("authors")
genres_collection = db.get_collection("genres")
subgenres_collection = db.get_collection("subgenres")

# Books CRUD functions
def get_books() -> List[Book]:
    return [Book(**book) for book in books_collection.find()]

def get_book(book_id: str) -> Book:
    return Book(**books_collection.find_one({"_id": ObjectId(book_id)}))

def create_book(book: BookCreate) -> Book:
    result = books_collection.insert_one(book.dict())
    book_id = str(result.inserted_id)
    return Book(id=book_id, **book.dict())

def update_book(book_id: str, updated_book: BookCreate) -> Book:
    books_collection.update_one({"_id": ObjectId(book_id)}, {"$set": updated_book.dict()})
    return Book(id=book_id, **updated_book.dict())

def delete_book(book_id: str) -> Book:
    deleted_book = books_collection.find_one_and_delete({"_id": ObjectId(book_id)})
    return Book(**deleted_book)

# Authors CRUD functions
def get_authors() -> List[Author]:
    return [Author(**author) for author in authors_collection.find()]

def get_author(author_id: str) -> Author:
    return Author(**authors_collection.find_one({"_id": ObjectId(author_id)}))

def create_author(author: AuthorCreate) -> Author:
    result = authors_collection.insert_one(author.dict())
    author_id = str(result.inserted_id)
    return Author(id=author_id, **author.dict())

def update_author(author_id: str, updated_author: AuthorCreate) -> Author:
    authors_collection.update_one({"_id": ObjectId(author_id)}, {"$set": updated_author.dict()})
    return Author(id=author_id, **updated_author.dict())

def delete_author(author_id: str) -> Author:
    deleted_author = authors_collection.find_one_and_delete({"_id": ObjectId(author_id)})
    return Author(**deleted_author)

# Genres CRUD functions
def get_genres() -> List[Genre]:
    return [Genre(**genre) for genre in genres_collection.find()]

def get_genre(genre_id: str) -> Genre:
    return Genre(**genres_collection.find_one({"_id": ObjectId(genre_id)}))

def create_genre(genre: GenreCreate) -> Genre:
    result = genres_collection.insert_one(genre.dict())
    genre_id = str(result.inserted_id)
    return Genre(id=genre_id, **genre.dict())

def update_genre(genre_id: str, updated_genre: GenreCreate) -> Genre:
    genres_collection.update_one({"_id": ObjectId(genre_id)}, {"$set": updated_genre.dict()})
    return Genre(id=genre_id, **updated_genre.dict())

def delete_genre(genre_id: str) -> Genre:
    deleted_genre = genres_collection.find_one_and_delete({"_id": ObjectId(genre_id)})
    return Genre(**deleted_genre)

# Subgenres CRUD functions
def get_subgenres() -> List[Subgenre]:
    return [Subgenre(**subgenre) for subgenre in subgenres_collection.find()]

def get_subgenre(subgenre_id: str) -> Subgenre:
    return Subgenre(**subgenres_collection.find_one({"_id": ObjectId(subgenre_id)}))

def create_subgenre(subgenre: SubgenreCreate) -> Subgenre:
    result = subgenres_collection.insert_one(subgenre.dict())
    subgenre_id = str(result.inserted_id)
    return Subgenre(id=subgenre_id, **subgenre.dict())

def update_subgenre(subgenre_id: str, updated_subgenre: SubgenreCreate) -> Subgenre:
    subgenres_collection.update_one({"_id": ObjectId(subgenre_id)}, {"$set": updated_subgenre.dict()})
    return Subgenre(id=subgenre_id, **updated_subgenre.dict())

def delete_subgenre(subgenre_id: str) -> Subgenre:
    deleted_subgenre = subgenres_collection.find_one_and_delete({"_id": ObjectId(subgenre_id)})
    return Subgenre(**deleted_subgenre)
