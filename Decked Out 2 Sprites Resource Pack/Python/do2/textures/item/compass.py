import cv2
import numpy as np

import common
from resource_pack import mcmeta, image


SETTINGS = {
    "blue_ice": {"size": (11, 11), "offset": (4, 8)},
    "magma": {
        "size": (11, 11),
        "offset": (12, 10),
        # "update": {"frametime": 5},
    },
    "sculk": {
        "size": (11, 11),
        "offset": (9, 5),
        "update": {"frametime": 15},
    },
    "soul_fire_0": {
        "size": (10, 10),
        "offset": (7, 0),
        "update": {"frametime": 3, "interpolate": True},
    },
}


COMPASS_MASK = common.read_image("Compass/compass_mask.png")[..., 3] > 0.5


def _needle():
    needle = []

    for index in range(32):
        needle.append(common.read_item_texture(f"compass_{index:02d}.png"))

    needle = np.stack(needle, axis=0)
    median_needle = np.median(needle, axis=0)

    mask = np.any(needle != median_needle, axis=-1)
    needle[..., -1] = 0.33 * mask
    mask = (needle[..., 0] > 0.7) & (needle[..., 1] < 0.1) & (needle[..., 2] < 0.1)
    needle[mask, -1] = 1.0
    return needle


def _yellow(needle):
    return needle[..., [0, 0, 1, 3]]


COMPASS_NEEDLE = _needle()
COMPASS_NEEDLE_YELLOW = _yellow(COMPASS_NEEDLE)


def _animate_ice(face):
    face = np.concatenate([face, face], axis=1)
    face = np.concatenate([face, face], axis=0)

    face = np.concatenate(
        [
            face[:, :][:16, :16],
            face[15:, :][:16, :16],
            face[15:, 1:][:16, :16],
        ],
        axis=0,
    )

    return face


def _blend(top, bottom, mask=None):
    alpha = top[..., -1][..., np.newaxis]

    ret = alpha * top + (1 - alpha) * bottom
    if mask is not None:
        ret[~mask] = 0.0
        ret[mask, -1] = 1.0
    return ret.clip(0, 1)


def _create_compass_level(level):
    FACE_NAME = {1: "blue_ice", 2: "magma", 3: "sculk", 4: "soul_fire_0"}[level]
    FACE_PATH = f"{FACE_NAME}.png"

    COMPASS_FRAME_NAME = {
        1: "frozen",
        2: "blackrock",
        3: "wooden",
        4: "warped",
    }[level]

    COMPASS_FRAME = common.read_image(f"Compass/compass_frame_{COMPASS_FRAME_NAME}.png")
    COMPASS_FACE = common.read_block_texture(FACE_PATH)

    if level == 1:
        COMPASS_FACE = _animate_ice(COMPASS_FACE)
        MCMETA = {"animation": {"frametime": 80, "interpolate": True}}
    else:
        MCMETA = common.read_block_texture_mcmeta(FACE_PATH)

    def _create_compass(index):
        texture_name = f"level{level}/compass_{index:02d}"

        @image(name=texture_name)
        def _():
            settings = SETTINGS[FACE_NAME]
            frames = []
            n_frames = COMPASS_FACE.shape[0] // 16

            w, h = settings["size"]
            x, y = settings["offset"]

            for i in range(n_frames):
                face = COMPASS_FACE[16 * i :][:16, :16]
                face = np.concatenate([face, face, face], axis=1)
                face = np.concatenate([face, face, face], axis=0)
                face = cv2.resize(face, (3 * w, 3 * h), interpolation=cv2.INTER_CUBIC)
                face = face[y:, x:][:16, :16]

                canvas = np.zeros((16, 16, 4), dtype="f4")
                canvas = _blend(face, canvas, COMPASS_MASK)
                canvas = _blend(COMPASS_FRAME, canvas, None)

                if level == 2:
                    needle = COMPASS_NEEDLE_YELLOW[index]
                else:
                    needle = COMPASS_NEEDLE[index]

                canvas = _blend(needle, canvas, None)
                frames.append(canvas)

            output = np.concatenate(frames, axis=0)
            return output.clip(0, 1)

        @mcmeta(name=texture_name)
        def _():
            return MCMETA

    for index in range(32):
        _create_compass(index)


for level in [1, 2, 3, 4]:
    _create_compass_level(level)
