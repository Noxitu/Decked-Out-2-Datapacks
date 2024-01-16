from mcfunction import mcfunction

COUNT_IN_ROW = 20

BLOCK_X = -517
BLOCK_X_STEP = 3
BLOCK_Y = 61
BLOCK_Z = [1845, 1850]

X_OFFSET = [0, 1]
ROW_Y = [55, 57]
Z_OFFSET = [0, 2]


SPECIAL_Z_OFFSET = {
    (1, 0): 2,
    (1, 1): 1,
}

REDSTONE = 'minecraft:redstone_wire'
RAIL = 'minecraft:powered_rail[shape=north_south]'

ITEM = {
    (1, 9): REDSTONE,
    (1, 10): REDSTONE,
    (1, 11): REDSTONE,
}


@mcfunction(tags=["do2:fix_dungeon"])
def _():
    for row in range(2):
        for column in range(COUNT_IN_ROW):
            x1 = BLOCK_X + column * BLOCK_X_STEP
            y1 = BLOCK_Y
            z1 = BLOCK_Z[row]

            x2 = x1 + X_OFFSET[row]
            y2 = ROW_Y[row]
            z2 = z1 + Z_OFFSET[row] + SPECIAL_Z_OFFSET.get((row, column), 0)

            x3 = x1 + 1
            y3 = y1 - 1
            z3 = z1 - 2

            item = ITEM.get((row, column), RAIL)

            display_block = {
                False: "minecraft:mushroom_stem",
                # False: "minecraft:light_gray_wool",
                True: "minecraft:white_wool",
            }[column % 10 < 5]

            yield f"fill {x1} {y1} {z1} {x3} {y3} {z3} {display_block} replace #minecraft:wool"
            yield f"fill {x1} {y1} {z1} {x3} {y3} {z3} {display_block} replace minecraft:mushroom_stem"

            # prefix = f"execute run"
            prefix = f"execute unless block {x1} {y1} {z1} minecraft:water run"
            yield f"{prefix} setblock {x2} {y2} {z2} minecraft:air"
            yield f"{prefix} setblock {x2} {y2} {z2} {item}"
