
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from database.db import (
    get_authors, get_author, create_author, update_author, delete_author,
)
from models.book import Author as DBAuthor

router = APIRouter()

# Authors API routes
@router.get("/authors", response_model=list[DBAuthor])
def read_authors(db: Session = Depends(get_db)):
    return get_authors(db)

@router.post("/authors", response_model=DBAuthor)
def create_new_author(author: DBAuthor, db: Session = Depends(get_db)):
    return create_author(db, author)

@router.get("/author/{author_id}", response_model=DBAuthor)
def read_author(author_id: int, db: Session = Depends(get_db)):
    author = get_author(db, author_id)
    if author:
        return author
    raise HTTPException(status_code=404, detail="Author not found")

@router.put("/author/{author_id}", response_model=DBAuthor)
def update_existing_author(author_id: int, updated_author: DBAuthor, db: Session = Depends(get_db)):
    return update_author(db, author_id, updated_author)

@router.delete("/author/{author_id}", response_model=DBAuthor)
def delete_existing_author(author_id: int, db: Session = Depends(get_db)):
    return delete_author(db, author_id)

