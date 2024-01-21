from motor.motor_asyncio import AsyncIOMotorClient
from databases import Database
from config import DATABASE_TOKEN

DATABASE_URL = DATABASE_TOKEN

# Create the motor client
client = AsyncIOMotorClient(DATABASE_URL)

# Create the database instance
database = Database(DATABASE_URL)