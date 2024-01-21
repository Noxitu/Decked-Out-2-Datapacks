import json as _json


def json(generator, target_path):
    value = generator()

    if value is ...:
        if target_path.exists():
            target_path.unlink()
        return

    with open(target_path, "wt", encoding="utf-8") as fd:
        _json.dump(value, fd, indent=4)
