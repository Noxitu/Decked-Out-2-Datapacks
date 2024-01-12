import functools as _functools
import json as _json
import matplotlib.pyplot as plt
from pathlib import Path as _Path
import shutil

import common


_ROOT = _Path(__file__).parents[1] / "assets"
_ASSETS = []


def _get_asset_desc(call, *, name):
    if name is None:
        name = call.__qualname__.split(".")
    else:
        name = name.split("/")

    parts = call.__module__.split(".") + name
    parts = [p for p in parts if p != "_"]

    asset_type = parts[1]
    assert asset_type in {"models", "textures"}
    return parts[0] + ":" + "/".join(parts[2:]), asset_type


def _get_asset_path(asset_name, asset_type, ext):
    return _ROOT / (asset_name.replace(":", f"/{asset_type}/") + f".{ext}")


def _create_func(save_func, ext):
    def _decorator(call=None, *, skip=False, name=None):
        if call is None:
            return _functools.partial(_decorator, skip=skip, name=name)

        asset_name, asset_type = _get_asset_desc(call, name=name)

        class Call:
            SAVE = staticmethod(save_func)
            EXT = ext

            def __call__(self):
                return call()

            def __str__(self):
                return asset_name

        ret = Call()

        if not skip:
            _ASSETS.append((asset_name, asset_type, ret))

        return ret

    return _decorator


def _save_json(path, call):
    with open(path, "wt", encoding="utf-8") as fd:
        value = call()
        _json.dump(value, fd)


def _save_image(path, call):
    image = call()

    if isinstance(image, str):
        shutil.copy2(common.get_path(image), path)
    else:
        plt.imsave(path, image)


json = _create_func(_save_json, "json")
mcmeta = _create_func(_save_json, "png.mcmeta")
image = _create_func(_save_image, "png")


def save(verbose=False):
    for asset_name, asset_type, asset_call in _ASSETS:
        path = _get_asset_path(asset_name, asset_type, asset_call.EXT)
        path.parent.mkdir(exist_ok=True, parents=True)

        if verbose:
            print(path.relative_to(_ROOT))

        asset_call.SAVE(path, asset_call)
