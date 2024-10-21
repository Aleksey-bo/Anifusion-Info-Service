from typing import Optional

from pydantic import BaseModel, Field


class StudioSchemas(BaseModel):
    id: Optional[int] = Field(default=None)
    studio_name: str