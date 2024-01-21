from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from database.db import (
    get_genres, get_genre, create_genre, update_genre, delete_genre,
    get_subgenres, get_subgenre, create_subgenre, update_subgenre, delete_subgenre
)
from models.book import Genre as DBGenre, Subgenre as DBSubgenre

router = APIRouter()

# Genres API routes
@router.get("/genres", response_model=list[DBGenre])
def read_genres(db: Session = Depends(get_db)):
    return get_genres(db)

@router.post("/genres", response_model=DBGenre)
def create_new_genre(genre: DBGenre, db: Session = Depends(get_db)):
    return create_genre(db, genre)

@router.get("/genre/{genre_id}", response_model=DBGenre)
def read_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = get_genre(db, genre_id)
    if genre:
        return genre
    raise HTTPException(status_code=404, detail="Genre not found")

@router.put("/genre/{genre_id}", response_model=DBGenre)
def update_existing_genre(genre_id: int, updated_genre: DBGenre, db: Session = Depends(get_db)):
    return update_genre(db, genre_id, updated_genre)

@router.delete("/genre/{genre_id}", response_model=DBGenre)
def delete_existing_genre(genre_id: int, db: Session = Depends(get_db)):
    return delete_genre(db, genre_id)


# Subgenres API routes
@router.get("/subgenres", response_model=list[DBSubgenre])
def read_subgenres(db: Session = Depends(get_db)):
    return get_subgenres(db)

@router.post("/subgenres", response_model=DBSubgenre)
def create_new_subgenre(subgenre: DBSubgenre, db: Session = Depends(get_db)):
    return create_subgenre(db, subgenre)

@router.get("/subgenre/{subgenre_id}", response_model=DBSubgenre)
def read_subgenre(subgenre_id: int, db: Session = Depends(get_db)):
    subgenre = get_subgenre(db, subgenre_id)
    if subgenre:
        return subgenre
    raise HTTPException(status_code=404, detail="Subgenre not found")

@router.put("/subgenre/{subgenre_id}", response_model=DBSubgenre)
def update_existing_subgenre(subgenre_id: int, updated_subgenre: DBSubgenre, db: Session = Depends(get_db)):
    return update_subgenre(db, subgenre_id, updated_subgenre)

@router.delete("/subgenre/{subgenre_id}", response_model=DBSubgenre)
def delete_existing_subgenre(subgenre_id: int, db: Session = Depends(get_db)):
    return delete_subgenre(db, subgenre_id)
