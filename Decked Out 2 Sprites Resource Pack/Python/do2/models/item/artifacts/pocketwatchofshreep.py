from resource_pack import json


def _create_clock(index):
    model_name = "clock" if index == 0 else f"clock_{index:02d}"
    texture_name = f"do2:item/artifacts/pocketwatchofshreep/clock_{index:02d}"

    @json(name=model_name)
    def _():
        return {
            "parent": "minecraft:item/generated",
            "textures": {"layer0": texture_name},
        }


for index in range(64):
    _create_clock(index)
