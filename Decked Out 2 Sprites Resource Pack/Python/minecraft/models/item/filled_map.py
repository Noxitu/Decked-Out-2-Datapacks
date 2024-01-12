from resource_pack import json


@json
def _():
    return {
        "parent": "item/generated",
        "textures": {
            "layer0": "item/filled_map",
            "layer1": "item/filled_map_markings",
        },
        "overrides": [
            {
                "predicate": {"custom_model_data": 201},
                "model": "do2:item/gui_map",
            }
        ],
    }
