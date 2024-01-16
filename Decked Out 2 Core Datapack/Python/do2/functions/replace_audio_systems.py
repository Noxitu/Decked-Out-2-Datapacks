from mcfunction import mcfunction

AIR = "minecraft:air"
FILLER = "minecraft:diamond_block"


REMOVE_OLD_SYSTEM = True


def sound(name, distance, *, facing="south", condition="", at=None):
    command_block = f"minecraft:command_block[facing={facing},conditional=false]"
    command = [
        "execute",
        condition,
        f"as @a[distance=..{distance}]",
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


@mcfunction(tags=["do2:replace_audio_systems"])
def replace_artifact_pickup():
    x, y, z = -525, -31, 1936
    block = sound(f"do2:events.artifact_retrived", 220)

    yield f"setblock {x} {y} {z} {block}"

    if REMOVE_OLD_SYSTEM:
        yield f"fill {x} {y} {z+1} {x} {y+2} {z+4} {AIR}"


@mcfunction(tags=["do2:replace_audio_systems"])
def replace_card_callout():
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

            if name == "-":
                block = unused(f"<card callout @ {x} {y} {z}>")
            else:
                block = sound(f"do2:cards.{name}", 177)

            yield f"setblock {x} {y} {z} {block}"

            if REMOVE_OLD_SYSTEM:
                yield f"setblock {x+1} {y-1} {z} {FILLER}"
                yield f"setblock {x+1} {y} {z} {AIR}"
                yield f"setblock {x+2} {y-1} {z} {AIR}"
                yield f"setblock {x+2} {y} {z} {AIR}"


@mcfunction(tags=["do2:replace_audio_systems"])
def replace_card_reveal_left():
    x, y, z = -627, -25, 2004
    block = sound(f"do2:events.card_reveal", 32)

    yield f"setblock {x} {y} {z} {block}"

    if REMOVE_OLD_SYSTEM:
        yield f"fill {x} {y+1} {z+1} {x-2} {y+2} {z+2} {AIR}"
        yield f"setblock {x} {y+2} {z} {AIR}"

@mcfunction(tags=["do2:replace_audio_systems"])
def replace_card_reveal_right():
    x, y, z = -648, -24, 2002
    block = sound(f"do2:events.card_reveal", 32)

    yield f"setblock {x} {y} {z} {block}"

    if REMOVE_OLD_SYSTEM:
        yield f"fill {x+1} {y} {z-1} {x+3} {y+1} {z-2} {AIR}"
        yield f"setblock {x+1} {y+1} {z} {AIR}"


@mcfunction(tags=["do2:replace_audio_systems"])
def replace_cave_gust():
    x, y, z = -537, -59, 1919
    block = sound(f"do2:ambient.cave_gust", 176)

    yield f"setblock {x} {y} {z} {block}"

    if REMOVE_OLD_SYSTEM:
        yield f"fill {x-2} {y} {z-2} {x-1} {y+1} {z+2} {AIR}"
        yield f"setblock {x} {y+1} {z} {AIR}"


@mcfunction(tags=["do2:replace_audio_systems"])
def replace_difficulty():
    x0, y, z = -557, 117, 1986
    names = ["easy", "medium", "hard", "deadly", "deepfrost"]
    condition = "if block ~ ~-3 ~ minecraft:repeater[powered=true]"

    for ix, name in enumerate(names):
        x = x0 - ix
        block = sound(
            f"do2:interactions.difficulty.{name}", distance=20, condition=condition
        )

        yield f"setblock {x} {y} {z} {FILLER}"
        yield f"setblock {x} {y+1} {z} {block}"

        if REMOVE_OLD_SYSTEM:
            yield f"fill {x} {y-1} {z+2} {x} {y+1} {z+3} {AIR}"


@mcfunction(tags=["do2:replace_audio_systems"])
def replace_drone():
    x, y, z = -533, -57, 1915
    block = sound(f"do2:ambient.drone", 179)

    yield f"setblock {x} {y} {z} {block}"

    if REMOVE_OLD_SYSTEM:
        yield f"fill {x+1} {y-2} {z} {x-2} {y-1} {z+4} {AIR}"
        yield f"fill {x} {y} {z+2} {x-2} {y+1} {z+4} {AIR}"


@mcfunction(tags=["do2:replace_audio_systems"])
def replace_drone_deepfrost():
    x, y, z = -531, -57, 1912
    block = sound(f"do2:ambient.drone_deepfrost", 176)

    yield f"setblock {x} {y} {z} {block}"

    if REMOVE_OLD_SYSTEM:
        yield f"setblock {x} {y} {z-1} {AIR}"
        yield f"fill {x} {y-2} {z-1} {x+4} {y-1} {z+2} {AIR}"
        yield f"fill {x+2} {y} {z} {x+4} {y} {z+2} {AIR}"


@mcfunction(tags=["do2:replace_audio_systems"])
def replace_dungeon_door_open():
    x, y, z = -621, 44, 1953
    block = sound(f"do2:interactions.dungeon_door_open", 20)

    yield f"fill {x} {y} {z+1} {x} {y} {z+3} minecraft:repeater[delay=4,facing=north]"
    yield f"setblock {x} {y} {z+4} {block}"

    if REMOVE_OLD_SYSTEM:
        yield f"fill {x-2} {y} {z} {x-2} {y-1} {z-2} {AIR}"



@mcfunction(tags=["do2:replace_audio_systems"])
def replace_dungeon_is_ready():
    x, y, z = -539, 116, 1968
    block = sound(f"do2:events.dungeon_is_ready", 100)

    yield f"setblock {x} {y} {z} {block}"

    if REMOVE_OLD_SYSTEM:
        yield f"fill {x+1} {y} {z-1} {x+5} {y+3} {z-1} {AIR}"

@mcfunction(tags=["do2:replace_audio_systems"])
def replace_dungeon_taunt():
    x, y, z = -644, -19, 1988
    block = sound(f"do2:interactions.dungeon_taunt", 50)

    yield f"setblock {x} {y} {z} {block}"

    if REMOVE_OLD_SYSTEM:
        yield f"fill {x-1} {y-2} {z+1} {x} {y} {z+3} {AIR}"


@mcfunction(tags=["do2:replace_audio_systems"])
def replace_ember_shop_open():
    x, y, z = -629, -20, 1987
    block = sound(f"do2:interactions.ember_shop_open", 50)

    yield f"setblock {x} {y} {z} {block}"

    if REMOVE_OLD_SYSTEM:
        yield f"fill {x+1} {y-1} {z-2} {x+1} {y+1} {z} {AIR}"

@mcfunction(tags=["do2:replace_audio_systems"])
def replace_ember_shop_opening():
    x, y, z = -643, -22, 1981
    block = sound(f"do2:interactions.ember_shop_opening", 50)

    yield f"setblock {x} {y} {z} {block}"

    if REMOVE_OLD_SYSTEM:
        yield f"setblock -644 -21 1980 minecraft:barrel"



@mcfunction(tags=["do2:replace_audio_systems"])
def replace_event_sounds():
    x0, y, z = -547, -57, 1951
    events = ["heartbeat", "clank_blocked", "hazard", "hazard_blocked"]

    if REMOVE_OLD_SYSTEM:
        yield f"fill {x0-1} {y} {z-3} {x0+4} {y} {z-1} {AIR}"

    for ix, event in enumerate(events):
        x = x0 + ix
        block = sound(f"do2:events.{event}", 170, facing="north")
        yield f"setblock {x} {y+1} {z} {block}"
        yield f"setblock {x} {y+2} {z} minecraft:torch"


@mcfunction(tags=["do2:replace_audio_systems"])
def replace_game_over():
    x, y, z = -551, 119, 1970
    block = sound(f"do2:events.game_over", 48)

    yield f"setblock {x} {y} {z} {block}"

    if REMOVE_OLD_SYSTEM:
        yield f"fill {x-2} {y} {z+1} {x-1} {y+2} {z+1} {AIR}"


@mcfunction(tags=["do2:replace_audio_systems"])
def replace_install_deck():
    x, y, z = -569, 114, 1979
    block = sound(f"do2:interactions.install_deck", 20)

    yield f"setblock {x} {y} {z} {block}"

    if REMOVE_OLD_SYSTEM:
        yield f"fill {x-1} {y-1} {z+1} {x} {y+1} {z+4} {AIR}"


@mcfunction(tags=["do2:replace_audio_systems"])
def replace_open_level04():
    x, y, z = -637, -20, 1894
    block = sound(f"do2:events.deepfrost_tnt", 64)

    yield f"setblock {x} {y} {z} {block}"

    if REMOVE_OLD_SYSTEM:
        yield f"fill {x+1} {y-1} {z} {x+3} {y+1} {z} {AIR}"


@mcfunction(tags=["do2:replace_audio_systems"])
def replace_open_main_door():
    x, y, z = -539, 109, 1977
    block = sound(f"do2:interactions.open_main_door", 32, at="-543 114 1980")

    yield f"setblock {x} {y} {z} {block}"

    if REMOVE_OLD_SYSTEM:
        yield f"fill {x} {y} {z+1} {x} {y+1} {z+2} {AIR}"


@mcfunction(tags=["do2:replace_audio_systems"])
def replace_take_your_items():
    x, y, z = -547, 119, 1992
    block = sound(f"do2:interactions.take_your_items", 32)

    yield f"setblock {x} {y} {z} {block}"

    if REMOVE_OLD_SYSTEM:
        yield f"fill {x-3} {y-1} {z+1} {x+1} {y} {z+1} {AIR}"


@mcfunction(tags=["do2:replace_audio_systems"])
def replace_test_room():
    x, y, z = -522, 122, 1983
    block1 = sound(f"do2:events.hazard", 16)
    block2 = sound(f"do2:events.hazard_blocked", 16)
    block3 = sound(f"do2:events.clank_blocked", 16)
    block4 = sound(f"do2:events.artifact_retrived", 16)

    yield f"setblock {x+3} {y} {z} {block1}"
    yield f"setblock {x+3} {y+3} {z} {block2}"
    yield f"setblock {x} {y} {z+6} {block3}"
    yield f"setblock {x} {y} {z+8} {block4}"

    if REMOVE_OLD_SYSTEM:
        yield f"fill {x+3} {y+1} {z-1} {x+3} {y+2} {z-3} {AIR}"
        yield f"fill {x+1} {y+2} {z+1} {x+2} {y+3} {z+1} {AIR}"
        yield f"fill {x-1} {y+1} {z+6} {x-3} {y+2} {z+8} {AIR}"


@mcfunction(tags=["do2:replace_audio_systems"])
def replace_warden_emerge():
    x, y, z = -575, 88, 1938
    block = sound(f"do2:ambient.warden_emerge", 50)

    yield f"setblock {x} {y} {z} {block}"

    if REMOVE_OLD_SYSTEM:
        yield f"fill {x-4} {y} {z} {x-2} {y+2} {z} {AIR}"
        yield f"setblock {x-2} {y} {z} {FILLER}"

@mcfunction(tags=["do2:replace_audio_systems"])
def replace_warden_emerge():
    x, y, z = -612, 45, 1945
    block = sound(f"do2:ambient.warden_roar", 50)

    yield f"fill {x} {y} {z} {x} {y} {z+1} minecraft:repeater[delay=4,facing=north]"
    yield f"setblock {x} {y} {z+2} {block}"

    if REMOVE_OLD_SYSTEM:
        yield f"fill {x+2} {y} {z-3} {x+2} {y+2} {z-1} {AIR}"

