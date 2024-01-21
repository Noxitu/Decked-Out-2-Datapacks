import functools as _functools

from noxitu_pack_builder.context import ContextStorage
import noxitu_pack_builder.tags

_OUTPUTS = ContextStorage("outputs", list)


def _get_path(call, *, name):
    if name is None:
        name = call.__qualname__

    parts = call.__module__.split(".") + name.split(".")
    parts = [part for part in parts if part != "_"]
    return "/".join(parts)


def _get_name(path):
    parts = path.split("/")
    return f"{parts[0]}:{'/'.join(parts[2:])}"


def _output_file(call, *, save, path=None, no_root=False, suffix=None, tags=[], name=None):
    if path is None:
        path = _get_path(call, name=name)

    class OutputFile:
        def __str__(self):
            return _get_name(path)

        def __call__(self):
            return call()
        
        def save(self, target_path, root):
            if not no_root:
                target_path /= root

            target_path /= path

            if suffix is not None:
                target_path = target_path.with_suffix(suffix)

            target_path.parent.mkdir(exist_ok=True, parents=True)
            print("\033[35m::\033[m   ", target_path)
            save(call, target_path)

    ret = OutputFile()
    _OUTPUTS.append(ret)

    noxitu_pack_builder.tags.register_tags(ret, *tags)

    return ret


def output_file(call=None, **kwargs):
    if call is None:
        return _functools.partial(output_file, **kwargs)

    return _output_file(call, **kwargs)


def save_outputs(output_root, *, root):
    for output in _OUTPUTS:
        output.save(output_root, root)

# def _get_asset_desc(call, *, name):
#     if name is None:
#         name = call.__qualname__.split(".")
#     else:
#         name = name.split("/")

#     parts = call.__module__.split(".") + name
#     parts = [p for p in parts if p != "_"]

#     asset_type = parts[1]
#     assert asset_type in {"models", "textures"}
#     return parts[0] + ":" + "/".join(parts[2:]), asset_type


# def _get_asset_path(asset_name, asset_type, ext):
#     return _ROOT / (asset_name.replace(":", f"/{asset_type}/") + f".{ext}")


# def _create_func(save_func, ext):
#     def _decorator(call=None, *, skip=False, name=None):
#         if call is None:
#             return _functools.partial(_decorator, skip=skip, name=name)

#         asset_name, asset_type = _get_asset_desc(call, name=name)

#         class Call:
#             SAVE = staticmethod(save_func)
#             EXT = ext

#             def __call__(self):
#                 return call()

#             def __str__(self):
#                 return asset_name

#         ret = Call()

#         if not skip:
#             _ASSETS.append((asset_name, asset_type, ret))

#         return ret

#     return _decorator


# def _save_json(path, call):
#     with open(path, "wt", encoding="utf-8") as fd:
#         value = call()
#         _json.dump(value, fd)


# def _save_image(path, call):
#     image = call()

#     if isinstance(image, str):
#         shutil.copy2(common.get_path(image), path)
#     else:
#         plt.imsave(path, image)


# json = _create_func(_save_json, "json")
# mcmeta = _create_func(_save_json, "png.mcmeta")
# image = _create_func(_save_image, "png")


# def save(verbose=False):
#     for asset_name, asset_type, asset_call in _ASSETS:
#         path = _get_asset_path(asset_name, asset_type, asset_call.EXT)
#         path.parent.mkdir(exist_ok=True, parents=True)

#         if verbose:
#             print(path.relative_to(_ROOT))

#         asset_call.SAVE(path, asset_call)
