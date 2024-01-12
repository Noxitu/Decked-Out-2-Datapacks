from common import read_json, extend_overrides
from resource_pack import json


@json
def _():
    clock = read_json("orig_clock.json")

    clock["overrides"] = extend_overrides(
        clock["overrides"],
        {1: lambda m: m.replace("item/", f"do2:item/artifacts/pocketwatchofshreep/")},
    )

    return clock
