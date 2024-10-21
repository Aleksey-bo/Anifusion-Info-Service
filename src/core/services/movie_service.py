

from .abstract.abstract_service import AbstractService
from repositories.movie_repository import MovieRepository


class MovieService(AbstractService):
    def __init__(self, movie_service: AbstractService) -> None:
        self.movie_service: AbstractService = movie_service()

    async def create_handler(self, data):
        return await MovieRepository().create(data=data.model_dump())
    
    async def get_all_handler(self):
        pass

    async def get_handler(self):
        pass

    async def update_handler(self):
        pass

    async def delete_handler(self):
        pass