from noxpack import json
import numpy as np


def _space(code, size):
    return {
        "type": "bitmap",
        "file": "do2:gui/empty.png",
        "ascent": -65535,
        "height": size - (1 if size > 0 else 2),
        "chars": [chr(code)],
    }


def _bitmap(name, ascent, height, chars):
    return {
        "type": "bitmap",
        "file": f"{name}.png",
        "ascent": ascent,
        "height": height,
        "chars": [chars],
    }

@json
def _():
    space_left = []
    space_right = []

    implemented = list(range(1, 33)) + [64, 128, 255]
    space_left = [_space(0xEB00 + size, -size) for size in implemented]
    space_right = [_space(0xEA00 + size, size) for size in implemented]

    artifacts = "".join(chr(0xe100 + i) for i in range(1, 30))

    return {
        "providers": [
            _bitmap("do2:font_icons/icons16", 16, 16, "\ue001\ue002\ue003\ue004\ue023"),
            _bitmap("do2:font_icons/icons32", 16, 16, artifacts),
            _bitmap("do2:font_icons/icons64", 16, 16, "\ue011\ue012\ue013\ue021\ue022\ue11e"),
            *space_left,
            *space_right,
        ]
    }
