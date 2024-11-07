from utils.repository import SqlAlchemyRepository
from db.models.models import SerieModels


class SerieRepository(SqlAlchemyRepository):
    model = SerieModels