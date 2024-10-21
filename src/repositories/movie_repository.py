from db.models.models import MovieModels
from utils.repository import SqlAlchemyRepository


class MovieRepository(SqlAlchemyRepository):
    model = MovieModels