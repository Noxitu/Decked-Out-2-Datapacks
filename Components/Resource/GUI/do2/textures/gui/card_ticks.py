import numpy as np
from noxpack import png

CANVAS_SIZE = 128
WIDTH = 2
HEIGHT = 3
Y0 = 115
Y_STEP = 5

COLORS = [
    [(178, 177, 169), (217, 217, 207)],
    [(138, 138, 132), (169, 169, 161)],
]

BLUE = (63, 63, 240, 255)

def _create_ticks(colors):
    ret = np.full((HEIGHT, WIDTH, 4), 255, dtype="u1")

    ret[..., :3] = colors[1]
    ret[0, :, :3] = colors[0]

    return ret

@png
def _():
    n_sprites = 6
    canvas = np.zeros((CANVAS_SIZE, n_sprites * WIDTH, 4), dtype="u1")

    for i in range(n_sprites):
        color_i = i // 3

        x1 = i * WIDTH
        x2 = x1 + WIDTH

        y1 = Y0
        y2 = y1 + HEIGHT
        y3 = Y0 + Y_STEP
        y4 = y3 + HEIGHT


        sprite1 = _create_ticks(COLORS[color_i]) if (i % 3) >= 1 else BLUE
        sprite2 = _create_ticks(COLORS[color_i]) if (i % 3) >= 2 else BLUE

        canvas[y1:y2, x1:x2] = sprite1
        canvas[y3:y4, x1:x2] = sprite2

    return canvas
