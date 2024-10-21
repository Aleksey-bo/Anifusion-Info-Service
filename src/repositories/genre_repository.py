from db.models.models import Genre
from utils.repository import SqlAlchemyRepository


class GenreRepository(SqlAlchemyRepository):
    model = Genre