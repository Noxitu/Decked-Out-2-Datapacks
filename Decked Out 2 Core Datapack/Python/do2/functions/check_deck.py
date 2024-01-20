from mcfunction import mcfunction


STORAGE = "storage do2:check_deck"
TAG_CARD_MARKER = "do2.tags.check_deck.card_marker"
TAG_TMP = "do2.tags.check_deck.tmp"
TMP_LOCATION = "-562 114 1983"

SCOREBOARD = "do2.check_deck"
SCOREBOARD_ID = "do2.check_deck.id"
SCOREBOARD_COUNT = "do2.check_deck.count"
SCOREBOARD_LIMIT = "do2.check_deck.limit"

DECK_LIMIT = 40


def _fill_stats():
    yield f"scoreboard players reset * {SCOREBOARD}"

    stats = {
        "$deck_size": "",
        "$ethereal": "ethereal: true",
        "$permanent": "permanent: true",
        "$rarity_common": 'rarity: "common"',
        "$rarity_uncommon": 'rarity: "uncommon"',
        "$rarity_rare": 'rarity: "rare"',
        "$rarity_shop": 'rarity: "shop"',
    }

    for title, selector in stats.items():
        yield f"scoreboard players set {title} {SCOREBOARD} 0"
        if selector:
            selector = f",nbt={{data:{{{selector}}}}}"

        yield f"""
            execute as @e[tag={TAG_CARD_MARKER}{selector}]
                    run scoreboard players operation 
                        {title} {SCOREBOARD} += @s {SCOREBOARD_COUNT}
            """


@mcfunction(skip=True)
def _():
    import data
    yield "say check_deck start"

    yield f"scoreboard objectives add {SCOREBOARD} dummy"
    yield f"scoreboard objectives add {SCOREBOARD_COUNT} dummy"
    yield f"scoreboard objectives add {SCOREBOARD_LIMIT} dummy"
    yield f"scoreboard objectives add {SCOREBOARD_ID} dummy"
    yield f"scoreboard objectives setdisplay sidebar {SCOREBOARD}"

    yield f"""data modify {STORAGE} Deck
                set from block -565 114 1980 Items
        """

    yield f"kill @e[tag={TAG_CARD_MARKER}]"
    
    for card_name, card_info in data.CARD_INFO.items():
        escaped_name = card_name.replace("'", "\\'")

        yield f"""summon minecraft:marker {TMP_LOCATION} {{
                    CustomName: '"{escaped_name}"',
                    Tags: ["{TAG_CARD_MARKER}"],
                    data: {{
                        id: {card_info["id"]},
                        limit: {card_info["limit"]},
                        rarity: "{card_info["rarity"]}",
                        permanent: {"true" if card_info["permanent"] else "false"},
                        ethereal: {"true" if card_info["ethereal"] else "false"}
                    }}
        }}"""

    yield f"""
        execute as @e[tag={TAG_CARD_MARKER}]
                store result score @s {SCOREBOARD_ID}
                run data get entity @s data.id
        """

    yield f"""
        execute as @e[tag={TAG_CARD_MARKER}]
                store result score @s {SCOREBOARD_LIMIT}
                run data get entity @s data.limit
        """

    for card_name, card_nbt in data.NBT.CARDS.items():
        card_info = data.CARD_INFO[card_name]

        selector = f"""Deck[{{
                "id": "{card_nbt["id"]}",
                "tag": {{CustomModelData: {card_nbt["tag"]["CustomModelData"]}}}
            }}]"""

        yield f"""
            execute if data {STORAGE} {selector}
                    run data modify {STORAGE} {selector}.CardId
                        set value {card_info["id"]}
            """
        
    yield f"function {check_first_item}"

    yield f"""
        execute as @e[tag={TAG_CARD_MARKER}]
                if score @s {SCOREBOARD_COUNT} > @s {SCOREBOARD_LIMIT}
                run function {report_too_many_cards}
        """
    
    yield from _fill_stats()
    
    yield f"""
        execute unless score $deck_size {SCOREBOARD} matches ..{DECK_LIMIT}
                run function {report_too_large_deck}
        """

    yield "say check_deck done"


@mcfunction
def check_first_item():
    yield f"execute unless data {STORAGE} Deck[0] run return 0"
    yield f"execute unless data {STORAGE} Deck[0].CardId run function {report_invalid_item}"
    yield f"execute if data {STORAGE} Deck[0].CardId run function {check_first_card}"
    yield f"data remove {STORAGE} Deck[0]"
    yield f"function {check_first_item}"


@mcfunction
def check_first_card():
    yield f"""
        execute store result score $current_card_id {SCOREBOARD}
                run data get {STORAGE} Deck[0].CardId 
        """

    yield f"""
        execute store result score $current_card_count {SCOREBOARD}
                run data get {STORAGE} Deck[0].Count
        """

    yield f"""
        execute as @e[tag={TAG_CARD_MARKER}]
                if score @s {SCOREBOARD_ID} = $current_card_id {SCOREBOARD}
                run scoreboard players operation 
                    @s {SCOREBOARD_COUNT} += $current_card_count {SCOREBOARD}"""


@mcfunction
def report_invalid_item():
    tmp = f"@e[tag={TAG_TMP},limit=1]"
    yield f"""summon minecraft:item {TMP_LOCATION} {{
            Item: {{
                "id": "minecraft:iron_nugget",
                "Count": 1
            }},
            Tags: ["{TAG_TMP}"]
        }}"""

    yield f"""
        data modify entity {tmp} Item
            set from {STORAGE} Deck[0]
        """

    yield f"""
        execute positioned -558 113 1980
                run tellraw @a[distance=..8] [
                    {{"text": ""}},
                    {{"text": "[!]", "color": "red"}},
                    {{"text": " Deck contains invalid item: "}},
                    {{"selector": "{tmp}"}},
                    {{"text": "."}}
                ]
        """
    
    yield f"kill {tmp}"


@mcfunction
def report_too_many_cards():
    yield f"""
        execute positioned -558 113 1980
                run tellraw @a[distance=..8] [
                    {{"text": ""}},
                    {{"text": "[!]", "color": "red"}},
                    {{"text": " Deck contains too many cards: "}},
                    {{"selector": "@s"}},
                    {{"text": ". ["}},
                    {{"score": {{"name": "@s","objective": "{SCOREBOARD_COUNT}"}} }},
                    {{"text": "/"}},
                    {{"score": {{"name": "@s","objective": "{SCOREBOARD_LIMIT}"}} }},
                    {{"text": "]"}}
                ]
        """
    
@mcfunction
def report_too_large_deck():
    yield f"""
        execute positioned -558 113 1980
                run tellraw @a[distance=..8] [
                    {{"text": ""}},
                    {{"text": "[!]", "color": "red"}},
                    {{"text": " Deck contains too many cards in total."}},
                    {{"text": " ["}},
                    {{"score": {{"name": "$deck_size","objective": "{SCOREBOARD}"}} }},
                    {{"text": "/{DECK_LIMIT}"}},
                    {{"text": "]"}}
                ]
        """