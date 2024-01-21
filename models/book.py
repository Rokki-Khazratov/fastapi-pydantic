from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#Genres
class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

class Subgenre(Base):
    __tablename__ = 'subgenres'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    parent_genre_id = Column(Integer, ForeignKey('genres.id'))
    parent_genre = relationship('Genre', back_populates='subgenres')

#Books
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    subgenre_id = Column(Integer, ForeignKey('subgenres.id'))
    subgenre = relationship('Subgenre', back_populates='books')
    year = Column(Integer)

#Authors
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birth_year = Column(Integer)
    nationality = Column(String)
    books = relationship('Book', back_populates='author')
