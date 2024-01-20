from mcfunction import mcfunction


@mcfunction(tags=["do2:fix_dungeon"])
def fix_artifact_10():
    """Fix artifact #10 not connected to clank."""
    yield "fill -546 35 1995 -546 35 1993 minecraft:cyan_wool"
    yield "fill -546 35 1993 -550 35 1993 minecraft:cyan_wool"
    yield "fill -550 35 1993 -550 35 1985 minecraft:cyan_wool"

    yield "fill -546 36 1995 -546 36 1993 minecraft:redstone_wire"
    yield "fill -546 36 1993 -550 36 1993 minecraft:redstone_wire"
    yield "fill -550 36 1993 -550 36 1985 minecraft:redstone_wire"

    yield "setblock -546 36 1994 minecraft:repeater[facing=south]"


@mcfunction(tags=["do2:fix_dungeon"])
def fix_toots():
    # https://www.reddit.com/r/HermitCraft/comments/18t3bz8
    yield """
        execute if block -558 63 1960 minecraft:clay
                run setblock -558 63 1960 minecraft:stone
        """




@mcfunction(tags=["do2:fix_dungeon"])
def fix_crown_converter_delay():
    yield """
        execute if block -644 -15 1984 minecraft:repeater[facing=south,delay=1]
                run setblock -644 -15 1984 minecraft:repeater[facing=south,delay=3]
        """
    

@mcfunction(tags=["do2:fix_dungeon"])
def fix_silent_runner():
    yield "fill -553 29 1924 -552 31 1927 minecraft:air"
    yield "fill -552 29 1924 -552 29 1927 minecraft:redstone_wire"
    yield "setblock -553 30 1928 minecraft:target"
    yield "setblock -554 24 1938 minecraft:sticky_piston[facing=up]"
    yield "setblock -554 25 1938 minecraft:blue_wool"
    yield "setblock -554 24 1939 minecraft:blue_wool"
    yield "setblock -554 25 1939 minecraft:redstone_wire"