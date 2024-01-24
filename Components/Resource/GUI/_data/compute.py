from pathlib import Path
import numpy as np


MAP_BORDER_SIZE = 434
MAP_SIZE = 390

data_root = Path(__file__).parent


print("ascent height")

for path in data_root.glob("gui*.txt"):
    level, file_size = map(int, path.stem.split("_")[1:])
    a1, b1, a2, b2, x1, y1, x2, y2 = map(int, path.read_text().split())

    assert abs(MAP_SIZE - (a2-a1)) <= 1
    assert abs(MAP_SIZE - (b2-b1)) <= 1

    screen_size = x2 - x1
    assert screen_size == y2 - y1

    screen2file = file_size / screen_size
    file2screen = 1 / screen2file

    target_height = np.round(MAP_SIZE * screen2file).astype(int)

    if y2 > b2:
        target_ascent = target_height
    else:
        target_ascent = target_height - int((b2 - y2) * screen2file)

    x0 = (x1 + x2) / 2

    left_offset = int((x0 - a1) * screen2file)

    print(a1, b2, x0, (1080 - y2) * screen2file)
    print(dict(screen2file=screen2file, left_offset=left_offset, ascent=target_ascent, height=target_height))

    def back(n):
        return "\\ueb99" * (n // 98) + f"\\ueb{n % 98 + 1:02d}"

    ret = back(2 * left_offset) + f"\\ue00{level}" + back(target_height + 1)

    # file_ascent = file_size

    # print(f'"{ret}"')    
    # print(target_ascent, target_height, sep=", ")
