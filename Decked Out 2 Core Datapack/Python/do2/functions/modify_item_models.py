from mcfunction import mcfunction


def _modify_compass(dropper_idx, model, slots=["{}"]):
    for slot in slots:
        yield f"""data modify block -549 106 {1979-dropper_idx} Items[{slot}].tag.CustomModelData set value {model}"""


@mcfunction(tags=["do2:fix_dungeon"])
def _():
    # Modify Compasses
    yield from _modify_compass(0, 1)
    yield from _modify_compass(1, 1)
    yield from _modify_compass(2, 1)
    yield from _modify_compass(3, 2)
    yield from _modify_compass(4, 2)
    yield from _modify_compass(5, 2)
    yield from _modify_compass(5, 3, [6, 7])
    yield from _modify_compass(6, 3)
    yield from _modify_compass(7, 3)
    yield from _modify_compass(7, 4, [6, 7])
    yield from _modify_compass(8, 4)
    yield from _modify_compass(9, 4)

    # yield "data modify block -625 59 1945 Items[{}].tag.CustomModelData set value 201"
