from typing import List, Annotated
from fastapi.routing import APIRouter
from fastapi import Depends, status, HTTPException

from schemas.movie_schemas import MovieSchemas, MovieCreateUpdate
from core.services.movie_service import MovieService
from api.v1.dependencies import movie_dep


router = APIRouter(prefix="/movie", tags=["Movie"])


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_movie(data: MovieCreateUpdate, movie_service: Annotated[MovieService, Depends(movie_dep)]):
    movie_service = await movie_service.create_handler(data=data)
    if movie_service is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server")
    return movie_service


@router.get("/all", status_code=status.HTTP_200_OK)
async def get_all_movie(movie_service: Annotated[MovieService, Depends(movie_dep)]) -> List[MovieSchemas]:
    movie_service = await movie_service.get_all_handler()
    if movie_service is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
    elif movie_service is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return movie_service


@router.get("/get/{movie_id}", status_code=status.HTTP_200_OK)
async def get_currnet_movie(movie_id: int, movie_service: Annotated[MovieService, Depends(movie_dep)]) -> MovieSchemas:
    movie_service = await movie_service.get_handler(movie_id=movie_id)
    if movie_service is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
    elif movie_service is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return movie_service


@router.put("/update/{movie_id}", status_code=status.HTTP_200_OK)
async def update_movie(movie_id: int, data: MovieCreateUpdate, movie_service: Annotated[MovieService, Depends(movie_dep)]):
    movie_service = await movie_service.update_handler(movie_id=movie_id, data=data)
    if movie_service is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
    elif movie_service is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return movie_service


@router.delete("/delete/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_movie(movie_id: int, movie_service: Annotated[MovieService, Depends(movie_dep)]):
    movie_service = await movie_service.delete_handler(movie_id=movie_id)
    if movie_service is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
    elif movie_service is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return movie_service
