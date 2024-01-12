import copy
import json
from pathlib import Path

import matplotlib.pyplot as plt


_DATA_PATH = Path(__file__).parents[1] / "Data"
_SOURCES_ROOT = _DATA_PATH.parents[3]
_ITEM_TEXTURES = (
    _SOURCES_ROOT / "Minecraft/Data/Versions/1.20.1/assets/minecraft/textures/item"
)
_BLOCK_TEXTURES = (
    _SOURCES_ROOT / "Minecraft/Data/Versions/1.20.1/assets/minecraft/textures/block"
)


def get_path(path):
    return _DATA_PATH / path


def read_image(path):
    return plt.imread(get_path(path))


def read_item_texture(path):
    return plt.imread(_ITEM_TEXTURES / path)


def read_block_texture(path):
    return plt.imread(_BLOCK_TEXTURES / path)


def read_block_texture_mcmeta(path):
    try:
        with open(_BLOCK_TEXTURES / (path + ".mcmeta"), "rt", encoding="utf-8") as fd:
            return json.load(fd)

    except FileNotFoundError:
        return None


def read_json(path):
    with open(get_path(path), "rt", encoding="utf-8") as fd:
        return json.load(fd)


def extend_overrides(overrides, replace):
    ret = []

    for override in overrides:
        ret.append(override)

        for model, func in replace.items():
            new_override = copy.deepcopy(override)
            new_override["predicate"]["custom_model_data"] = model
            new_override["model"] = func(override["model"])
            ret.append(new_override)

    return ret
