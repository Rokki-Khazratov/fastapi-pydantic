from pymongo import MongoClient
from bson import ObjectId
from config import DATABASE_URL
from models.book import Book as DBBook, Author as DBAuthor, Genre as DBGenre, Subgenre as DBSubgenre


client = MongoClient(DATABASE_URL)
db = client.get_database()

# collections
books_collection = db.get_collection("books")
authors_collection = db.get_collection("authors")
genres_collection = db.get_collection("genres")
subgenres_collection = db.get_collection("subgenres")

# Books CRUD functions
def get_books():
    return list(books_collection.find())

def get_book(book_id: str):
    return books_collection.find_one({"_id": ObjectId(book_id)})

def create_book(book: DBBook):
    result = books_collection.insert_one(book.dict())
    book_id = str(result.inserted_id)
    return {**book.dict(), "id": book_id}

def update_book(book_id: str, updated_book: DBBook):
    books_collection.update_one({"_id": ObjectId(book_id)}, {"$set": updated_book.dict()})
    return {**updated_book.dict(), "id": book_id}

def delete_book(book_id: str):
    deleted_book = books_collection.find_one_and_delete({"_id": ObjectId(book_id)})
    return deleted_book

# Authors CRUD functions
def get_authors():
    return list(authors_collection.find())

def get_author(author_id: str):
    return authors_collection.find_one({"_id": ObjectId(author_id)})

def create_author(author: DBAuthor):
    result = authors_collection.insert_one(author.dict())
    author_id = str(result.inserted_id)
    return {**author.dict(), "id": author_id}

def update_author(author_id: str, updated_author: DBAuthor):
    authors_collection.update_one({"_id": ObjectId(author_id)}, {"$set": updated_author.dict()})
    return {**updated_author.dict(), "id": author_id}

def delete_author(author_id: str):
    deleted_author = authors_collection.find_one_and_delete({"_id": ObjectId(author_id)})
    return deleted_author

# Genres CRUD functions
def get_genres():
    return list(genres_collection.find())

def get_genre(genre_id: str):
    return genres_collection.find_one({"_id": ObjectId(genre_id)})

def create_genre(genre: DBGenre):
    result = genres_collection.insert_one(genre.dict())
    genre_id = str(result.inserted_id)
    return {**genre.dict(), "id": genre_id}

def update_genre(genre_id: str, updated_genre: DBGenre):
    genres_collection.update_one({"_id": ObjectId(genre_id)}, {"$set": updated_genre.dict()})
    return {**updated_genre.dict(), "id": genre_id}

def delete_genre(genre_id: str):
    deleted_genre = genres_collection.find_one_and_delete({"_id": ObjectId(genre_id)})
    return deleted_genre

# Subgenres CRUD functions
def get_subgenres():
    return list(subgenres_collection.find())

def get_subgenre(subgenre_id: str):
    return subgenres_collection.find_one({"_id": ObjectId(subgenre_id)})

def create_subgenre(subgenre: DBSubgenre):
    result = subgenres_collection.insert_one(subgenre.dict())
    subgenre_id = str(result.inserted_id)
    return {**subgenre.dict(), "id": subgenre_id}

def update_subgenre(subgenre_id: str, updated_subgenre: DBSubgenre):
    subgenres_collection.update_one({"_id": ObjectId(subgenre_id)}, {"$set": updated_subgenre.dict()})
    return {**updated_subgenre.dict(), "id": subgenre_id}

def delete_subgenre(subgenre_id: str):
    deleted_subgenre = subgenres_collection.find_one_and_delete({"_id": ObjectId(subgenre_id)})
    return deleted_subgenre
