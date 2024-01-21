from noxpack import mcfunction
from .utils import *


def modify_card_callout(add=False, remove=False):
    assert add or remove

    x0, y, z0 = -551, -55, 1921

    cards = [
        "stability sneak ember_seeker eerie_silence treasure_hunter chill_step moment_of_clarity pirates_booty",
        "tread_lightly - frost_focus swagger reckless_charge smash_and_grab pay_to_win adrenaline_rush",
        "evasion - nimble_looting eyes_on_the_prize - dungeon_repairs - -",
        "deep_frost quickstep brilliance - - - - stumble",
        "- loot_and_scoot - beast_sense - sprint - cash_cow",
        "- - - avalanche bounding_strides second_wind - cold_snap",
    ]

    for ix, row in enumerate(cards):
        x = x0 + 5 * ix

        for iz, name in enumerate(row.split()):
            z = z0 + iz

            if add:
                if name == "-":
                    block = unused(f"<card callout @ {x} {y} {z}>")
                elif name == "reckless_charge":
                    block = delay_sound(f"do2:audio/play/cards_{name}", 12)
                else:
                    block = sound(f"do2:cards.{name}", 177)

                yield f"setblock {x} {y} {z} {EMPTY}"
                yield f"setblock {x} {y} {z} {block}"

            if remove:
                yield f"setblock {x+1} {y-1} {z} {FILLER}"
                yield f"setblock {x+1} {y} {z} {EMPTY}"
                yield f"setblock {x+2} {y-1} {z} {EMPTY}"
                yield f"setblock {x+2} {y} {z} {EMPTY}"



def modify_difficulty(add=False, remove=False):
    assert add or remove

    x0, y, z = -557, 117, 1986
    names = ["easy", "medium", "hard", "deadly", "deepfrost"]
    condition = "if block ~ ~-3 ~ minecraft:repeater[powered=true]"

    for ix, name in enumerate(names):
        x = x0 - ix

        if add:
            block = sound(
                f"do2:interactions.difficulty.{name}", distance=20, condition=condition
            )

            yield f"setblock {x} {y} {z} {FILLER}"
            yield f"setblock {x} {y+1} {z} {block}"

        if remove:
            yield f"fill {x} {y-1} {z+2} {x} {y+1} {z+3} {EMPTY}"


def modify_events(add=False, remove=False):
    assert add or remove
    
    x0, y, z = -547, -57, 1951
    events = ["heartbeat", "clank_blocked", "hazard", "hazard_blocked"]

    if remove:
        yield f"fill {x0-1} {y} {z-3} {x0+4} {y} {z-1} {EMPTY}"

    if add:
        for ix, event in enumerate(events):
            x = x0 + ix
            block = sound(f"do2:events.{event}", 170, facing="north")
            yield f"setblock {x} {y+1} {z} {block}"
            yield f"setblock {x} {y+2} {z} minecraft:torch"


def modify_test_room(add=False, remove=False):
    assert add or remove
    
    x, y, z = -522, 122, 1983

    if add:
        block1 = sound(f"do2:events.hazard", 16)
        block2 = sound(f"do2:events.hazard_blocked", 16)
        block3 = sound(f"do2:events.clank_blocked", 16)
        block4 = sound(f"do2:events.artifact_retrived", 16)

        yield f"setblock {x+3} {y} {z} {block1}"
        yield f"setblock {x+3} {y+3} {z} {block2}"
        yield f"setblock {x} {y} {z+6} {block3}"
        yield f"setblock {x} {y} {z+8} {block4}"

    if remove:
        yield f"fill {x+3} {y+1} {z-1} {x+3} {y+2} {z-3} {EMPTY}"
        yield f"fill {x+1} {y+2} {z+1} {x+2} {y+3} {z+1} {EMPTY}"
        yield f"fill {x-1} {y+1} {z+6} {x-3} {y+2} {z+8} {EMPTY}"
