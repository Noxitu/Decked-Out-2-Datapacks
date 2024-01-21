import noxpack
from noxitu_pack_builder.context import ContextStorage

_TAGS = ContextStorage("tags", dict)


def _get_path(tag):
    namespace, tag = tag.split(":")
    tag = tag.split("/")

    return "/".join([namespace, "tags", "functions"] + tag)


def get_tag(tag):
    if tag not in _TAGS:
        _TAGS[tag] = []

        @noxpack.json(path=_get_path(tag))
        def _():
            if not _TAGS[tag]:
                return ...

            return {
                "values": _TAGS[tag]
            }

    functions = _TAGS[tag]
    return functions


def register_tags(function, *tags):
    for tag in tags:
        get_tag(tag).append(str(function))