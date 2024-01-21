from fastapi import FastAPI
from routes import books,authors,genres

app = FastAPI()

app.include_router(books.router, prefix="/api/", tags=["books"])
app.include_router(authors.router, prefix="/api/", tags=["authors"])
app.include_router(genres.router, prefix="/api/", tags=["genres"])

