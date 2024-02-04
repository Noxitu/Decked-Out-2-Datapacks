from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from noxpack import png


BRILLIANCE_PATH = Path(__file__).resolve().parents[6] / "trackedout/Brilliance/Brilliance Resourcepack/assets"
MINECRAFT_PATH = Path(__file__).resolve().parents[7] / "Minecraft/Data/Versions/1.20.1/assets"


def image_list(path):
    glob = (BRILLIANCE_PATH / path.replace(":", "/textures/")).glob("*.png")
    return [path.stem for path in glob]


def imread(name):
    if name == "do2:item/sweet_berries":
        name = name.replace("do2:", "minecraft:")
        root = MINECRAFT_PATH
    else:
        root = BRILLIANCE_PATH

    image = plt.imread((root / name.replace(":", "/textures/")).with_suffix(".png"))
    image = (255 * image).astype("u1")

    if name == "do2:item/artifacts/tntslab":
        assert image.shape == (64, 256, 4), f"Invalid shape: {image.shape}"
        image = image[:, 128:][:, :64]
        image[32:] = 0

    return image


def png_array(call):
    @png(name=call.__name__)
    def _():
        names = []
        
        for item in call():
            if isinstance(item, str):
                names.append(item)
            elif isinstance(item, tuple) and len(item) == 2 and isinstance(item[1], list):
                prefix, item = item
                names.extend(prefix + name for name in item)
            else:
                names.extend(item)
    
        textures = [
            imread(f"do2:item/{name}") for name in names
        ]

        for texture in textures:
            texture[-1, -1] = (60, 60, 60, 1)

        return np.concatenate(textures, axis=1)


@png_array
def icons16():
    yield "do_coin", "do_crown", "do_ember", "do_tome"
    yield "sweet_berries"

@png_array
def icons32():
    artifacts = image_list("do2:/item/artifacts")
    artifacts = [a for a in artifacts if a != "tntslab"]
    print(f"::       Got {len(artifacts)} artifacts.")
    yield "artifacts/", artifacts

@png_array
def icons64():
    yield "keys/", ["do_key1_64", "do_key4_64", "do_key6_64", "toolbox", "do_key3_64"]
    yield "artifacts/tntslab"
