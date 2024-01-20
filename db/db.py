from pymongo import MongoClient
from config import DATABASE_URL

client = MongoClient(DATABASE_URL)
db = client.get_database()