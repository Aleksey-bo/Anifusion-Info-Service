from typing import List

from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base
from schemas.genre_schemas import GenreShemas
from schemas.movie_schemas import MovieSchemas
from schemas.country_schemas import CountrySchemas
from schemas.studio_schemas import StudioSchemas


movie_genre_association = Table(
    "movie_genre_association",
    Base.metadata,
    Column("movie_id", ForeignKey("movies.id"), primary_key=True),
    Column("genre_id", ForeignKey("genres.id"), primary_key=True)
)


movie_studio_association = Table(
    "movie_studio_association",
    Base.metadata,
    Column("movie_id", ForeignKey("movies.id"), primary_key=True),
    Column("studio_id", ForeignKey("studios.id"), primary_key=True)
)


class GenreModels(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(primary_key=True)
    genre_name: Mapped[str] = mapped_column()

    movies: Mapped[List["MovieModels"]] = relationship(
        "MovieModels", secondary=movie_genre_association, back_populates="genres"
    )

    def to_read_model(self) -> GenreShemas:
        return GenreShemas(**(self.__dict__))


class CountryModels(Base):
    __tablename__ = "countries"

    id: Mapped[int] = mapped_column(primary_key=True)
    country_name: Mapped[str] = mapped_column()

    def to_read_model(self) -> CountrySchemas:
        return CountrySchemas(**(self.__dict__))


class StudioModels(Base):
    __tablename__ = "studios"

    id: Mapped[int] = mapped_column(primary_key=True)
    studio_name: Mapped[str] = mapped_column()

    movies: Mapped[List["MovieModels"]] = relationship(
        "MovieModels", secondary=movie_genre_association, back_populates="studios"
    )

    def to_read_model(self) -> StudioSchemas:
        return StudioSchemas(**(self.__dict__))


class MovieModels(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

    studios: Mapped[List[StudioModels]] = relationship(
        "StudioModels", secondary=movie_genre_association, back_populates="movies"
    )

    genres: Mapped[List[GenreModels]] = relationship(
        "Genre", secondary=movie_genre_association, back_populates="movies"
    )

    def to_read_model(self) -> MovieSchemas:
        return MovieSchemas(
            id=self.id,
            title=self.title,
            description=self.description,
            genres=[genre.to_read_model() for genre in self.genres]
        )
