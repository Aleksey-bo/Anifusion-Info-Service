from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base
from schemas.genre_schemas import GenreShemas
from schemas.movie_schemas import MovieSchemas
from schemas.country_schemas import CountrySchemas
from schemas.studio_schemas import StudioSchemas
from schemas.season_schemas import SeasonShemas
from schemas.serie_schemas import SerieSchemas


class MovieGenreAssociation(Base):
    __tablename__ = 'movie_genre'
    movie_id: Mapped[int] = mapped_column(ForeignKey('movies.id', ondelete="CASCADE"), primary_key=True)
    genre_id: Mapped[int] = mapped_column(ForeignKey('genres.id', ondelete="CASCADE"), primary_key=True)


class MovieStudioAssociation(Base):
    __tablename__ = 'movie_studio'
    movie_id: Mapped[int] = mapped_column(ForeignKey('movies.id', ondelete="CASCADE"), primary_key=True)
    studio_id: Mapped[int] = mapped_column(ForeignKey('studios.id', ondelete="CASCADE"), primary_key=True)


class GenreModels(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(primary_key=True)
    genre_name: Mapped[str] = mapped_column(unique=True)

    movies: Mapped[list["MovieModels"]] = relationship(
        secondary="movie_genre", back_populates="genres", lazy='selectin'
    )

    async def to_read_model(self) -> GenreShemas:
        return GenreShemas(**(self.__dict__))


class CountryModels(Base):
    __tablename__ = "countries"

    id: Mapped[int] = mapped_column(primary_key=True)
    country_name: Mapped[str] = mapped_column(unique=True)

    movies = relationship("MovieModels", back_populates="country", lazy='selectin')

    async def to_read_model(self) -> CountrySchemas:
        return CountrySchemas(**(self.__dict__))


class StudioModels(Base):
    __tablename__ = "studios"

    id: Mapped[int] = mapped_column(primary_key=True)
    studio_name: Mapped[str] = mapped_column(unique=True)

    movies: Mapped[List["MovieModels"]] = relationship(
        secondary="movie_studio", back_populates="studios", lazy='selectin'
    )

    async def to_read_model(self) -> StudioSchemas:
        return StudioSchemas(**(self.__dict__))


class MovieModels(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column()
    country_id: Mapped[int] = mapped_column(ForeignKey("countries.id"))

    country = relationship("CountryModels", back_populates="movies", lazy='selectin')

    genres: Mapped[List["GenreModels"]] = relationship(
        secondary="movie_genre", back_populates="movies", lazy='selectin', passive_deletes=True
    )
    studios: Mapped[List["StudioModels"]] = relationship(
        secondary="movie_studio", back_populates="movies", lazy='selectin', passive_deletes=True
    )

    season: Mapped["SeasonModels"] = relationship(
        back_populates="movie", passive_deletes=True
    )

    async def to_read_model(self) -> MovieSchemas:
        return MovieSchemas(
            id=self.id,
            title=self.title,
            description=self.description,
            genres=[await genre_association.to_read_model() for genre_association in self.genres],
            country=await self.country.to_read_model(),
            studios=[await studio_association.to_read_model() for studio_association in self.studios],
        )
    

class SeasonModels(Base):
    __tablename__ = "seasons"

    id: Mapped[int] = mapped_column(primary_key=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id"))
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    season_num: Mapped[int] = mapped_column()
    series_count: Mapped[int] = mapped_column()

    movie: Mapped["MovieModels"] = relationship(
        back_populates="season"
    )

    series: Mapped["SerieModels"] = relationship(
        back_populates="season", passive_deletes=True
    )

    async def to_read_model(self):
        return SeasonShemas(**(self.__dict__))


class SerieModels(Base):
    __tablename__ = "series"

    id: Mapped[int] = mapped_column(primary_key=True)
    season_id: Mapped[int] = mapped_column(ForeignKey("seasons.id"))
    title: Mapped[int] = mapped_column()
    serie_num: Mapped[int] = mapped_column()
    serie_link: Mapped[str] = mapped_column()

    season: Mapped["SeasonModels"] = relationship(
        back_populates="series"
    )

    async def to_read_model(self):
        return SerieSchemas(**(self.__dict__))
