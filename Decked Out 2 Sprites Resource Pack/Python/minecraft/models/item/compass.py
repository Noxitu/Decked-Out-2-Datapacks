from common import read_json, extend_overrides
from resource_pack import json


@json
def _():
    compass = read_json("orig_compass.json")

    compass["overrides"] = extend_overrides(
        compass["overrides"],
        {
            1: lambda m: m.replace("item/", f"do2:item/compass/level1/"),
            2: lambda m: m.replace("item/", f"do2:item/compass/level2/"),
            3: lambda m: m.replace("item/", f"do2:item/compass/level3/"),
            4: lambda m: m.replace("item/", f"do2:item/compass/level4/"),
        },
    )

    return compass
