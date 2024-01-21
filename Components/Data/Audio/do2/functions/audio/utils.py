EMPTY = "minecraft:glass"
FILLER = "minecraft:diamond_block"


def delay_sound(function_name, delay, *, facing="south"):
    command_block = f"minecraft:command_block[facing={facing},conditional=false]"

    if delay > 0:
        command = f"schedule function {function_name} {delay}t append"
    else:
        command = f"function {function_name}"

    return f"""{command_block}{{Command: "{command}"}}"""


def sound(name, distance, *, facing="south", condition="", at=None):
    command_block = f"minecraft:command_block[facing={facing},conditional=false]"
    command = [
        "execute",
        condition,
        f"as @a[tag=do2.cmd_sound,distance=..{distance}]",
        "at @s",
        f"run playsound {name} master @s",
    ]

    if at is not None:
        command.append(at)

    command = " ".join(part for part in command if part)

    return f"""{command_block}{{Command: "{command}"}}"""


def unused(name, *, facing="south"):
    command_block = f"minecraft:command_block[facing={facing},conditional=false]"
    command = f"say Triggered unused sound system: {name}"

    return f"""{command_block}{{Command: "{command}"}}"""