from mcfunction import mcfunction


BUSH = "minecraft:sweet_berry_bush"
AIR = "minecraft:air"
GROWN = "age=3"


@mcfunction(tags=["do2:fix_dungeon"])
def _():
    import data
    for item in data.SWEET_BERRY_BUSHES:
        x, y, z = item["pos"]
        pos = f"{x} {y} {z}"

        yield f"# {item['description']}"
        yield f"fill {pos} {pos} {BUSH}[{GROWN}] replace {AIR}"
        yield f"fill {pos} {pos} {BUSH}[{GROWN}] replace {BUSH}"
        yield ""
