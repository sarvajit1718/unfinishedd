from pydantic import BaseModel
from typing import List


class Risk(BaseModel):
    risk_id: str
    scene_id: int
    severity: str
    category: str
    description: str
    recommendation: str
    evidence: List[str]