from fastapi import APIRouter, Depends, HTTPException
from pymongo.database import Database as MongoDB
from models.book import Author as DBAuthor, Book as DBBook, Genre as DBGenre, Subgenre as DBSubgenre
from database.db import *
from database import get_db

router = APIRouter()

# Authors API routes
@router.get("/authors", response_model=list[DBAuthor])
def read_authors(db: MongoDB = Depends(get_db)):
    return get_authors(db)

@router.post("/authors", response_model=DBAuthor)
def create_new_author(author: AuthorCreate, db: MongoDB = Depends(get_db)):
    return create_author(db, author)

@router.get("/author/{author_id}", response_model=DBAuthor)
def read_author(author_id: str, db: MongoDB = Depends(get_db)):
    author = get_author(db, author_id)
    if author:
        return author
    raise HTTPException(status_code=404, detail="Author not found")

@router.put("/author/{author_id}", response_model=DBAuthor)
def update_existing_author(author_id: str, updated_author: AuthorCreate, db: MongoDB = Depends(get_db)):
    return update_author(db, author_id, updated_author)

@router.delete("/author/{author_id}", response_model=DBAuthor)
def delete_existing_author(author_id: str, db: MongoDB = Depends(get_db)):
    return delete_author(db, author_id)

# Books API routes
@router.get("/books", response_model=list[DBBook])
def read_books(db: MongoDB = Depends(get_db)):
    return get_books(db)

@router.post("/books", response_model=DBBook)
def create_new_book(book: BookCreate, db: MongoDB = Depends(get_db)):
    return create_book(db, book)

@router.get("/book/{book_id}", response_model=DBBook)
def read_book(book_id: str, db: MongoDB = Depends(get_db)):
    book = get_book(db, book_id)
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.put("/book/{book_id}", response_model=DBBook)
def update_existing_book(book_id: str, updated_book: BookCreate, db: MongoDB = Depends(get_db)):
    return update_book(db, book_id, updated_book)

@router.delete("/book/{book_id}", response_model=DBBook)
def delete_existing_book(book_id: str, db: MongoDB = Depends(get_db)):
    return delete_book(db, book_id)

# Genres API routes
@router.get("/genres", response_model=list[DBGenre])
def read_genres(db: MongoDB = Depends(get_db)):
    return get_genres(db)

@router.post("/genres", response_model=DBGenre)
def create_new_genre(genre: GenreCreate, db: MongoDB = Depends(get_db)):
    return create_genre(db, genre)

@router.get("/genre/{genre_id}", response_model=DBGenre)
def read_genre(genre_id: str, db: MongoDB = Depends(get_db)):
    genre = get_genre(db, genre_id)
    if genre:
        return genre
    raise HTTPException(status_code=404, detail="Genre not found")

@router.put("/genre/{genre_id}", response_model=DBGenre)
def update_existing_genre(genre_id: str, updated_genre: GenreCreate, db: MongoDB = Depends(get_db)):
    return update_genre(db, genre_id, updated_genre)

@router.delete("/genre/{genre_id}", response_model=DBGenre)
def delete_existing_genre(genre_id: str, db: MongoDB = Depends(get_db)):
    return delete_genre(db, genre_id)

# Subgenres API routes
@router.get("/subgenres", response_model=list[DBSubgenre])
def read_subgenres(db: MongoDB = Depends(get_db)):
    return get_subgenres(db)

@router.post("/subgenres", response_model=DBSubgenre)
def create_new_subgenre(subgenre: SubgenreCreate, db: MongoDB = Depends(get_db)):
    return create_subgenre(db, subgenre)

@router.get("/subgenre/{subgenre_id}", response_model=DBSubgenre)
def read_subgenre(subgenre_id: str, db: MongoDB = Depends(get_db)):
    subgenre = get_subgenre(db, subgenre_id)
    if subgenre:
        return subgenre
    raise HTTPException(status_code=404, detail="Subgenre not found")

@router.put("/subgenre/{subgenre_id}", response_model=DBSubgenre)
def update_existing_subgenre(subgenre_id: str, updated_subgenre: SubgenreCreate, db: MongoDB = Depends(get_db)):
    return update_subgenre(db, subgenre_id, updated_subgenre)

@router.delete("/subgenre/{subgenre_id}", response_model=DBSubgenre)
def delete_existing_subgenre(subgenre_id: str, db: MongoDB = Depends(get_db)):
    return delete_subgenre(db, subgenre_id)
