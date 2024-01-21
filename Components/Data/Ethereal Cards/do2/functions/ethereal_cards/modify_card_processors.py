from noxpack import mcfunction
import data
from .util import card_nbt
from .process_card import _ as process_card

class Permanent:
    POS = -544, 40, 1913
    CARDS = "Speed Runner,-,-,-,Fuzzy Bunny Slippers,-,-,-,Silent Runner,-,-,Suit Up,-,-,-"


class NormalCards:
    POS = -570, 36, 1917
    X_LAST = -617
    CARDS = (
        "-,-,-,Eerie Silence,-,Chill Step,-,Pirate's Booty,Tread Lightly,-,Frost Focus,Swagger,"
        "Reckless Charge,Smash and Grab,-,Adrenaline Rush,Evasion,-,Nimble Looting,Eyes on the Prize,"
        "-,Dungeon Repairs,-,-,Deepfrost,Quickstep,Brilliance,-,-,-,-,-,-,Loot and Scoot,-,"
        "Beast Sense,-,Sprint,-,-,-,-,-,-,Bounding Strides,Second Wind,-,Cold Snap"
    )

FILTER_FILLER = {"id": "minecraft:iron_nugget", "tag": {"display": {"Name": "Filter Filler!"}}}


def _reschedule_if_not_loaded():
    yield f"schedule function {_} 16s replace"

    x, y, z = Permanent.POS
    yield f"execute unless loaded {x} {y} {z} run return 0"

    x, (y, z) = NormalCards.X_LAST, NormalCards.POS[1:]

    yield f"execute unless loaded {x} {y} {z} run return 0"

    yield f"schedule clear {_}"


def _nbt(data, *, slot=None, count=None):
    if isinstance(data, bool):
        return "1b" if data else "0b"

    if isinstance(data, str):
        text = data.replace("'", "\\'")
        return f"'{text}'"

    if isinstance(data, list):
        return "[" + ",".join(_nbt(item) for item in data) + "]"

    if isinstance(data, dict):
        items = [f"{key}: {_nbt(item)}" for key, item in data.items()]
        
        if count is not None:
            items.append(f"Count: {count}b")  

        if slot is not None:
            items.append(f"Slot: {slot}b")

        return "{" + ",".join(items) + "}"

    return str(data)

@mcfunction(tags=["minecraft:load"])
def _():
    yield from _reschedule_if_not_loaded()

    for category in [Permanent, NormalCards]:
        x0, y, z = category.POS

        for i, name in enumerate(category.CARDS.split(",")):
            if name == "-":
                continue

            x = x0 - i

            card = data.NBT.CARDS[name]

            yield f"""
                data modify block {x} {y} {z} Items
                    set value [
                        {_nbt(card, slot=0, count=1)},
                        {card_nbt(name, slot=1, count=1)},
                        {_nbt(FILTER_FILLER, slot=2, count=18)},
                        {_nbt(FILTER_FILLER, slot=3, count=1)},
                        {_nbt(FILTER_FILLER, slot=4, count=1)}
                    ]
                """

            block_pos = f"{x} {y-2} {z+3}"
            yield f"""setblock {block_pos} minecraft:quartz_block"""
            block_pos = f"{x} {y-3} {z+3}"
            yield f"""setblock {block_pos} minecraft:glass"""
            yield f"""setblock {block_pos} minecraft:command_block{{
                        Command: "function {process_card}"
                }}"""
