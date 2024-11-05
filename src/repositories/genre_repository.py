from db.models.models import GenreModels
from utils.repository import SqlAlchemyRepository


class GenreRepository(SqlAlchemyRepository):
    model = GenreModels