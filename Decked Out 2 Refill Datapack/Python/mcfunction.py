import functools as _functools
import json
from pathlib import Path as _Path


_ROOT = _Path(__file__).parents[1] / "data"
_FUNCTIONS = {}
_FUNCTION_TAGS = {
    "minecraft:load": [],
    "minecraft:tick": [],
}


def _get_function_name(call):
    parts = call.__module__.split(".") + call.__qualname__.split(".")
    while parts[-1] == '_':
        parts.pop()

    assert parts[1] == "functions"
    return parts[0] + ":" + "/".join(parts[2:])


def _get_function_path(function_name):
    return _ROOT / (function_name.replace(":", "/functions/") + ".mcfunction")


def _get_tags_path(function_name):
    return _ROOT / (function_name.replace(":", "/tags/functions/") + ".json")


def mcfunction(call=None, *, tags=None, skip=False):
    if call is None:
        return _functools.partial(mcfunction, tags=tags, skip=skip)

    function_name = _get_function_name(call)

    if not skip:
        _FUNCTIONS[function_name] = call

    class Call:
        def __call__(self):
            return call()
        
        def __str__(self):
            return function_name

    if tags is not None:
        for tag in tags:
            assert ":" in tag

            if tag not in _FUNCTION_TAGS:
                _FUNCTION_TAGS[tag] = []

            _FUNCTION_TAGS[tag].append(function_name)

    return Call()


def save():
    for function_name, function_call in _FUNCTIONS.items():
        path = _get_function_path(function_name)
        path.parent.mkdir(exist_ok=True, parents=True)

        with open(path, "wt", encoding="utf-8") as fd:
            for command in function_call():
                if '\n' in command:
                    command = command.split('\n')
                    command = [line.strip() for line in command]
                    command = [line for line in command if line]
                    command = ' '.join(command)
                print(command, file=fd)
            print(file=fd)

    for tag, functions in _FUNCTION_TAGS.items():
        content = {"values": functions}

        path = _get_tags_path(tag)
        path.parent.mkdir(exist_ok=True, parents=True)

        with open(path, "wt", encoding="utf-8") as fd:
            json.dump(content, fd, indent=2)
