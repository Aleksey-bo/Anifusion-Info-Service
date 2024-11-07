from typing import Optional

from pydantic import BaseModel, Field


class SerieSchemas(BaseModel):
    id: Optional[int] = Field(default=None)
    season_id: int
    title: str
    serie_num: int
    serie_link: Optional[str] = Field(default=None)