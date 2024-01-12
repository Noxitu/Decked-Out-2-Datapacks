from resource_pack import json


def _create_compass(level, index):
    model_name = (
        f"level{level}/compass" if index == 16 else f"level{level}/compass_{index:02d}"
    )
    texture_name = f"do2:item/compass/level{level}/compass_{index:02d}"

    @json(name=model_name)
    def _():
        return {
            "parent": "minecraft:item/generated",
            "textures": {"layer0": texture_name},
        }


for level in [1, 2, 3, 4]:
    for index in range(32):
        _create_compass(level, index)
