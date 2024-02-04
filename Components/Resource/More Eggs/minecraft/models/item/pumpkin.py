from noxpack import json
import data


@json
def _():
    overrides = []

    for name, model in data.CUSTOM_MODIFICATIONS.MORE_EGGS.MODELS.items():
        overrides.append(
            {
                "predicate": {"custom_model_data": model},
                "model": f"do2:item/eggs/{name}",
            }
        )

    return {
        "parent": "minecraft:block/pumpkin",
        "overrides": overrides,
    }
