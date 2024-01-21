from mcfunction import mcfunction


def _one(name, symbol, value, value_match=None):
    if value_match is None:
        value_match = value

    symbol = chr(ord("\uE010") + symbol)
    symbols = value * symbol
    back = 6 * value + 1
    back = 16 * (back // 10) + back % 10
    back = chr(ord("\uEB00") + back)

    if value == 0:
        back = ""

    yield f"""
        execute if score ${name} do2.gui matches {value_match}
                run data modify storage tmp tmp.{name}
                    set value "{symbols}{back}"
        """


def _card(value, value_match=None):
    if value_match is None:
        value_match = value

    symbols = (["\uE015", "\uEB04\uE016"] * 5 + ["\uE017", "\uEB04\uE018"] * 5)
    symbols *= 2
    symbols = symbols[:value]
    symbols = "".join(symbols)
    back = (value + 1) // 2
    back = 3 * back + 1
    back = 16 * (back // 10) + back % 10
    back = chr(ord("\uEB00") + back)

    if value == 0:
        back = ""

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
    yield """title @a actionbar [
            "\uEB99\uEB99\uEB99\uEB99\uEB95\uE002\uEB99\uEB39\uE004\uEB99\uEB02",
            {"nbt": "tmp.embers", "storage": "tmp"},
            {"nbt": "tmp.treasure", "storage": "tmp"},
            {"nbt": "tmp.hazard_block", "storage": "tmp"},
            {"nbt": "tmp.clank_block", "storage": "tmp"},
            "\uEA29",
            {"nbt": "tmp.cards", "storage": "tmp"}
        ]"""
