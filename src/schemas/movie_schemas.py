from typing import List

from pydantic import BaseModel

from .genre_schemas import GenreShemas


class MovieSchemas(BaseModel):
    id: int
    title: str
    description: str
    genre: List[GenreShemas]

    class Config:
        from_attributes = True


class MovieCreateUpdate(BaseModel):
    title: str
    description: str
    genres: List[int]

    class Config:
        from_attributes = True

