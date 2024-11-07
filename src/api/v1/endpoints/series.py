from typing import List

from fastapi.routing import APIRouter
from fastapi import Depends, status, HTTPException

from schemas.serie_schemas import SerieSchemas


router = APIRouter(prefix='/series', tags=["Series"])


@router.get("/get_all/{season_id}", status_code=status.HTTP_200_OK)
async def get_all_series_for_season(season_id: int) -> List[SerieSchemas]:
    pass


@router.put("/update/{series_id}", status_code=status.HTTP_200_OK)
async def update_series(series_id: int, data: SerieSchemas) -> SerieSchemas:
    pass


@router.delete("/delete/{series_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_series(series_id: int):
    pass