from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import cv2

from noxpack import png
from .dungeon_logs import paper_list


BRILLIANCE_PATH = Path(__file__).resolve().parents[5] / "trackedout/Brilliance/Brilliance Resourcepack/assets"
MINECRAFT_PATH = Path(__file__).resolve().parents[6] / "Minecraft/Data/Versions/1.20.1/assets"
SELF = Path(__file__).resolve().parent


def imread(name):
    if name == "do2:item/paper":
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


PAPER = imread("do2:item/paper")


def _create_texture(name):
    @png(name=f"item/dungeon_log/paper_{name}")
    def _():
        if name == "skull":
            icon = plt.imread(SELF / "_skull.png")
            icon = 255 * icon
            icon = (icon - 20) * 255 / (175 - 20)
            icon = icon.clip(0, 255).astype("u1")
            icon = np.concatenate([icon, 255 - icon[..., 0:1]], axis=-1)
        else:
            icon = imread(f"do2:item/artifacts/{name}")

        size = 48
        k2 = size / 128
        x1, x2, y1, y2 = -16, 48, -24, 56
        k1 = icon.shape[0] / 32
        paper = cv2.resize(PAPER, (size, size), interpolation=cv2.INTER_NEAREST)
        P = cv2.getPerspectiveTransform(
            k1 * np.array([x1, y1, x2, y1, x2, y2, x1, y2]).astype('f4').reshape(4, 1, 2), 
            k2 * np.array([80, 14.7, 125, 59.8, 54.3, 111.7, 8.6, 64.7]).astype('f4').reshape(4, 1, 2), 
        )
        # icon2 = cv2.warpPerspective(icon, P, (size, size), flags=cv2.INTER_NEAREST)
        icon2 = cv2.warpPerspective(icon, P, (size, size), flags=cv2.INTER_CUBIC)
        canvas = paper.copy()

        a1 = icon2[..., -1].astype('f4') / 255
        a2 = (1 - a1) * canvas[..., -1].astype('f4') / 255
        a = a1 + a2
        a = a.clip(0.001, None)

        canvas = icon2 * (a1 / a)[..., np.newaxis] + canvas * (a2 / a)[..., np.newaxis]
        canvas[..., -1] = 255 * a
        canvas = canvas.clip(0, 255).astype("u1")
        return canvas

for name in paper_list():
    _create_texture(name)
