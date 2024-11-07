from core.services.abstract.abstract_service import AbstractService
from utils.repository import AbstractRepository


class StudioService(AbstractService):
    def __init__(self, studio_repo: AbstractRepository) -> None:
        self.studio_repository = studio_repo()

    async def create_handler(self, data):
        try:
            return await self.studio_repository.create(data=data.model_dump())
        except Exception:
            return None

    async def get_all_handler(self):
        try:
            return await self.studio_repository.get_all()
        except Exception:
            return None

    async def get_handler(self, studio_id):
        try:
            return await self.studio_repository.get(id=studio_id)
        except Exception:
            return None

    async def update_handler(self, studio_id, data):
        try: 
            return await self.studio_repository.update(data=data.model_dump(exclude=("id")), id=studio_id)
        except Exception:
            return None

    async def delete_handler(self, studio_id):
        try:
            return await self.studio_repository.delete(id=studio_id)
        except Exception:
            return None