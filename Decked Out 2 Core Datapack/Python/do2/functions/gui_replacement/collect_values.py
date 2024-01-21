from mcfunction import mcfunction

SCOREBOARD = "do2.gui"
SCOREBOARD_TMP = "do2.gui.tmp"


def _get_count_impl(target, *, n=1, init=True):
    for i in range(n):
        if init and i == 0:
            yield f"""
                execute store result score $tmp {SCOREBOARD_TMP}
                        run data get {target} Items[{i}].Count
                        """
        else:
            yield f"""
                execute store result score $tmp2 {SCOREBOARD_TMP}
                        run data get {target} Items[{i}].Count
                        """
            
            yield f"scoreboard players operation $tmp {SCOREBOARD_TMP} += $tmp2 {SCOREBOARD_TMP}"



def _get_count(name, pos, *, n=1, div=1):
    yield from _get_count_impl(f"block {pos}", n=n)

    if div != 1:
        yield f"scoreboard players set $tmp2 {SCOREBOARD_TMP} {div}"
        yield f"scoreboard players operation $tmp {SCOREBOARD_TMP} /= $tmp2 {SCOREBOARD_TMP}"

    yield f"scoreboard players operation {name} {SCOREBOARD} = $tmp {SCOREBOARD_TMP}"


def _set_level(name):
    yield f"scoreboard players set $tmp {SCOREBOARD_TMP} 4"

    for level in [3, 2, 1]:
        pos = f"{-630-level} 26 1993"
        yield f"execute if block {pos} minecraft:quartz_block run scoreboard players set $tmp {SCOREBOARD_TMP} {level}"

    yield f"scoreboard players operation {name} {SCOREBOARD} = $tmp {SCOREBOARD_TMP}"


@mcfunction(tags=["minecraft:load"])
def init():
    yield f"""scoreboard objectives add {SCOREBOARD} dummy "Decked Out 2" """
    yield f"""scoreboard objectives add {SCOREBOARD_TMP} dummy"""

    yield f"""
        execute unless block -525 52 1872 minecraft:dropper
                run setblock -525 52 1872 minecraft:dropper[facing=west]
        """
    
    yield f"""
        execute unless block -526 52 1872 minecraft:dropper
                run setblock -526 52 1872 minecraft:dropper[facing=east]{{
                    Items: [{{
                        id: "minecraft:iron_nugget",
                        Slot: 0b,
                        Count: 64b
                    }}]
                }}
        """

    yield f"""schedule function {update_scoreboard} 3s replace"""


@mcfunction
def update_scoreboard():
    yield from _get_count("$recycle", "-622 34 1920")
    yield from _get_count("$effect.regeneration", "-623 33 1934")
    yield from _get_count("$effect.resistance", "-623 33 1936")
    yield from _get_count("$effect.jump_boost", "-623 33 1938")
    yield from _get_count("$effect.speed", "-623 33 1940")
    yield from _get_count("$clank_block", "-618 25 1959")
    yield from _get_count("$clank", "-618 24 1969", n=9, div=5)
    yield from _get_count("$hazard_block", "-616 25 1983")

    yield from _get_count("$treasure", "-614 25 1990", n=4)
    yield from _get_count("$embers", "-614 25 1999", n=3)
    yield from _get_count("$treasure.level1_left", "-615 20 1994", n=2)
    yield from _get_count("$embers.level1_left", "-624 22 2006", n=6)

    yield from _get_count("$cards", "-525 52 1872")


    yield from _set_level("$level")

    yield f"schedule function {update_scoreboard} 3s replace"

    yield "function do2:gui_replacement/display/update"

