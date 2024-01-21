from noxpack import mcfunction


def _one(name, symbol, value, value_match=None):
    if value_match is None:
        value_match = value

    symbol = chr(ord("\uE010") + symbol)
    symbols = value * symbol
    back = "\uE01A" * value

    yield f"""
        execute if score ${name} do2.gui matches {value_match}
                run data modify storage tmp tmp.{name}
                    set value "{symbols}{back}"
        """


def _card(value, value_match=None):
    if value_match is None:
        value_match = value

    symbols = (["\uE015", "\uE01B\uE016"] * 5 + ["\uE017", "\uE01B\uE018"] * 5)
    symbols *= 2
    symbols = symbols[:value]
    symbols = "".join(symbols)
    back = (value + 1) // 2 * "\uE01B"

    yield f"""
        execute if score $cards do2.gui matches {value_match}
                run data modify storage tmp tmp.cards
                    set value "{symbols}{back}"
        """


def _update_category(name, symbol):
    for i in range(15):
        yield from _one(name, symbol, i)
    yield from _one(name, symbol, 15, "15..")

@mcfunction
def update():
    yield "data modify storage tmp tmp set value {}"

    yield from _update_category("embers", 1)
    yield from _update_category("treasure", 2)
    yield from _update_category("hazard_block", 3)
    yield from _update_category("clank_block", 4)

    for i in range(40):
        yield from _card(i)
    yield from _card(40, "40..")

@mcfunction(tags=["minecraft:tick"])
def _():
    offset_left = 6 * "\uE00A"
    offset_right = 6 * "\uE00B"
    padding_left = "\uE00C"
    padding_right = 3 * "\uE00D"

    offset, padding = offset_left, padding_left
    # offset, padding = offset_right, padding_right
    # padding = ""

    yield f"""title @a actionbar [
            "{offset}",
            "{padding}",
            "\uE002\uE01C\uE004\uE01D",
            {{"nbt": "tmp.embers", "storage": "tmp"}},
            {{"nbt": "tmp.treasure", "storage": "tmp"}},
            {{"nbt": "tmp.hazard_block", "storage": "tmp"}},
            {{"nbt": "tmp.clank_block", "storage": "tmp"}},
            "\uE01E",
            {{"nbt": "tmp.cards", "storage": "tmp"}},
            "\uE01F",
            "|"
        ]"""
