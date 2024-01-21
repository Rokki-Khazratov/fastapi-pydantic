from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from database.db import get_books, get_book, create_book, update_book, delete_book
from models.book import Book as DBBook

router = APIRouter()

# Books API routes
@router.get("/books", response_model=list[DBBook])
def read_books(db: Session = Depends(get_db)):
    return get_books(db)

@router.post("/books", response_model=DBBook)
def create_new_book(book: DBBook, db: Session = Depends(get_db)):
    return create_book(db, book)

@router.get("/book/{book_id}", response_model=DBBook)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = get_book(db, book_id)
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.put("/book/{book_id}", response_model=DBBook)
def update_existing_book(book_id: int, updated_book: DBBook, db: Session = Depends(get_db)):
    return update_book(db, book_id, updated_book)

@router.delete("/book/{book_id}", response_model=DBBook)
def delete_existing_book(book_id: int, db: Session = Depends(get_db)):
    return delete_book(db, book_id)
