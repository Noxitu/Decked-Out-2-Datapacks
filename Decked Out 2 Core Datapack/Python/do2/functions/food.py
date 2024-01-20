from mcfunction import mcfunction


SCOREBOARD = "do2.scoreboard.food"
TAG_HUNGER = "do2.tags.hunger"
TAG_SATURATION1 = "do2.tags.saturation1"

# Target saturation will be rounded down
TARGET_SATURATION = 12.8


@mcfunction(tags=["minecraft:load"])
def create_scoreboard():
    yield f"scoreboard objectives add {SCOREBOARD} dummy"


def _update_total():
    yield f"execute store result score $foodSaturationLevel {SCOREBOARD} run data get entity @s foodSaturationLevel 1000"
    yield f"execute store result score $total {SCOREBOARD} run data get entity @s foodSaturationLevel 8000"
    yield f"execute store result score $tmp {SCOREBOARD} run data get entity @s foodExhaustionLevel 2000"

    yield f"scoreboard players add $total {SCOREBOARD} 8000"
    yield f"scoreboard players operation $total {SCOREBOARD} -= $tmp {SCOREBOARD}"



# @mcfunction(tags=["minecraft:tick"])
# def display_food():
#     yield "scoreboard players reset * dummy"
#     yield """
#         execute as @a[name=!TangoCam]
#                 store result score @s dummy 
#                 run data get entity Noxitu foodSaturationLevel 1000
#         """
#     yield "execute store result score $foodExhaustionLevel dummy run data get entity Noxitu foodExhaustionLevel 1000"


@mcfunction(tags=["do2:fix_dungeon"])
def invoke_set_food():
    yield f"""
        execute positioned -559 115 1979
                as @a[distance=..7]
                run function {set_food}
        """

@mcfunction
def set_food():
    yield f"effect give @s minecraft:instant_health 1 100 true"
    yield f"tag @s add {TAG_SATURATION1}"
    yield f"schedule function {invoke_saturation1} 1t replace"


@mcfunction
def invoke_saturation1():
    yield f"""
        execute as @a[tag={TAG_SATURATION1}]
                run function {saturation1}
        """

    yield f"""
        execute if entity @a[tag={TAG_SATURATION1}]
                run schedule function {invoke_saturation1} 1t
        """


@mcfunction
def saturation1():
    yield from _update_total()

    max_saturation = 20000
    condition = f"score $foodSaturationLevel {SCOREBOARD} matches {max_saturation}"

    yield f"execute unless {condition} run effect give @s minecraft:saturation infinite 255 false"
    yield f"execute if {condition} run tag @s remove {TAG_SATURATION1}"
    yield f"execute if {condition} run effect clear @s minecraft:saturation"

    yield f"execute if {condition} run tag @s add {TAG_HUNGER}"
    yield f"execute if {condition} run schedule function {invoke_hunger} 1t replace"


@mcfunction
def invoke_hunger():
    yield f"""
        execute as @a[tag={TAG_HUNGER}]
                run function {hunger}
        """

    yield f"""
        execute if entity @a[tag={TAG_HUNGER}]
                run schedule function {invoke_hunger} 1t
        """


@mcfunction
def hunger():
    yield from _update_total()

    yield "effect clear @s minecraft:hunger"

    target = int(TARGET_SATURATION // 1 + 1) * 8000

    for step in [0, 10, 100, 255]:
        yield f"""
            execute if score $total {SCOREBOARD} matches {target + 10 * step}..
                    run effect give Noxitu minecraft:hunger infinite {step} true
            """

    condition = f"score $total {SCOREBOARD} matches {target}.."

    yield f"execute unless {condition} run tag @s remove {TAG_HUNGER}"
    yield f"execute unless {condition} run effect clear @s minecraft:hunger"
