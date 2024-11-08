import functools
from core.services.abstract.abstract_service import AbstractService
from utils.repository import AbstractRepository
from datetime import datetime


def async_timing_decorator(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = await func(*args, **kwargs)
        end_time = datetime.now()
        print(f"Function {func.__name__} executed in {end_time - start_time} seconds")
        return result
    return wrapper


class MovieService(AbstractService):
    def __init__(self, 
                 movie_repo: AbstractRepository,
                 interval_genre_repo: AbstractRepository,
                 interval_studio_repo: AbstractRepository, 
                 studio_repo: AbstractRepository,
                 genre_repo: AbstractRepository
                 ) -> None:
        self.movie_repository = movie_repo()
        self.interval_genre_repository = interval_genre_repo()
        self.interval_studio_repository = interval_studio_repo()
        self.studio_repository = studio_repo()
        self.genre_repository = genre_repo()

    @async_timing_decorator
    async def create_handler(self, data) -> object|None:
        try:
            movie_obj = await self.movie_repository.create(
                data=data.model_dump(exclude=("genres", "studios"))
                )
            movie_obj = await movie_obj.to_read_model()
                    
            for genre_id in data.genres:
                genre_obj = await self.genre_repository.get(id=genre_id)
                if genre_obj:
                    await self.interval_genre_repository.create(
                        data={
                                "movie_id": movie_obj.id, 
                                "genre_id": genre_obj.id
                            }
                            )
                    movie_obj.genres.append(genre_obj)

            for studio_id in data.studios:
                studio_obj = await self.studio_repository.get(id=studio_id)
                if studio_obj:
                    await self.interval_studio_repository.create(
                        data={
                                "movie_id": movie_obj.id, 
                                "studio_id": studio_obj.id
                            }
                            )
                    movie_obj.studios.append(studio_obj)

            return movie_obj
        except Exception:
            return None
    
    async def get_all_handler(self) -> list|None:
        try:
            movie_obj_list = await self.movie_repository.get_all()
            return movie_obj_list
        except Exception:
            return None

    async def get_handler(self, movie_id: int) -> object|None:
        try:
            movie_obj = await self.movie_repository.get(id=movie_id)
            return movie_obj
        except Exception:
            return None

    @async_timing_decorator
    async def update_handler(self, movie_id, data) -> object|None:
            movie_obj_update = await self.movie_repository.update(
                data=data.model_dump(exclude=("id", "genres", "studios")), 
                id=movie_id
                )
            movie_obj_update = await movie_obj_update.to_read_model()
            
            if data.genres:
                for genre_id in data.genres:
                    genre_obj = await self.genre_repository.get(id=genre_id)
                    movie_genre_association = await self.interval_genre_repository.get(
                            movie_id=movie_obj_update.id, genre_id=genre_obj.id
                        )
                    if genre_obj and movie_genre_association:
                        await self.interval_genre_repository.update(
                            data={
                                "movie_id": movie_obj_update.id, 
                                "genre_id": genre_obj.id
                            }, 
                            movie_id=movie_obj_update.id, 
                            genre_id=movie_obj_update.genres[data.genres.index(genre_id)].id
                        )
                    else:
                        await self.interval_genre_repository.create(
                            data={
                                "movie_id": movie_obj_update.id,
                                "genre_id": genre_obj.id
                            }
                        )

                    movie_obj_update.genres.append(genre_obj)
            
            if data.studios:
                for studio_id in data.studios:
                    studio_obj = await self.studio_repository.get(id=studio_id)
                    movie_studio_association = await self.interval_studio_repository.get(
                        movie_id=movie_obj_update.id, studio_id=studio_id
                    )
                    if studio_obj and movie_studio_association:
                        await self.interval_studio_repository.update(
                            data={
                                "movie_id": movie_obj_update.id,
                                "studio_id": studio_obj.id
                            }, 
                            movie_id=movie_obj_update.id,
                            studio_id=movie_obj_update.studios[studio_id]["id"]
                            )
                    else:
                        await self.interval_studio_repository.create(
                            data={
                                "movie_id": movie_obj_update.id,
                                "studio_id": studio_id
                            }
                            )

                    movie_obj_update.studios.append(studio_obj)

            return movie_obj_update

    async def delete_handler(self, movie_id: int) -> bool|None:
        try:
            movie_obj = await self.movie_repository.delete(id=movie_id)
            return movie_obj
        except Exception:
            return None