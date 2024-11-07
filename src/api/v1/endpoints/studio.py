from typing import List, Annotated

from fastapi.routing import APIRouter
from fastapi import Depends, status, HTTPException

from schemas.studio_schemas import StudioSchemas
from core.services.studio_service import StudioService
from api.v1.dependencies import studio_dep


router = APIRouter(prefix="/studio", tags=["Studio"])


studio_depend = Annotated[StudioService, Depends(studio_dep)]


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_studio(data: StudioSchemas, studio_service: studio_depend) -> StudioSchemas:
    studio_service = await studio_service.create_handler(data=data)
    if studio_service is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
    return studio_service


@router.get("/all", status_code=status.HTTP_200_OK)
async def get_all_studio(studio_service: studio_depend) -> List[StudioSchemas]:
    studio_service = await studio_service.get_all_handler()
    if studio_service is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
    return studio_service


@router.get("/get/{studio_id}", status_code=status.HTTP_200_OK)
async def get_current_studio(studio_id: int, studio_service: studio_depend) -> StudioSchemas:
    studio_service = await studio_service.get_handler(studio_id=studio_id)
    if studio_service is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
    if studio_service is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Studio not found")
    return studio_service



@router.put("/update/{studio_id}", status_code=status.HTTP_200_OK)
async def update_studio(studio_id: int, data: StudioSchemas, studio_service: studio_depend) -> StudioSchemas:
    studio_service = await studio_service.update_handler(studio_id=studio_id, data=data)
    if studio_service is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
    if studio_service is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Studio not found")
    return studio_service


@router.delete("/delete/{studio_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_studio(studio_id: int, studio_service: studio_depend):
    studio_service = await studio_service.delete_handler(studio_id=studio_id)
    if studio_service is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
    if studio_service is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Studio not found")
    return studio_service