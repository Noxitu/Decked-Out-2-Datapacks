from noxpack import mcfunction
import data
from .util import cards, card_display_name, card_model


STORAGE = "storage do2:deck_validation"



@mcfunction(tags=["do2:deck_validation/add_card_ids"])
def _():
    for name in cards():
        model = card_model(name)
        display_name = card_display_name(name)
        display_name = display_name.replace("'", "\\'")

        card_info = data.CARD_INFO[name]

        selector = f"""Deck[{{
                "id": "minecraft:gold_nugget",
                "tag": {{
                    CustomModelData: {model},
                    display: {{
                        Name: '{display_name}'
                    }}
                }}
            }}]"""

        yield f"""
            execute if data {STORAGE} {selector}
                    run data modify {STORAGE} {selector}.CardId
                        set value {card_info["id"]}
            """
