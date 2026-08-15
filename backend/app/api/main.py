from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from ..schemas.project import Project

from ..schemas.scene import Scene
from ..services.risk_engine import detect_scene_risks
from ..services.production_planner import build_production_plan

app = FastAPI(title="CutWise API")


class SceneRequest(BaseModel):
    scenes: List[Scene]


@app.get("/")
def health_check():
    return {"status": "ok", "service": "CutWise API"}


@app.post("/risks")
def analyze_risks(request: SceneRequest):
    risks = detect_scene_risks(request.scenes)
    return {"risks": risks}


@app.post("/production-plan")
def production_plan(request: SceneRequest):
    plan = build_production_plan(request.scenes)
    return {"plan": plan}

@app.post("/analyze")
def analyze_project(project: Project):
    risks = detect_scene_risks(project.scenes)
    plan = build_production_plan(project.scenes)

    return {
        "project_id": project.project_id,
        "project_name": project.name,
        "scene_count": len(project.scenes),
        "risks": risks,
        "production_plan": plan,
    }