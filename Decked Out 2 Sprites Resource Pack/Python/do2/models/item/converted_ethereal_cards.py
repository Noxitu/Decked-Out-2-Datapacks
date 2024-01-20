from common import read_json
from resource_pack import json


TEXTURE_REPLACEMENTS = {
    # "custom:item/do/cards/borders/no_perm": "custom:item/do/cards/borders/no_perm",
    "custom:item/do/cards/borders/normal_bane": "custom:item/do/cards/borders/normal_crown",
    "custom:item/do/cards/borders/normal_common": "custom:item/do/cards/borders/normal_crown",
    # "custom:item/do/cards/borders/normal_crown": "custom:item/do/cards/borders/normal_crown",
    "custom:item/do/cards/borders/normal_legendary": "custom:item/do/cards/borders/normal_crown",
    "custom:item/do/cards/borders/normal_rare": "custom:item/do/cards/borders/normal_crown",
    "custom:item/do/cards/borders/normal_uncommon": "custom:item/do/cards/borders/normal_crown",
    # "custom:item/do/cards/borders/reinforced": "custom:item/do/cards/borders/reinforced",
    "custom:item/do/cards/icons/card_0": "custom:item/do/cards/icons/ethereal",
    # "custom:item/do/cards/icons/cards1": "custom:item/do/cards/icons/cards1",
    # "custom:item/do/cards/icons/cards3": "custom:item/do/cards/icons/cards3",
    # "custom:item/do/cards/icons/cards5": "custom:item/do/cards/icons/cards5",
    # "custom:item/do/cards/icons/ethereal": "custom:item/do/cards/icons/ethereal",
    "custom:item/do/cards/icons/permanent": "custom:item/do/cards/icons/permanent_and_ethereal",
    # "custom:item/do/cards/icons/permanent_and_ethereal": "custom:item/do/cards/icons/permanent_and_ethereal",
}


def _create_card(name):
    @json(name=name)
    def _():
        card = read_json(f"OrigCards/{name}.json")

        for key, value in list(card["textures"].items()):
            card["textures"][key] = TEXTURE_REPLACEMENTS.get(value, value)

        return card


cards = read_json(f"converted_ethereal_cards.json")

for name in cards.values():
    if not name.startswith("-"):
        _create_card(name)
