from fastapi import APIRouter, HTTPException
from models.book import Book
from database.db import get_books, get_book, create_book, update_book, delete_book

router = APIRouter()

#Books API routes
@router.get("/books", response_model=list[Book])
def read_books():
    return get_books()

@router.post("/books", response_model=Book)
def create_new_book(book: Book):
    return create_book(book)

@router.get("/book/{book_id}", response_model=Book)
def read_book(book_id: str):
    book = get_book(book_id)
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.put("/book/{book_id}", response_model=Book)
def update_existing_book(book_id: str, updated_book: Book):
    return update_book(book_id, updated_book)

@router.delete("/book/{book_id}", response_model=Book)
def delete_existing_book(book_id: str):
    return delete_book(book_id)
