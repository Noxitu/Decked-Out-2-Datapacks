from resource_pack import json
from common import read_json

@json
def _():
    cards = read_json(f"converted_ethereal_cards.json")
    cards = {int(model): name for model, name in cards.items()}

    overrides = []

    for model in sorted(cards):
        name = cards[model]
        overrides.append({
                "predicate": {"custom_model_data": model},
                "model": f"do2:item/converted_ethereal_cards/{name}",
            })
        
    return {
        "parent": "item/generated",
        "textures": {
            "layer0": "item/gold_nugget",
        },
        "overrides": overrides,
    }
