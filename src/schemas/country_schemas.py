from typing import Optional

from pydantic import BaseModel, Field


class CountrySchemas(BaseModel):
    id: Optional[int] = Field(default=None)
    country_name: str