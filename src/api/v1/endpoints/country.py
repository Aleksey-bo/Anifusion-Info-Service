from typing import List, Annotated

from fastapi.routing import APIRouter
from fastapi import Depends, status, HTTPException

from schemas.country_schemas import CountrySchemas
from core.services.country_service import CountryService
from api.v1.dependencies import country_dep


router = APIRouter(prefix="/country", tags=["Country"])


country_depend = Annotated[CountryService, Depends(country_dep)]


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_country(data: CountrySchemas, country_service: country_depend) -> CountrySchemas:
    country_service = await country_service.create_handler(data=data)
    if country_service is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
    return country_service


@router.get("/all", status_code=status.HTTP_200_OK)
async def get_all_country(country_service: country_depend) -> List[CountrySchemas]:
    country_service = await country_service.get_all_handler()
    if country_service is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
    return country_service


@router.get("/get/{country_id}", status_code=status.HTTP_200_OK)
async def get_current_country(contry_id: int, country_servce: country_depend) -> CountrySchemas:
    country_service = await country_servce.get_handler(country_id=contry_id)
    if country_service is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
    if country_service is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Country not found")
    return country_service


@router.put("/update/{country_id}", status_code=status.HTTP_200_OK)
async def update_country(country_id: int, data: CountrySchemas, country_service: country_depend) -> bool:
    country_service = await country_service.update_handler(country_id=country_id, data=data)
    if country_service is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
    if country_service is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Country not found")
    return country_service


@router.delete("/delete/{country_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_country(country_id: int, country_service: country_depend):
    country_service = await country_service.delete_handler(country_id=country_id)
    if country_service is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error")
    if country_service is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Country not found")
    return country_service