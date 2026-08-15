from typing import List
from ..schemas.scene import Scene
from ..schemas.risk import Risk


def detect_scene_risks(scenes: List[Scene]) -> List[Risk]:
    risks = []

    for scene in scenes:
        if scene.weather and scene.weather.lower() in {"rain", "snow", "storm"}:
            risks.append(
                Risk(
                    risk_id=f"weather-{scene.scene_id}",
                    scene_id=scene.scene_id,
                    severity="medium",
                    category="weather",
                    description=f"Scene {scene.scene_id} depends on {scene.weather} weather.",
                    recommendation="Confirm weather availability or prepare a controlled backup plan.",
                    evidence=[f"Required weather: {scene.weather}"],
                )
            )

        if scene.duration_seconds and scene.duration_seconds > 300:
            risks.append(
                Risk(
                    risk_id=f"duration-{scene.scene_id}",
                    scene_id=scene.scene_id,
                    severity="low",
                    category="duration",
                    description=f"Scene {scene.scene_id} has a long estimated duration.",
                    recommendation="Review the scene for possible pacing or shooting-time issues.",
                    evidence=[f"Estimated duration: {scene.duration_seconds} seconds"],
                )
            )

    return risks