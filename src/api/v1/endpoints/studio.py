from typing import List

from fastapi.routing import APIRouter
from fastapi import Depends, status

from schemas.studio_schemas import StudioSchemas


router = APIRouter(prefix="/api/v1/studio", tags=["Studio"])


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_studio(data: StudioSchemas) -> StudioSchemas:
    pass


@router.get("/all", status_code=status.HTTP_200_OK)
async def get_all_studio() -> List[StudioSchemas]:
    pass


@router.get("/get/{studio_id}", status_code=status.HTTP_200_OK)
async def get_current_studio(studio_id: int) -> StudioSchemas:
    pass


@router.put("/update/{studio_id}", status_code=status.HTTP_200_OK)
async def update_studio(studio_id: int, data: StudioSchemas) -> bool:
    pass


@router.delete("/delete/{studio_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_studio(studio_id: int):
    pass