def create_egg(name):
    return {
        "parent": "custom:item/egg/gold",
        "textures": {"2": f"eggs:item/{name}", "particle": f"eggs:item/{name}"},
    }
