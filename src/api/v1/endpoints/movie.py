from typing import List, Annotated
from fastapi.routing import APIRouter
from fastapi import Depends, status

from schemas.movie_schemas import MovieSchemas, MovieCreateUpdate
from core.services.movie_service import MovieService
from api.v1.dependencies import movie_service


router = APIRouter(prefix="/api/v1/movie", tags=["Movie"])


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_movie(data: MovieCreateUpdate, movie_service: Annotated[MovieService, Depends(movie_service)]) -> MovieSchemas:
    movie_service = await movie_service.create_handler(data=data)
    return movie_service


@router.get("/all", status_code=status.HTTP_200_OK)
async def get_all_movie() -> List[MovieSchemas]:
    pass


@router.get("/get/{movie_id}", status_code=status.HTTP_200_OK)
async def get_currnet_movie(movie_id: int, movie_service: Annotated[MovieService, Depends(movie_service)]) -> MovieSchemas:
    pass


@router.put("/update/{movie_id}", status_code=status.HTTP_200_OK)
async def update_movie(movie_id: int, movie_service: Annotated[MovieService, Depends(movie_service)]) -> MovieSchemas:
    pass


@router.delete("/delete/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_movie(movie_id: int, movie_service: Annotated[MovieService, Depends(movie_service)]):
    pass
