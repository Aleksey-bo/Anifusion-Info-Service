from db.models.models import CountryModels
from utils.repository import SqlAlchemyRepository


class CountryRepository(SqlAlchemyRepository):
    model = CountryModels