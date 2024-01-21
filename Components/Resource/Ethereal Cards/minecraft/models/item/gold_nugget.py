from noxpack import json
import data


@json
def _():
    overrides = []

    card_list = data.CUSTOM_MODIFICATIONS.ETHEREAL_CARDS.items()
    card_list = sorted(card_list, key=lambda item: item[1]["model"])

    for name, desc in card_list:
        card_id = name.lower().replace("'", "").replace(" ", "_")
        card_id = {
            "speed_runner": "speed_run",
            "pirates_booty": "pirate_booty",
        }.get(card_id, card_id)

        overrides.append(
            {
                "predicate": {"custom_model_data": desc["model"]},
                "model": f"do2:item/ethereal_cards/{card_id}",
            }
        )

    return {
        "parent": "item/generated",
        "textures": {
            "layer0": "item/gold_nugget",
        },
        "overrides": overrides,
    }
