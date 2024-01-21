from noxpack import mcfunction
from .validate_deck import _ as validate_deck
from .validate_deck import remove_redstone

@mcfunction(tags=["minecraft:load"])
def _():
    pos = "-568 114 1980"
    command = f"function {validate_deck}"

    yield f"""
        execute unless loaded {pos}
                run schedule function {_} 16s replace
        """
    
    yield f"setblock {pos} minecraft:glass"
    yield f"""setblock {pos} minecraft:command_block{{Command: "{command}"}}"""
    yield from remove_redstone()