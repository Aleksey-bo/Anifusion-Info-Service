from typing import List, Annotated

from fastapi.routing import APIRouter
from fastapi import Depends, status, HTTPException

from schemas.season_schemas import SeasonShemas
from core.services.season_service import SeasonService
from api.v1.dependencies import season_dep


router = APIRouter(prefix='/season', tags=["Season"])


season_depend = Annotated[SeasonService, Depends(season_dep)]


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_season(data: SeasonShemas, season_service: season_depend) -> SeasonShemas:
    season_service = await season_service.create_handler(data=data)
    if season_service is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="")
    return season_service


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