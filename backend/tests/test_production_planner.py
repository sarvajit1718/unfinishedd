from backend.app.schemas.scene import Scene
from backend.app.services.production_planner import build_production_plan


def test_production_plan_groups_scenes_by_location():
    scenes = [
        Scene(
            scene_id=1,
            location="Studio",
            characters=["Mira"],
            duration_seconds=120,
        ),
        Scene(
            scene_id=2,
            location="Studio",
            characters=["Mira", "Arjun"],
            duration_seconds=180,
        ),
        Scene(
            scene_id=3,
            location="Forest",
            characters=["Arjun"],
            duration_seconds=60,
        ),
    ]

    plan = build_production_plan(scenes)

    assert len(plan) == 2

    studio_day = plan[0]

    assert studio_day.location == "Studio"
    assert studio_day.scene_ids == [1, 2]
    assert studio_day.characters == ["Arjun", "Mira"]
    assert studio_day.estimated_minutes == 5