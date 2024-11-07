from typing import List

from fastapi.routing import APIRouter
from fastapi import Depends, status, HTTPException

from schemas.season_schemas import SeasonShemas


router = APIRouter(prefix='/season', tags=["Season"])


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_season(data: SeasonShemas) -> SeasonShemas:
    pass


@router.get("/get_all", status_code=status.HTTP_200_OK)
async def get_all_season(movie_id: int) -> List[SeasonShemas]:
    pass


@router.get("/get/{season_id}", status_code=status.HTTP_200_OK)
async def get_current_season(season_id: int) -> SeasonShemas:
    pass


@router.put("/update/{season_id}", status_code=status.HTTP_200_OK)
async def update_season(season_id: int, data: SeasonShemas) -> SeasonShemas:
    pass


@router.delete("/delete/{season_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_season(season_id: int):
    pass