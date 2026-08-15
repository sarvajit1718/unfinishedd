from pydantic import BaseModel, Field
from typing import List


class ProductionDay(BaseModel):
    day: int
    location: str
    scene_ids: List[int] = Field(default_factory=list)
    characters: List[str] = Field(default_factory=list)
    estimated_minutes: int = 0