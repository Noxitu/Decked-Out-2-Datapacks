import cv2
import numpy as np

from resource_pack import image
from common import read_image


WATCH = read_image("Watch/watch.png")
WATCH_MASK = read_image("Watch/watch_mask.png")[..., 3] > 0.5
WATCH_FACE = read_image("Watch/watch_face.png")

WATCH_CENTER = 15, 16
WATCH_SIZE = 32, 32


def _rotate(image, angle, center=(16, 16)):
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, rotation_matrix, WATCH_SIZE, flags=cv2.INTER_LANCZOS4)


def _create_clock(index):
    texture_name = f"clock_{index:02d}"

    @image(name=texture_name)
    def _():
        angle = 57.5 - index * 360 / 64

        face = _rotate(WATCH_FACE, angle, WATCH_CENTER)

        alpha = WATCH[..., -1].copy()
        output_alpha = alpha.copy()

        alpha[~WATCH_MASK] = 1.0
        alpha = alpha[..., np.newaxis]
        output_alpha[WATCH_MASK] = 1.0

        output = alpha * WATCH + (1 - alpha) * face
        output[..., -1] = output_alpha
        output = output.clip(0, 1)

        return output


for index in range(64):
    _create_clock(index)
