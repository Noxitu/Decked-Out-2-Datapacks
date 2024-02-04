from noxpack import json
from .dungeon_logs import paper_list


@json(path="minecraft/models/item/paper")
def _():
    overrides = []

    for idx, name in enumerate(paper_list()):
        overrides.append(
            {
                "predicate": {"custom_model_data": idx + 1},
                "model": f"do2:item/dungeon_log/paper_{name}",
            }
        )

    return {
        "parent": "item/generated",
        "textures": {
            "layer0": "item/paper",
        },
        "overrides": overrides,
    }
