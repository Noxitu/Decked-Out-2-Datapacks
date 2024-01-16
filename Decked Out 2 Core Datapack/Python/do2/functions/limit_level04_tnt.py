from mcfunction import mcfunction


@mcfunction(tags=["do2:fix_dungeon"])
def _():
    yield """
        data modify block -640 17 1904 Items
            set value [{Slot: 4b, id: "minecraft:tnt", Count: 1b}]
    """
