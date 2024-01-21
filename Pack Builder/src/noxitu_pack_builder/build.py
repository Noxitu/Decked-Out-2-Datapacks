import importlib
from pathlib import Path
import sys

from .utils import load_json

import noxpack
from noxitu_pack_builder.context import context
import noxitu_pack_builder.output_file
import noxitu_pack_builder.tags


def _create_copy(path, root):
    @noxpack.copy(path=path.relative_to(root))
    def _():
        return path

def _import(path, root):
    path = path.relative_to(root)
    path = ".".join(path.parts[:-1]) + f".{path.stem}"
    root = str(root)

    sys.path.append(root)

    importlib.import_module(path)

    last = sys.path.pop()
    assert last is root


def _build_pack(config):
    print("\033[32m::\033[m Pack", config["name"])
    root = Path(".")
    output_root = root / "Generated Packs"
    assert output_root.is_dir()
    output_root = output_root / config["name"]

    with context:
        @noxpack.json(path="pack.mcmeta", no_root=True, suffix=None)
        def _():
            return {"pack": {"pack_format": 15, "description": config["description"]}}

        @noxpack.copy(path="pack.png", no_root=True)
        def _():
            return root / "pack.png"
        
        if config["type"] == "datapack":
            noxitu_pack_builder.tags.get_tag("minecraft:load")
            noxitu_pack_builder.tags.get_tag("minecraft:tick")

        content_root = {
            "datapack": "data",
            "resource_pack": "assets"
        }[config["type"]]

        components_root = {
            "datapack": root / "Components/Data",
            "resource_pack": root / "Components/Resource",
        }[config["type"]]

        for component_name in config["components"]:
            if component_name.startswith("-"):
                continue

            component_root = components_root / component_name
            
            for png_path in component_root.rglob("*.png"):
                _create_copy(png_path, component_root)

            for py_path in component_root.rglob("*.py"):
                _import(py_path, component_root)

        noxitu_pack_builder.output_file.save_outputs(output_root, root=content_root)


def main():
    config_path = Path(sys.argv[1])
    configs = load_json(config_path)

    for config in configs:
        if any(config[key].startswith("-") for key in ("name", "type")):
            continue
        _build_pack(config)


if __name__ == "__main__":
    main()
