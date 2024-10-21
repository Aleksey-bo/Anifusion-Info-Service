from typing import List
from enum import Enum

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from db.db import Base
from schemas.genre_schemas import GenreShemas


class Type(str, Enum):
    show = "show"
    movie = "movie"


class Genre(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(primary_key=True)
    genre_name: Mapped[str] = mapped_column()

    movie: Mapped["MovieModels"] = relationship(back_populates="genre")

    def to_read_model(self) -> GenreShemas:
        return GenreShemas(**(self.__dict__))
    

class MovieModels(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    genre_id: Mapped[int] = mapped_column(ForeignKey("genres.id"))

    genre: Mapped[List["Genre"]] = relationship(back_populates="movie")