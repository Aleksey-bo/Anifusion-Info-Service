from typing import List, Annotated
from fastapi.routing import APIRouter
from fastapi import Depends, status

from repositories.genre_repository import GenreRepository
from core.services.genre_service import GenreService
from schemas.genre_schemas import GenreShemas
from api.v1.dependencies import genre_service


router = APIRouter(prefix='/api/v1/genre', tags=["Genre"])


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_genre(data: GenreShemas) -> GenreShemas:
    genre_obj = await GenreRepository().create(data=data.model_dump())
    return genre_obj


@router.get("/all", status_code=status.HTTP_200_OK)
async def get_all_genre() -> List[GenreShemas]:
    genre_list_obj = await GenreRepository().get_all()
    return genre_list_obj

@router.get("/get/{genre_id}", status_code=status.HTTP_200_OK)
async def get_current_genre(genre_id: int, genre_service: Annotated[GenreService, Depends(genre_service)]) -> GenreShemas:
    genre_service = await genre_service.get_handler(genre_id=genre_id)
    return genre_service


@router.put("/update/{genre_id}", status_code=status.HTTP_200_OK)
async def update_genre(genre_id: int, data: GenreShemas) -> bool:
    genre_obj = await GenreRepository().update(data=data.model_dump(exclude_none=True), id=genre_id)
    return genre_obj


@router.delete("/delete/{genre_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(genre_id: int):
    genre_obj = await GenreRepository().delete(id=genre_id)
    return genre_obj