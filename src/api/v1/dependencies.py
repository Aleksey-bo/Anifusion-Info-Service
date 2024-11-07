from repositories.genre_repository import GenreRepository
from repositories.movie_repository import MovieRepository
from repositories.studio_repository import StudioRepository
from repositories.country_repository import CountryRepository
from repositories.interval.interval_for_movie import IntervalMovieGenreRepository, IntervalMovieStudioRepository
from core.services.genre_service import GenreService
from core.services.movie_service import MovieService
from core.services.studio_service import StudioService
from core.services.country_service import CountryService


def genre_dep():
    return GenreService(
        genre_repo=GenreRepository
    )


def movie_dep():
    return MovieService(
        movie_repo=MovieRepository,
        interval_genre_repo=IntervalMovieGenreRepository, 
        interval_studio_repo=IntervalMovieStudioRepository,
        genre_repo=GenreRepository,
        studio_repo=StudioRepository
    )


def country_dep():
    return CountryService(
        country_repo=CountryRepository
    )


def studio_dep():
    return StudioService(
        studio_repo=StudioRepository
    )


def season_dep():
    pass