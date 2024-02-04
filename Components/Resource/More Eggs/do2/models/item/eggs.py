from pathlib import Path

from noxpack import json


TEXTURES = Path(__file__).parents[2] / "textures/item/eggs"

def _create_egg(name):
    @json(name=name)
    def _():
        return {
            "parent": "custom:item/egg/gold",
            "textures": {
                "2": f"do2:item/eggs/{name}",
                "particle": f"do2:item/eggs/{name}"
            }
        }
    

for name in TEXTURES.glob("*.png"):
    name = name.stem
    if name.startswith("_"):
        continue

    _create_egg(name)