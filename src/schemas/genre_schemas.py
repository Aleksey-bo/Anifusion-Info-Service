from typing import Optional

from pydantic import BaseModel, Field


class GenreShemas(BaseModel):
    id: Optional[int] = Field(default=None)
    genre_name: str

    class Config:
        from_attributes = True