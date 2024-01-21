from noxpack import json


def _space(size, character=None):
    if character is None:
        base = {
            False: "\uEB00",
            True: "\uEA00",
        }[size > 0]
        encoded_size = 16 * (abs(size) // 10) + abs(size) % 10
        character = chr(ord(base) + encoded_size)

    return {
        "type": "bitmap",
        "file": "do2:gui/empty.png",
        "ascent": -65535,
        "height": size - 1,
        "chars": [character],
    }


def _bitmap(name, ascent, height, chars):
    return {
        "type": "bitmap",
        "file": f"do2:gui/{name}.png",
        "ascent": ascent,
        "height": height,
        "chars": [chars],
    }

@json
def _():
    space_left = [_space(-size) for size in range(100)]
    space_right = [_space(size) for size in range(100)]

    return {
        "providers": [
            # GUI Level 2 - Can't figure out some subpixel alignments :/
            # _bitmap("map_background", 200, 213, "\uE001"),
            # _bitmap("map_blue", 200, 213, "\uE002"),
            # _bitmap("water_gui", 190, 192, "\uE003"),
            # _bitmap("empty_gui", 190, 192, "\uE004"),
            # _bitmap("ticks", 190, 192, "\uE011\uE012\uE013\uE014"),
            # _bitmap("card_ticks", 190, 192, "\uE015\uE016\uE017\uE018"),
            # _space(-3.9, "\uE019"),
            # _space(-160, "\uE00A"), # 1/6th of Left Offset
            # _space(160, "\uE00B"), # 1/6th of Right Offset
            # _space(120, "\uE00C"), # Left Padding
            # _space(-165, "\uE00D"), # 1/3th of Right Padding
            # _space(-10, "\uE01A"), # Step back tick
            # _space(-5, "\uE01B"),  # Step back card tick
            # _space(-205, "\uE01C"),  # From end of map border to start of map content
            # _space(-149, "\uE01D"),  # From end of map content to start of ticks
            # _space(43, "\uE01E"),  # From start of ticks to start of cards
            # _space(-67, "\uE01F"),  # From start of cards to start of map border

            # GUI Level 3
            _bitmap("map_background", 107, 142, "\uE001"),
            _bitmap("map_blue", 107, 142, "\uE002"),
            _bitmap("water_gui", 100, 128, "\uE003"),
            _bitmap("empty_gui", 100, 128, "\uE004"),
            _bitmap("ticks", 100, 128, "\uE011\uE012\uE013\uE014"),
            _bitmap("card_ticks", 100, 128, "\uE015\uE016\uE017\uE018"),
            _space(-106, "\uE00A"), # 1/6th of Left Offset
            _space(106, "\uE00B"), # 1/6th of Right Offset
            _space(80, "\uE00C"), # Left Padding
            _space(-109, "\uE00D"), # 1/3th of Right Padding
            _space(-7, "\uE01A"), # Step back tick
            _space(-4, "\uE01B"),  # Step back card tick
            _space(-137, "\uE01C"),  # From end of map border to start of map content
            _space(-100, "\uE01D"),  # From end of map content to start of ticks
            _space(29, "\uE01E"),  # From start of ticks to start of cards
            _space(-67, "\uE01F"),  # From start of cards to start of map border
          
            *space_left,
            *space_right,
        ]
    }
