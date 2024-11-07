from typing import List, Annotated
from fastapi.routing import APIRouter
from fastapi import Depends, status

from core.services.genre_service import GenreService
from schemas.genre_schemas import GenreShemas
from api.v1.dependencies import genre_dep


router = APIRouter(prefix='/genre', tags=["Genre"])

genre_depend = Annotated[GenreService, Depends(genre_dep)]


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_genre(data: GenreShemas, genre_service: genre_depend) -> GenreShemas:
    genre_obj = await genre_service.create_handler(data=data)
    return genre_obj


@router.get("/all", status_code=status.HTTP_200_OK)
async def get_all_genre(genre_service: genre_depend) -> List[GenreShemas]:
    genre_list_obj = await genre_service.get_all_handler()
    return genre_list_obj

@router.get("/get/{genre_id}", status_code=status.HTTP_200_OK)
async def get_current_genre(genre_id: int, genre_service: genre_depend) -> GenreShemas:
    genre_service = await genre_service.get_handler(genre_id=genre_id)
    return genre_service


@router.put("/update/{genre_id}", status_code=status.HTTP_200_OK)
async def update_genre(genre_id: int, data: GenreShemas, genre_service: genre_depend) -> GenreShemas:
    genre_obj = await genre_service.update_handler(data=data.model_dump(exclude_none=True), genre_id=genre_id)
    return genre_obj


@router.delete("/delete/{genre_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(genre_id: int, genre_service: genre_depend):
    genre_obj = await genre_service.delete_handler(genre_id=genre_id)
    return genre_obj