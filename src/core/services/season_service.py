from core.services.abstract.abstract_service import AbstractService
from utils.repository import AbstractRepository


class SeasonService(AbstractService):
    def __init__(
            self,
            season_repo: AbstractRepository
            ) -> None:
        self.season_repository = season_repo()

    async def create_handler(self, data):
        try:
            return await self.season_repository.create(
                data=data.dump_model(
                    exclude=("id")
                )
            )
        except Exception:
            return None

    async def get_all_handler(self):
        try:
            return await self.season_repository.get_all()
        except Exception:
            return None

    async def get_handler(self, movie_id):
        try:
            return await self.season_repository.get(
                movie_id=movie_id
            )
        except Exception:
            return None

    async def update_handler(self, season_id, data):
        try:
            return await self.season_repository.update(
                data=data.dump_model(
                    exclude=("id")
                ),
                id=season_id
            )
        except Exception:
            return None

    async def delete_handler(self, season_id):
        try:
            return await self.season_repository.delete(
                id=season_id
            )
        except Exception:
            return None