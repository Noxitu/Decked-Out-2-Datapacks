from noxpack import mcfunction
import data
from .utils import EMPTY, FILLER, delay_sound, sound
from .modify_complex_systems import *


@mcfunction
def remove_old_systems():
    yield from modify_card_callout(remove=True)
    yield from modify_difficulty(remove=True)
    yield from modify_events(remove=True)
    yield from modify_test_room(remove=True)

    for systems in data.SOUNDSYSTEMS.Items:
        for desc in systems:
            remove_list = desc.get("remove", [])

            if not isinstance(remove_list, list):
                remove_list = [remove_list]

            for remove_item in remove_list:
                if isinstance(remove_item, str):
                    remove_item = {"area": remove_item}

                area = remove_item["area"]
                block = remove_item.get("block", EMPTY)

                if block == "FILLER":
                    block = FILLER

                if len(area.split()) == 3:
                    cmd = "setblock"
                else:
                    cmd = "fill"

                yield f"""{cmd} {area} {block}"""


@mcfunction
def add_command_blocks():
    yield from modify_card_callout(add=True)
    yield from modify_difficulty(add=True)
    yield from modify_events(add=True)
    yield from modify_test_room(add=True)

    for systems in data.SOUNDSYSTEMS.Items:
        for desc in systems:
            if "delay" in desc:
                command_block = delay_sound(
                    f"""do2:audio/play/{desc["id"]}""", desc["delay"]
                )
            else:
                kwargs = {}
                if "at" in desc:
                    kwargs["at"] = desc["at"]

                command_block = sound(f"""do2:{desc["sound"]}""", desc["range"])

            yield f"""setblock {desc["command_block"]} {FILLER}"""
            yield f"""setblock {desc["command_block"]} {command_block}"""
