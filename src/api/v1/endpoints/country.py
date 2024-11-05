from typing import List

from fastapi.routing import APIRouter
from fastapi import Depends, status

from schemas.country_schemas import CountrySchemas


router = APIRouter(prefix="/api/v1/country", tags=["Country"])


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_country(data: CountrySchemas) -> CountrySchemas:
    pass


@router.get("/all", status_code=status.HTTP_200_OK)
async def get_all_country() -> List[CountrySchemas]:
    pass


@router.get("/get/{country_id}", status_code=status.HTTP_200_OK)
async def get_current_country(contry_id: int) -> CountrySchemas:
    pass


@router.put("/update/{country_id}", status_code=status.HTTP_200_OK)
async def update_country(country_id: int, data: CountrySchemas) -> bool:
    pass


@router.delete("/delete/{country_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_country(country_id: int):
    pass