from repositories.genre_repository import GenreRepository
from .abstract.abstract_service import AbstractService
from utils.repository import AbstractRepository


class GenreService(AbstractService):
    def __init__(self, genre_repo: AbstractRepository) -> None:
        self.genre_repository: AbstractRepository = genre_repo()

    async def create_handler(self, data):
        return await GenreRepository().create(data=data)

    async def get_handler(self, genre_id):
        return await GenreRepository().get(id=genre_id)

    async def get_all_handler(self):
        return await GenreRepository().get_all()

    async def update_handler(self, genre_id, data):
        return await GenreRepository().update(data=data, id=genre_id)

    async def delete_handler(self, genre_id):
        return await GenreRepository().delete(id=genre_id)