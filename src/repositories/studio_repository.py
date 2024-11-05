from utils.repository import SqlAlchemyRepository
from db.models.models import StudioModels


class StudioRepository(SqlAlchemyRepository):
    model = StudioModels