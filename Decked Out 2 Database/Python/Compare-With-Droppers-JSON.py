import json
from pathlib import Path


ROOT = Path(__file__).parents[1]


def load(path):
    with open(ROOT / path, "rt", encoding="utf-8") as fd:
        return json.load(fd)


def parse_pos(txt):
    x, y, z = map(int, txt.split(", "))
    return x, y, z


droppers_json = load("Python/_Droppers.json")

dropper_locations = [
    (parse_pos(pos), group)
    for group in droppers_json.values()
    for pos in group
]

print(f"Read {len(dropper_locations)} locations from Droppers.json")
dropper_locations = dict(dropper_locations)
print(f"Read {len(dropper_locations)} unique locations from Droppers.json")

dropper_db = [
    (tuple(container["pos"]), container)
    for path in (ROOT / "Containers").rglob("*.json")
    for container in load(path)
]

print(f"Read {len(dropper_db)} locations from DB")
dropper_db = dict(dropper_db)
print(f"Read {len(dropper_db)} unique locations from DB")


print("Common locations:", len(set(dropper_locations) & set(dropper_db)))
print("Locations only in Droppers.json:", len(set(dropper_locations) - set(dropper_db)))
print("Locations only in DB", len(set(dropper_db) - set(dropper_locations)))


for pos in dropper_db:
    if pos not in dropper_locations:
        print(json.dumps(dropper_db[pos], indent=4))