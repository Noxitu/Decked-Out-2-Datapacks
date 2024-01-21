import json as _json


def json(generator, target_path):
    with open(target_path, "wt", encoding="utf-8") as fd:
        _json.dump(generator(), fd, indent=4)
