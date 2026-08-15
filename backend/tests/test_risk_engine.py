from backend.app.schemas.scene import Scene
from backend.app.services.risk_engine import detect_scene_risks


def test_weather_risk():
    scenes = [
        Scene(
            scene_id=14,
            location="Forest",
            weather="rain",
        )
    ]

    risks = detect_scene_risks(scenes)

    assert len(risks) == 1
    assert risks[0].category == "weather"
    assert risks[0].scene_id == 14