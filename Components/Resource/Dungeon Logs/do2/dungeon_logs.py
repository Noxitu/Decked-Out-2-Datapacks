from pathlib import Path
from noxpack import json

BRILLIANCE_PATH = Path(__file__).resolve().parents[5] / "trackedout/Brilliance/Brilliance Resourcepack/assets"

def paper_list():
    path = "do2/textures/item/artifacts"
    glob = (BRILLIANCE_PATH / path).glob("*.png")
    return ["skull"] + [path.stem for path in glob]


def _create_model(name):
    @json(path=f"do2/models/item/dungeon_log/paper_{name}")
    def _():
        return {
            "parent": "item/generated",
            "textures": {
                "layer0": f"do2:item/dungeon_log/paper_{name}",
            }
        }

for name in paper_list():
    _create_model(name)