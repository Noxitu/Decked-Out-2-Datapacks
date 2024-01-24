import numpy as np

MAP_BORDER_SIZE = 434
MAP_SIZE = 392

MAP_LEFT = 112
MAP_BOTTOM = 946

ACTIONBAR_TOP_IN_FONT = 65
ACTIONBAR_LEFT = 960

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
            return chr(0xea00 + space)
        else:
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
            self.code = chr(base_code + code)  # f"\\u{base_code + code:04x}"
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
            value = repr(self.buffer).replace("'", '"')
            print(f'yield """data modify storage do2:gui Text.{title}.Level{level} set value {value} """')
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
    gui.add(map_border)
    gui.set_x(map_border_padding)
    gui.add(map_gui)
    gui.set_x(map_border_padding + ticks_offset + ticks_padding)
    gui.print("Map")

    for i in range(16):
        gui.set_x(map_border_padding + ticks_offset + ticks_padding)
        gui.discard()

        j = min(n_ticks, i)
        gui.add(*[ticks[0]] * j, *[holes[0]] * (n_ticks - j), sep=ticks_sep)
        gui.print(f"Embers{i}")

    gui.set_x(map_border_padding + ticks_offset + ticks_padding)
    gui.add(*[ticks[1]] * n_ticks, sep=ticks_sep)
    gui.print("Treasure")

    gui.set_x(map_border_padding + ticks_offset + ticks_padding)
    gui.add(*[ticks[2]] * 1, *[holes[2]] * (n_ticks - 1), sep=ticks_sep)
    gui.print("Hazard")

    gui.set_x(map_border_padding + ticks_offset + ticks_padding)
    gui.add(*[ticks[3]] * n_ticks, sep=ticks_sep)
    gui.print("Clank")

    # gui.set_x(map_border_padding + card_ticks_offset + card_ticks_padding)
    # gui.add(
    #     *[card_ticks[0]] * 3,
    #     *[card_ticks[1]] * 3,
    #     *[card_ticks[2]] * 3,
    #     *[card_ticks[3]] * 3,
    #     *[card_ticks[4]] * 3,
    #     *[card_ticks[5]] * 5,
    #     sep=card_ticks_sep
    # )

    gui.set_x(0)
    gui.print("Cards")

    # print(f'"{gui.buffer}"')
    print()

    # map_border_ascent = MAP_SIZE + (MAP_BORDER_SIZE - MAP_SIZE) / 2

    # print(f"""_bitmap("map_blue", {px(map_border_ascent)}, {px(MAP_BORDER_SIZE)}, "\\uE00{level}"),""")
    # print(f"""_bitmap("water_gui", {px(MAP_SIZE)}, {px(MAP_SIZE)}, "\\uE10{level}"),""")

    # def back(n):
    #     return "\\ueb99" * (n // 98) + f"\\ueb{n % 98 + 1:02d}"

    # # ret = back(map_border_ascent * screen2font + 1)

    # back1 = MAP_BORDER_SIZE - (MAP_BORDER_SIZE - MAP_SIZE) / 2

    # ticks_space_px = px(MAP_SIZE * BITMAP_TICK_SPACE_SIZE / BITMAP_SIZE)
    # tick_size_px = px(MAP_SIZE * BITMAP_TICKS_WIDTH / BITMAP_SIZE)
    # tick_free_px = ticks_space_px - (15 * tick_size_px + 14)
    # bitmap_tick_padding = BITMAP_TICK_SPACE_SIZE * tick_free_px / ticks_space_px / 2

    # back2 = MAP_SIZE * (BITMAP_SIZE - BITMAP_TICKS_X - bitmap_tick_padding) / BITMAP_SIZE
    # back3_px = tick_size_px * 15 + 15

    # ret = f"\\ue00{level}"
    # ret += back(px(back1) + 1) + f"\\ue10{level}"
    # ret += back(px(back2) + 2) + f"\\ue111" * 5 + f"\\ue511" * 10
    # ret += back(back3_px) + f"\\ue112" * 4 + f"\\ue512" * 11
    # ret += back(back3_px) + f"\\ue113" * 3 + f"\\ue513" * 12
    # ret += back(back3_px) + f"\\ue114" * 2 + f"\\ue514" * 13

    # print(f"""# title Noxitu actionbar "{ret}" """)
    # print()

    # print("size", MAP_SIZE * BITMAP_TICK_SPACE_SIZE / BITMAP_SIZE)
    # print("one", MAP_SIZE * BITMAP_TICKS_WIDTH / BITMAP_SIZE)
    # print(px(MAP_SIZE * BITMAP_TICK_SPACE_SIZE / BITMAP_SIZE), 15 * (px(MAP_SIZE * BITMAP_TICKS_WIDTH / BITMAP_SIZE) + 1))


for level in range(1, 5):
# for level in [3]:
    generate(level)

# space.report()
