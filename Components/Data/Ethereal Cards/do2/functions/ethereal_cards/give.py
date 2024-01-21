from noxpack import mcfunction
from .util import COLOR, ETHEREAL, cards, card_nbt


SHULKER_NAME = f"""{{"text": "{ETHEREAL} Ethereal Cards DLC {ETHEREAL}", "color": "{COLOR}"}}"""


@mcfunction
def _():
    items = []
    for slot, name in enumerate(cards()):
        items.append(card_nbt(name, count=64, slot=slot))

    yield f"""give @a minecraft:yellow_shulker_box{{
        BlockEntityTag: {{
            Items: [{','.join(items)}]
        }},
        display: {{
            Name: '{SHULKER_NAME}'
        }}
    }}"""