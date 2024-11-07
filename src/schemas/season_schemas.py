from typing import Optional

from pydantic import BaseModel, Field


class SeasonShemas(BaseModel):
    id: Optional[int] = Field(default=None)
    title: str
    description: str
    season_num: int
    series_count: int
