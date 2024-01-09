from mcfunction import mcfunction


DRIPSTONE = [
    (-554, 1961, (14, 15), (16, 17)),
    (-554, 1963, ..., (16, 17)),
    (-553, 1960, (14, 16), (17, 20)),
    (-553, 1962, ..., (17, 18)),
    (-552, 1959, (14, 15), ...),
    (-552, 1959, ..., (16, 17)),
    (-552, 1961, (14, 20), (21, 22)),
    (-552, 1962, ..., (16, 18)),
    (-552, 1963, (14, 16), (17, 18)),
    (-552, 1964, (14, 15), (16, 17)),
    (-549, 1961, (15, 17), (18, 21)),
]


def _fill(x, z, ys, direction, merge):
    if ys is Ellipsis:
        return
    
    y1, y2, dy = {
        "down": (min(ys), max(ys), 1),
        "up": (max(ys), min(ys), -1),
    }[direction]

    size = abs(y1 - y2) + 1
    tip = "tip_merge" if merge else "tip"

    def dripstone(thickness):
        return f"""minecraft:pointed_dripstone[vertical_direction={direction},thickness={thickness}]"""
    
    if size >= 3:
        yield f"""setblock {x} {y2} {z} {dripstone("base")}"""

    if size > 4:
        yield f"""fill {x} {y1+2*dy} {z} {x} {y2-dy} {z} {dripstone("middle")}"""

    if size == 4:
        yield f"""setblock {x} {y1+2*dy} {z} {dripstone("middle")}"""
    
    if size >= 2:
        yield f"""setblock {x} {y1+dy} {z} {dripstone("frustum")}"""

    if size >= 1:
        yield f"""setblock {x} {y1} {z} {dripstone(tip)}"""



@mcfunction(tags=["do2_refill:all", "do2_refill:fix"])
def _():
    ifs = []

    for x, z, up, down in DRIPSTONE:
        if up is not Ellipsis:
            ifs.append(f"if block {x} {up[1]} {z} minecraft:pointed_dripstone")

        if down is not Ellipsis:
            ifs.append(f"if block {x} {down[0]} {z} minecraft:pointed_dripstone")

    ifs = " ".join(ifs)

    yield "# If tips are not broken, all other blocks must be there."

    yield f"execute {ifs} run return 0"

    yield "# Don't fix while player is close by. It looks weird, and can be really unfun to get blocked by it."

    yield """
        execute positioned -552 15 1961
                if entity @p[distance=..16]
                run return 0
    """

    for x, z, up, down in DRIPSTONE:
        yield from _fill(x, z, up, 'up', down is not None)
        yield from _fill(x, z, down, 'down', up is not None)