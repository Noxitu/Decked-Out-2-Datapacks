from noxpack import mcfunction
import data


STORAGE = "storage do2:deck_validation"
TAG_CARD_MARKER = "do2.tags.deck_validation.card_marker"
TAG_TMP = "do2.tags.deck_validation.tmp"
TMP_LOCATION = "-562 114 1983"

SCOREBOARD = "do2.deck_validation"
SCOREBOARD_ID = "do2.deck_validation.id"
SCOREBOARD_COUNT = "do2.deck_validation.count"
SCOREBOARD_LIMIT = "do2.deck_validation.limit"

TELLRAW_PREFIX = "execute positioned -558 113 1980 run tellraw @a[distance=..8]"

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


@mcfunction
def _():
    yield f"""{TELLRAW_PREFIX} "Starting Deck Validation..." """

    yield f"scoreboard objectives add {SCOREBOARD} dummy"
    yield f"scoreboard objectives add {SCOREBOARD_COUNT} dummy"
    yield f"scoreboard objectives add {SCOREBOARD_LIMIT} dummy"
    yield f"scoreboard objectives add {SCOREBOARD_ID} dummy"
    yield f"scoreboard objectives setdisplay sidebar {SCOREBOARD}"

    yield f"""data modify {STORAGE} Deck
                set from block -565 114 1980 Items
        """

    yield f"kill @e[tag={TAG_CARD_MARKER}]"

    yield f"function #do2:deck_validation/summon_card_markers"

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

    yield f"function #do2:deck_validation/add_card_ids"

    yield f"data modify {STORAGE} ValidationStatus set value {{Valid: true}}"

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

    yield f"kill @e[tag={TAG_CARD_MARKER}]"

    yield f"""{TELLRAW_PREFIX} "Finished Deck Validation." """

    yield f"execute if data {STORAGE} ValidationStatus{{Valid: true}} run function {handle_valid_deck}"
    yield f"execute if data {STORAGE} ValidationStatus{{Valid: false}} run function {handle_invalid_deck}"


@mcfunction(tags=["do2:deck_validation/summon_card_markers"])
def summon_card_markers():
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


@mcfunction(tags=["do2:deck_validation/add_card_ids"])
def add_card_ids():
    for card_name, card_nbt in data.NBT.CARDS.items():
        card_info = data.CARD_INFO[card_name]
        model = card_nbt["tag"]["CustomModelData"]
        display_name = card_nbt["tag"]["display"]["Name"].replace("'", "\\'")

        selector = f"""Deck[{{
                "id": "{card_nbt["id"]}",
                "tag": {{
                    CustomModelData: {model},
                    display: {{
                        Name: '{display_name}'
                    }}
                }}
            }}]"""

        yield f"""
            execute if data {STORAGE} {selector}
                    run data modify {STORAGE} {selector}.CardId
                        set value {card_info["id"]}
            """


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
    yield f"data modify {STORAGE} ValidationStatus.Valid set value false"

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
        execute as {tmp}
                run data modify entity @s CustomName 
                    set from entity @s Item.tag.display.Name
        """

    yield f"""
        {TELLRAW_PREFIX} [
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
    yield f"data modify {STORAGE} ValidationStatus.Valid set value false"

    yield f"""
        {TELLRAW_PREFIX} [
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
    yield f"data modify {STORAGE} ValidationStatus.Valid set value false"

    yield f"""
        {TELLRAW_PREFIX} [
                    {{"text": ""}},
                    {{"text": "[!]", "color": "red"}},
                    {{"text": " Deck contains too many cards in total."}},
                    {{"text": " ["}},
                    {{"score": {{"name": "$deck_size","objective": "{SCOREBOARD}"}} }},
                    {{"text": "/{DECK_LIMIT}"}},
                    {{"text": "]"}}
                ]
        """


@mcfunction
def handle_valid_deck():
    yield f"""{TELLRAW_PREFIX} {{"text": "Deck is valid.", "color": "#00ff00"}} """
    yield f"""setblock -568 113 1980 minecraft:redstone_wire"""
    yield f"""setblock -568 115 1980 minecraft:redstone_wire"""
    yield f"""schedule function {remove_redstone} 5s replace"""


@mcfunction
def handle_invalid_deck():
    yield f"""{TELLRAW_PREFIX} {{"text": "Deck is invalid.", "color": "#ff0000"}} """
    yield from remove_redstone()
    yield f"""
        execute positioned -558 113 1980
            run playsound do2:halloween.failure master @a[distance=..8]
        """
    yield f"schedule function {uninstall_deck} 1s replace"

@mcfunction
def remove_redstone():
    yield f"""setblock -568 113 1980 minecraft:air"""
    yield f"""setblock -568 115 1980 minecraft:air"""

@mcfunction
def uninstall_deck():
    yield f"setblock -565 117 1980 minecraft:redstone_block"
    yield f"schedule function {uninstall_deck_reset} 12t replace"


@mcfunction
def uninstall_deck_reset():
    yield "setblock -565 117 1980 minecraft:air"