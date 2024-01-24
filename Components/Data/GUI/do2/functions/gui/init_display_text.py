from noxpack import mcfunction

import numpy as np

MAP_BORDER_SIZE = 434
MAP_SIZE = 392

MAP_X = 112
MAP_BOTTOM = 946

ACTIONBAR_TOP_IN_FONT = 65
ACTIONBAR_X = 960

BITMAP_SIZE = 128


def sc(size):
    return size * MAP_SIZE / BITMAP_SIZE


TICKS_X = sc(28)
TICK_SPACE_SIZE = sc(92)
TICKS_WIDTH = sc(5)

CARD_TICKS_X = sc(59)
CARD_TICK_SPACE_SIZE = sc(60)
CARD_TICKS_WIDTH = sc(2)


class SpaceManager:
    def _space(self, space):
        if space == 0:
            return ""

        if space > 0:
            # return f"\\u{0xea00 + space:04x}"
            return chr(0xea00 + space)
        else:
            # return f"\\u{0xeb00 - space:04x}"
            return chr(0xeb00 - space)

    def __call__(self, space):
        # print(f"space({space})")
        if space == 0:
            return ""
        
        for max_space in [255, 128, 64, 32]:
            if space in (-max_space, max_space):
                return self._space(space)

            if space > max_space:
                return self(max_space) + self(space - max_space)
            
            if space < -max_space:
                return self(-max_space) + self(space + max_space)
        
        return self._space(space)


space = SpaceManager()


def generate(level):
    screen2font = 1 / level
    base_code = 0xE000 + level * 0x100

    def px(size):
        return np.round(size * screen2font).astype(int)

    class Shape:
        def __init__(self, code, width):
            self.code = chr(base_code + code)
            # self.code = f"\\u{base_code + code:04x}"
            self.width = px(width)

    def shapes(width, *codes):
        return [Shape(code, width) for code in codes]

    class GUI:
        def __init__(self):
            self.buffer = ""
            self.x = 0

        def discard(self):
            self.buffer = ""

        def print(self, title):
            # print(title, repr(self.buffer).replace("'", '"'))
            # value = repr(self.buffer).replace("'", '"')
            value = self.buffer
            # print(f'yield """data modify storage do2:gui Text.{title}.Level{level} set value {value} """')
            yield f"""data modify storage do2:gui Text.{title}.Level{level} set value "{value}" """
            self.buffer = ""

        def add(self, *shapes, sep=0):
            first = True
            for shape in shapes:
                if not first:
                    self.buffer += space(sep)
                    self.x += sep
                first = False

                self.buffer += shape.code
                self.x += shape.width + 1


        def set_x(self, x):
            step = x - self.x
            self.buffer += space(step)
            self.x = x
                

    map_border = Shape(0x10, MAP_BORDER_SIZE)
    map_gui = Shape(0x20, MAP_SIZE)

    ticks = shapes(TICKS_WIDTH, *range(0x31, 0x35))
    holes = shapes(TICKS_WIDTH, *range(0x41, 0x45))

    card_ticks = shapes(CARD_TICKS_WIDTH, *range(0x51, 0x57))

    map_border_padding = px((MAP_BORDER_SIZE - MAP_SIZE) / 2)

    n_ticks = {4: 13}.get(level, 15)
    ticks_sep = {1: 2}.get(level, 0)

    ticks_offset = px(TICKS_X)
    ticks_size = n_ticks * ticks[0].width + (ticks_sep + 1) * (n_ticks - 1)
    ticks_space = px(TICK_SPACE_SIZE)

    ticks_padding = (ticks_space - ticks_size) // 2

    card_ticks_sep = {1: 2, 4: -1}.get(level, 0)

    card_ticks_offset = px(CARD_TICKS_X)
    card_ticks_size = 20 * card_ticks[0].width + (card_ticks_sep + 1) * 19
    card_ticks_space = px(CARD_TICK_SPACE_SIZE)
    card_ticks_padding = (card_ticks_space - card_ticks_size) // 2
    # print(f"# Level {level}")
    # print("padding: ", ticks_padding, card_ticks_padding)

    gui = GUI()
    gui.set_x(2*px(MAP_X - ACTIONBAR_X))
    yield from gui.print("offset")
    gui.set_x(0)
    gui.discard()

    gui.add(map_border)
    gui.set_x(map_border_padding)
    gui.add(map_gui)
    gui.set_x(map_border_padding + ticks_offset + ticks_padding)
    yield from gui.print("map")

    for idx, name in enumerate(["embers", "treasure", "hazard_block", "clank_block"]):
        for i in range(16):
            gui.set_x(map_border_padding + ticks_offset + ticks_padding)
            if name == "embers":
                gui.discard()

            j = min(n_ticks, i)
            gui.add(*[ticks[idx]] * j, *[holes[idx]] * (n_ticks - j), sep=ticks_sep)
            yield from gui.print(f"{name}{i}")

    x0 = gui.x

    for i in range(41):
        def get_tick(j):
            t = card_ticks
            t = t[:3] if j < 5 or 10 <= j < 15 else t[3:]
            j = 2 * j

            if j >= i:
                return t[0]
            if j+1 == i:
                return t[1]
            return t[2]

        gui.set_x(x0)
        gui.discard()

        gui.set_x(map_border_padding + card_ticks_offset + card_ticks_padding)
        gui.add(
            *[get_tick(j) for j in range(20)],
            sep=card_ticks_sep
        )

        gui.set_x(0)
        yield from gui.print(f"cards{i}")





@mcfunction(tags=["minecraft:load"])
def _():
    yield """data modify storage do2:gui Text set value {}"""

    for level in range(1, 5):
        yield from generate(level)
