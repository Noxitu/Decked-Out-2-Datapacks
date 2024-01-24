from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

data_root = Path(__file__).parent

for path in data_root.glob("gui*.png"):
    print(path.stem)
    image = plt.imread(path)[..., :3]
    image = (255 * image).astype('u1')
    RED = 122, 0, 0
    GREEN = 0, 252, 0

    mask1 = np.all(image == RED, axis=-1)
    mask2 = np.all(image == GREEN, axis=-1)

    def f(data):
        for i0, v in enumerate(data):
            if v:
                yield i0
                break

        for i1, v in enumerate(data):
            if i1 > i0 and not v:
                yield i1
                break

    def compute_rect(mask):
        rows = np.count_nonzero(mask, axis=1)
        cols = np.count_nonzero(mask, axis=0)
        y0, y1 = f(rows)
        x0, x1 = f(cols)
        
        assert np.count_nonzero(mask) == np.count_nonzero(mask[y0:y1, x0:x1])
        assert np.count_nonzero(~mask[y0:y1, x0:x1]) == 0

        return x0, y0, x1, y1

    x0, y0, x1, y1 = compute_rect(mask1)
    line1 = f"{x0} {y0} {x1} {y1}"

    x0, y0, x1, y1 = compute_rect(mask2)
    line2 = f"{x0} {y0} {x1} {y1}"
    
    path.with_suffix(".txt").write_text(f"{line1}\n{line2}\n")