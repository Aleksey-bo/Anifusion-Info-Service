from repositories.genre_repository import GenreRepository
from repositories.movie_repository import MovieRepository
from core.services.genre_service import GenreService
from core.services.movie_service import MovieService


def genre_service():
    return GenreService(GenreRepository)


def movie_service():
    return MovieService(MovieRepository)