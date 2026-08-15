from pydantic import BaseModel
from typing import List

from .scene import Scene


class Project(BaseModel):
    project_id: str
    name: str
    scenes: List[Scene]
    