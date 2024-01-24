import numpy as np
from noxpack import png

CANVAS_SIZE = 128
SIZE = 5
Y0 = 34
Y_STEP = 23

COLORS = [
    [(40, 99, 95), (178, 178, 174), (49, 121, 116), (78, 186, 177), (217, 217, 213)],
    [(150, 88, 34), (178, 174, 162), (184, 107, 41), (212, 202, 62), (217, 214, 199)], 
    [(78, 1, 0), (178, 0, 0), (95, 1, 0), (130, 43, 41), (217, 0, 0)], 
    [(36, 52, 118), (178, 177, 169), (43, 64, 144), (136, 136, 207), (217, 217, 207)],
]

BLUE = (63, 63, 240, 255)

def _create_ticks(colors):
    ret = np.full((SIZE, SIZE, 4), 255, dtype="u1")

    assert SIZE == 5
    ret[..., :3] = colors[2]
    ret[0, :, :3] = colors[1]
    ret[0, 0, :3] = colors[0]
    ret[1:-1, 1:-1, :3] = colors[3]
    ret[1:-1, -1, :3] = colors[4]

    return ret

@png
def _():
    n_sprites = 8
    canvas = np.zeros((CANVAS_SIZE, n_sprites * SIZE, 4), dtype="u1")

    for i in range(n_sprites):
        x1 = i * SIZE
        x2 = x1 + SIZE
        y1 = Y0 + (i % 4) * Y_STEP
        y2 = y1 + SIZE

        sprite_type = i // 4

        if sprite_type == 0:
            sprite = _create_ticks(COLORS[i])
        elif sprite_type == 1:
            sprite = BLUE

        canvas[y1:y2, x1:x2] = sprite

    return canvas
