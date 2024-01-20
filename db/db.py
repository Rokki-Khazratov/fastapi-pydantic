from pymongo import MongoClient
from app.config import DATABASE_URL
from app.models.book import Book
from bson import ObjectId

#connect
client = MongoClient(DATABASE_URL)
db = client.get_database()

# collections
books_collection = db.get_collection("books")
authors_collection = db.get_collection("authors")
genres_collection = db.get_collection("genres")
subgenres_collection = db.get_collection("subgenres")

# books CRUD functions
def get_books():
    return list(books_collection.find())

def get_book(book_id: str):
    return books_collection.find_one({"_id": ObjectId(book_id)})

def create_book(book: Book):
    result = books_collection.insert_one(book.dict())
    book_id = str(result.inserted_id)
    return {**book.dict(), "id": book_id}

def update_book(book_id: str, updated_book: Book):
    books_collection.update_one({"_id": ObjectId(book_id)}, {"$set": updated_book.dict()})
    return {**updated_book.dict(), "id": book_id}

def delete_book(book_id: str):
    deleted_book = books_collection.find_one_and_delete({"_id": ObjectId(book_id)})
    return deleted_book
