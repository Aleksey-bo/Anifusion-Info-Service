from typing import List, Optional

from pydantic import BaseModel, Field

from .genre_schemas import GenreShemas
from .studio_schemas import StudioSchemas
from .country_schemas import CountrySchemas


class MovieSchemas(BaseModel):
    id: int
    title: str
    description: str
    genres: Optional[List[GenreShemas]] = Field(default=None)
    country: Optional[CountrySchemas] = Field(default=None)
    studios: Optional[List[StudioSchemas]] = Field(default=None)

    class Config:
        from_attributes = True


class MovieCreateUpdate(BaseModel):
    title: str
    description: str
    genres: List[int]
    country_id: int
    studios: List[int]

    class Config:
        from_attributes = True
