import json


def load_json(path):
    with open(path, "rt", encoding="utf-8") as fd:
        return json.load(fd)
