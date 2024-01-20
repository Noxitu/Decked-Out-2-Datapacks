from mcfunction import mcfunction


def filler(slot, count=1):
    return f"""{{
        id: "minecraft:iron_nugget",
        Count: {count}b,
        Slot: {slot}b,
        tag: {{
            display: {{Name: '"Hopper Filler Item"'}},
            isFiller: true
        }}
    }}"""


SPEEDRUNNER = """{
        id: "minecraft:iron_nugget",
        Count: 1b,
        Slot: 0b,
        tag: {
            CustomRoleplayData: 1b, 
            NameFormat: {
                OriginalName: '{"color":"#3C44AA","text":"≡ Speed Runner ≡"}',
                ModifiedName: '{"color":"#3C44AA","text":"≡ Speed Runner ≡"}',
                color: "#3c44aa"
            },
            CustomModelData: 125,
            display: {
                Name: '{"color":"#3C44AA","text":"≡ Speed Runner ≡"}'
            }
        }
    }"""

SPEEDRUNNER2 = """{
        id: "minecraft:gold_ingot",
        Count: 1b,
        Slot: 1b,
        tag: {
            CustomModelData: 335,
            display: {
                Name: '{"color":"gold", "text":"✲≡ Speed Runner ≡✲"}'
            }
        }
    }"""


@mcfunction
def setup_card_processors():
    yield f"""
        data modify block -544 40 1913 Items
            set value [
                {SPEEDRUNNER},
                {SPEEDRUNNER2},
                {filler(2, 18)},
                {filler(3, 1)},
                {filler(4, 1)}
            ]
"""
    
    yield f"""
        setblock -544 38 1916 minecraft:glass
    """

    yield f"""
        setblock -544 38 1916 minecraft:command_block{{Command: "function {check_current_card}"}}
    """


@mcfunction
def check_current_card():
    yield """
        execute unless data block ~ ~2 ~-3 Items[{Slot: 0b, Count: 1b}]
                run say Normal Card
        """

    yield """
        execute unless data block ~ ~2 ~-3 Items[{Slot: 0b, Count: 1b}]
                run setblock ~ ~ ~-1 minecraft:repeater[facing=south,powered=true]
        """
    
    yield """
        execute unless data block ~ ~2 ~-3 Items[{Slot: 0b, Count: 1b}]
                run return 0
        """
    
    yield """say Ethereal Card"""
    yield """setblock ~ ~ ~-1 minecraft:glass"""

    yield """
        data modify block ~ ~2 ~-3 Items[{Slot: 1b}].Count
            set value 1
        """