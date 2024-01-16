from collections import defaultdict

from mcfunction import mcfunction


TAG = "do2.tags.teleport_mobs_marker"
KILL_MARKERS = f"kill @e[type=minecraft:marker,tag={TAG}]"


@mcfunction(tags=["do2:fix_dungeon"])
def _():
    import data

    yield KILL_MARKERS
    yield "data modify storage do2:debug MobPositions set value {}"

    MOBS_IN_ZONES = defaultdict(list)

    for mobs in [data.ENTITIES.RAVAGERS, data.ENTITIES.WARDENS]:
        for mob in mobs:
            MOBS_IN_ZONES[mob["zone"]].append(mob)

    for zone_name, zone in data.ZONES.items():
        if zone_name.startswith("_"):
            continue

        for x, y, z in zone["markers"]:
            yield f"""summon minecraft:marker {x} {y} {z} {{
                    Tags: ["{TAG}"]
                }}"""

        for mob in MOBS_IN_ZONES[zone_name]:
            yield f"""
                execute as {mob["id"]}
                        run tp @s @e[type=minecraft:marker,tag={TAG},sort=random,limit=1]
                """

            yield f"""
                data modify storage do2:debug MobPositions."{mob["name"]}"
                    set from entity {mob["id"]} Pos
                """

        yield KILL_MARKERS
