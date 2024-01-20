from fastapi import FastAPI
from routes import books  

app = FastAPI()

app.include_router(books.router, prefix="/books", tags=["books"])

