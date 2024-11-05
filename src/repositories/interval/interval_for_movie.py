from utils.repository import SqlAlchemyRepository
from db.models.models import MovieGenreAssociation, MovieStudioAssociation


class IntervalMovieGenreRepository(SqlAlchemyRepository):
    model = MovieGenreAssociation


class IntervalMovieStudioRepository(SqlAlchemyRepository):
    model = MovieStudioAssociation