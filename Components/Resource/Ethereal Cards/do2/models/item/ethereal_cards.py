from noxpack import json
import copy
import data

TEXTURE_REPLACEMENTS = {
    "custom:item/do/cards/borders/normal_bane": "custom:item/do/cards/borders/normal_crown",
    "custom:item/do/cards/borders/normal_common": "custom:item/do/cards/borders/normal_crown",
    "custom:item/do/cards/borders/normal_legendary": "custom:item/do/cards/borders/normal_crown",
    "custom:item/do/cards/borders/normal_rare": "custom:item/do/cards/borders/normal_crown",
    "custom:item/do/cards/borders/normal_uncommon": "custom:item/do/cards/borders/normal_crown",
    "custom:item/do/cards/icons/card_0": "custom:item/do/cards/icons/ethereal",
    "custom:item/do/cards/icons/permanent": "custom:item/do/cards/icons/permanent_and_ethereal",
    # "custom:item/do/cards/borders/no_perm": "custom:item/do/cards/borders/no_perm",
    # "custom:item/do/cards/borders/normal_crown": "custom:item/do/cards/borders/normal_crown",
    # "custom:item/do/cards/borders/reinforced": "custom:item/do/cards/borders/reinforced",
    # "custom:item/do/cards/icons/cards1": "custom:item/do/cards/icons/cards1",
    # "custom:item/do/cards/icons/cards3": "custom:item/do/cards/icons/cards3",
    # "custom:item/do/cards/icons/cards5": "custom:item/do/cards/icons/cards5",
    # "custom:item/do/cards/icons/ethereal": "custom:item/do/cards/icons/ethereal",
    # "custom:item/do/cards/icons/permanent_and_ethereal": "custom:item/do/cards/icons/permanent_and_ethereal",
}


def _create(name, desc):
    card_id = name.lower().replace("'", "").replace(" ", "_")
    card_id = {
        "speed_runner": "speed_run",
        "pirates_booty": "pirate_booty",
    }.get(card_id, card_id)

    original_card = getattr(data.CARD_MODELS, card_id.upper()).get()

    @json(name=card_id)
    def _():
        card = copy.deepcopy(original_card)

        for key, value in list(card["textures"].items()):
            card["textures"][key] = TEXTURE_REPLACEMENTS.get(value, value)

        return card


for name, desc in data.CUSTOM_MODIFICATIONS.ETHEREAL_CARDS.items():
    _create(name, desc)
