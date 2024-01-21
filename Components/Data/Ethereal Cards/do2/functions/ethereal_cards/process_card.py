from noxpack import mcfunction


@mcfunction
def _():
    hopper_pos = "~ ~3 ~-3"
    repeater_pos = "~ ~1 ~-1"

    yield f"""
        execute unless data block {hopper_pos} Items[{{Slot: 0b, Count: 1b}}]
                run say Normal Card
        """

    yield f"""
        execute unless data block {hopper_pos} Items[{{Slot: 0b, Count: 1b}}]
                run setblock {repeater_pos} minecraft:repeater[facing=south,powered=true]
        """
    
    yield f"""
        execute unless data block {hopper_pos} Items[{{Slot: 0b, Count: 1b}}]
                run return 0
        """
    
    yield """say Ethereal Card"""
    yield f"""setblock {repeater_pos} minecraft:glass"""

    yield f"""
        data modify block {hopper_pos} Items[{{Slot: 1b}}].Count
            set value 1
        """
