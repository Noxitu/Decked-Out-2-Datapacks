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
        "file": f"do2:gui/{name}.png",
        "ascent": ascent,
        "height": height,
        "chars": [chars],
    }


def generate_gui_font():
    for level in range(1, 5):
        MAP_BORDER_SIZE = 434
        MAP_SIZE = 392

        base_code = 0xE000 + level * 0x100
        screen2font = 1 / level

        # Y calculated from bottom of screen
        MAP_Y = 525
        ACTION_BAR_Y = 65 / screen2font

        def px(size):
            return int(np.round(size * screen2font))

        def bitmap(name, ascent, height, *codes):
            chars = "".join(chr(base_code + code) for code in codes)
            return _bitmap(name, px(ascent), px(height), chars)

        # print("need ascent", MAP_Y - ACTION_BAR_Y)
        map_ascent = min(MAP_SIZE, MAP_Y - ACTION_BAR_Y)
        border_ascent = map_ascent + (MAP_BORDER_SIZE - MAP_SIZE) / 2

        if border_ascent > MAP_BORDER_SIZE:
            reduce = border_ascent - MAP_BORDER_SIZE
            map_ascent -= reduce
            border_ascent -= reduce

        args = border_ascent, MAP_BORDER_SIZE

        yield bitmap("map_blue", *args, 0x10)
        yield bitmap("map", *args, 0x11)

        args = map_ascent, MAP_SIZE

        yield bitmap("gui_water", *args, 0x20)
        yield bitmap("gui_transparent", *args, 0x21)

        yield bitmap("ticks", *args, *range(0x31, 0x35), *range(0x41, 0x45))
        yield bitmap("card_ticks", *args, *range(0x51, 0x57))


@json
def _():
    space_left = []
    space_right = []

    implemented = list(range(1, 33)) + [64, 128, 255]
    space_left = [_space(0xEB00 + size, -size) for size in implemented]
    space_right = [_space(0xEA00 + size, size) for size in implemented]

    return {
        "providers": [
            *generate_gui_font(),
            *space_left,
            *space_right,
        ]
    }
