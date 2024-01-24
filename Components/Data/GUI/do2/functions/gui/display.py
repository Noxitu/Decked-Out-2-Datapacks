from noxpack import mcfunction

SCOREBOARD = "do2.gui"
STORAGE = "do2:gui"


@mcfunction(tags=["minecraft:load"])
def init_storage():
    yield f"""data modify storage {STORAGE} CurrentLevels set value {{embers: -1, treasure: -1, hazard_block: -1, clank_block: -1, cards: -1}}"""

    for i in range(1, 5):
        yield f"""give Noxitu minecraft:paper{{
            display: {{
                Name: '"GUI Level {i}"'
            }},
            Do2GuiLevel: {i}
        }}"""


def _create_update(name):
    @mcfunction(name=f"update_{name}")
    def _():
        yield f"""
            execute store result storage {STORAGE} CurrentLevels.{name} int 1
                    run scoreboard players get #current {SCOREBOARD}
            """
        
        n = {"cards": 40}.get(name, 15)

        for i in range(n+1):
            yield f"""
                execute if score #current {SCOREBOARD} matches {i}
                        run data modify storage {STORAGE} Text.{name}
                            set from storage {STORAGE} Text.{name}{i}
                """

for name in ["embers", "treasure", "hazard_block", "clank_block", "cards"]:
    _create_update(name)

@mcfunction
def update():
    for name in ["embers", "treasure", "hazard_block", "clank_block", "cards"]:
        max_level = {"cards": 40}.get(name, 15)
        yield f"""
            scoreboard players operation 
                #current {SCOREBOARD} = ${name} {SCOREBOARD}
            """
        
        yield f"""
            execute if score #current {SCOREBOARD} matches {max_level+1}..
                    run scoreboard players set #current {SCOREBOARD} {max_level}
            """
        
        yield f"""
            execute store result score #previous {SCOREBOARD}
                    run data get storage {STORAGE} CurrentLevels.{name}
            """
        
        yield f"""
            execute unless score #current {SCOREBOARD} = #previous {SCOREBOARD}
                    run function do2:gui/display/update_{name}
            """
        
def _create_level(level):
    @mcfunction(name=f"gui{level}.check_player")
    def check_player():
        yield f"""title @s actionbar [
            {{"text": "", "font": "do2:gui"}},
            {{"nbt": "Text.offset.Level{level}", "storage": "{STORAGE}"}},
            {{"nbt": "Text.map.Level{level}", "storage": "{STORAGE}"}},
            {{"nbt": "Text.embers.Level{level}", "storage": "{STORAGE}"}},
            {{"nbt": "Text.treasure.Level{level}", "storage": "{STORAGE}"}},
            {{"nbt": "Text.hazard_block.Level{level}", "storage": "{STORAGE}"}},
            {{"nbt": "Text.clank_block.Level{level}", "storage": "{STORAGE}"}},
            {{"nbt": "Text.cards.Level{level}", "storage": "{STORAGE}"}}
        ]"""

    @mcfunction(tags=["minecraft:tick"], name=f"gui{level}.invoke")
    def _():
        yield f"""
            execute unless data storage {STORAGE} Text.embers
                    run return 0
            """

        yield f"""
            execute as @a[nbt={{
                        SelectedItem: {{
                            tag:{{
                                Do2GuiLevel: {level}
                            }}
                        }}
                    }}] 
                    run function {check_player}
            """

for level in range(1, 5):
    _create_level(level)
