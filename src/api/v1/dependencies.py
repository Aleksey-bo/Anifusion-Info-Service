from repositories.genre_repository import GenreRepository
from repositories.movie_repository import MovieRepository
from repositories.studio_repository import StudioRepository
from repositories.interval.interval_for_movie import IntervalMovieGenreRepository, IntervalMovieStudioRepository
from core.services.genre_service import GenreService
from core.services.movie_service import MovieService


def genre_service():
    return GenreService(GenreRepository)


def movie_service():
    return MovieService(
        movie_repo=MovieRepository,
        interval_genre_repo=IntervalMovieGenreRepository, 
        interval_studio_repo=IntervalMovieStudioRepository,
        genre_repo=GenreRepository,
        studio_repo=StudioRepository
        )