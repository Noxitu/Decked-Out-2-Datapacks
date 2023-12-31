import json
from pathlib import Path

from egg import create_egg
from egg_hunter import create_bunny

ROOT = Path(__file__).parent.parent
MODELS = {}


def save(path, item):
    path = ROOT / path
    path.parent.mkdir(exist_ok=True, parents=True)

    with open(path, "wt", encoding="utf-8") as fd:
        json.dump(item, fd, indent=4)


def egg(model_id, name):
    MODELS[model_id] = f"eggs:item/{name}"
    egg = create_egg(name)
    save(f"assets/eggs/models/item/{name}.json", egg)


def egg_hunter(model_id, name, egg_texture):
    MODELS[model_id] = f"eggs:item/{name}"
    bunny = create_bunny(egg_texture)
    save(f"assets/eggs/models/item/{name}.json", bunny)


def save_pumpkin():
    item = {
        "parent": "minecraft:block/pumpkin",
        "overrides": [
            {"predicate": {"custom_model_data": idx}, "model": MODELS[idx]}
            for idx in sorted(MODELS)
        ],
    }

    save(f"assets/minecraft/models/item/pumpkin.json", item)


def main():
    egg(1, "silver")
    egg_hunter(101, "egg_hunter", "eggs:item/silver")
    save_pumpkin()


if __name__ == "__main__":
    main()
