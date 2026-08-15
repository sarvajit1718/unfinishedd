from collections import defaultdict
from typing import List

from ..schemas.scene import Scene
from ..schemas.production import ProductionDay


def build_production_plan(scenes: List[Scene]) -> List[ProductionDay]:
    """
    Groups scenes by location so scenes at the same location
    can be scheduled together.
    """

    grouped = defaultdict(list)

    for scene in scenes:
        location = scene.location or "Unknown Location"
        grouped[location].append(scene)

    plan = []

    for day, (location, location_scenes) in enumerate(grouped.items(), start=1):
        scene_ids = [scene.scene_id for scene in location_scenes]

        characters = sorted(
            {
                character
                for scene in location_scenes
                for character in scene.characters
            }
        )

        estimated_minutes = sum(
            (scene.duration_seconds or 0) // 60
            for scene in location_scenes
        )

        plan.append(
            ProductionDay(
                day=day,
                location=location,
                scene_ids=scene_ids,
                characters=characters,
                estimated_minutes=estimated_minutes,
            )
        )

    return plan