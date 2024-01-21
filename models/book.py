from pymongo import MongoClient
from bson import ObjectId
from config import DATABASE_URL


client = MongoClient(DATABASE_URL)
db = client.get_database()

books_collection = db["books"]
authors_collection = db["authors"]
genres_collection = db["genres"]
subgenres_collection = db["subgenres"]

class Genre:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Subgenre:
    def __init__(self, name, description, parent_genre_id):
        self.name = name
        self.description = description
        self.parent_genre_id = parent_genre_id

class Book:
    def __init__(self, title, author_id, subgenre_id, year):
        self.title = title
        self.author_id = author_id
        self.subgenre_id = subgenre_id
        self.year = year

class Author:
    def __init__(self, name, birth_year, nationality):
        self.name = name
        self.birth_year = birth_year
        self.nationality = nationality