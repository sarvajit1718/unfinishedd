from pydantic import BaseModel, Field
from typing import List, Optional


class Scene(BaseModel):
    scene_id: int
    title: Optional[str] = None
    location: Optional[str] = None
    time_of_day: Optional[str] = None
    characters: List[str] = Field(default_factory=list)
    duration_seconds: Optional[int] = None
    weather: Optional[str] = None
    props: List[str] = Field(default_factory=list)