from utils.repository import SqlAlchemyRepository
from db.models.models import SeasonModels


class SeasonRepository(SqlAlchemyRepository):
    model = SeasonModels