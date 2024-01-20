import json
from pathlib import Path
import sys

import matplotlib.pyplot as plt


class FileDatabase:
    def __init__(self, path):
        self._path = path
        self._data_obj = None

    def _data(self):
        if self._data_obj is None:
            with open(self._path, encoding='utf-8') as fd:
                self._data_obj = json.load(fd)     

        return self._data_obj

    def __getitem__(self, key):
        return self._data().__getitem__(key)

    def __iter__(self):
        return self._data().__iter__()
    
    def items(self):
        return self._data().items()


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
                    Items = []

                new_parent = NewParent()
                setattr(parent, part, new_parent)
                if hasattr(parent, "Items"):
                    parent.Items.append(new_parent)

            parent = getattr(parent, part)

        name = path.stem.lstrip('_').upper()
        data = FileDatabase(path)
        setattr(parent, name, data)
        if hasattr(parent, "Items"):
            parent.Items.append(data)


def imread(path):
    path = Path(__file__).parents[1] / 'Data' / path
    return plt.imread(path)


_init()
