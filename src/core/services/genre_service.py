from repositories.genre_repository import GenreRepository
from .abstract.abstract_service import AbstractService
from utils.repository import AbstractRepository


class GenreService(AbstractService):
    def __init__(self, genre_repo: AbstractRepository) -> None:
        self.genre_repository: AbstractRepository = genre_repo()

    async def create_handler(self, data) -> object|None:
        try:
            genre_obj = await self.genre_repository.create(data=data.model_dump())
            return genre_obj
        except Exception:
            return None

    async def get_handler(self, genre_id) -> object|None:
        try:
            genre_obj = await self.genre_repository.get(id=genre_id)
            return genre_obj
        except Exception:
            return None

    async def get_all_handler(self) -> list|None:
        try:
            genre_list = await self.genre_repository.get_all()
            return genre_list
        except Exception:
            return None

    async def update_handler(self, genre_id, data) -> object|bool|None:
        try:
            genre_update_obj = await self.genre_repository.update(data=data, id=genre_id)
            return genre_update_obj
        except Exception:
            return None

    async def delete_handler(self, genre_id) -> bool|None:
        try:
            return await self.genre_repository.delete(id=genre_id)
        except Exception:
            return None