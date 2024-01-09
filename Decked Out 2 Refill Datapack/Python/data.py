import json
from pathlib import Path
import sys

import matplotlib.pyplot as plt


def _init():
    root = Path(__file__).parents[2] / 'Decked Out 2 Database'
    module = sys.modules[__name__]

    for path in root.rglob("*.json"):
        parent = module
        parts = path.relative_to(root).parts[:-1]

        for part in parts:
            part = part.upper().lstrip('_')

            if not hasattr(parent, part):
                class NewParent:
                    pass
                setattr(parent, part, NewParent())

            parent = getattr(parent, part)

        name = path.stem.lstrip('_').upper()
        with open(path, encoding='utf-8') as fd:
            data = json.load(fd)
            setattr(parent, name, data)


def imread(path):
    path = Path(__file__).parents[1] / 'Data' / path
    return plt.imread(path)


_init()
