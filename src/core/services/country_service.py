from core.services.abstract.abstract_service import AbstractService
from utils.repository import AbstractRepository


class CountryService(AbstractService):
    def __init__(self, country_repo: AbstractRepository) -> None:
        self.country_repository = country_repo()

    async def create_handler(self, data):
        try:
            return await self.country_repository.create(data=data)
        except Exception:
            return None

    async def get_all_handler(self):
        try:
            return await self.country_repository.get_all()
        except Exception:
            return None

    async def get_handler(self, country_id):
        try:
            return await self.country_repository.get(id=country_id)
        except Exception:
            return None

    async def update_handler(self, country_id, data):
        try:
            return await self.country_repository.update(data=data, id=country_id)
        except Exception:
            return None

    async def delete_handler(self, country_id):
        try:
            return await self.country_repository.delete(id=country_id)
        except Exception:
            return None