
tellraw @s [{"text": ""}]
tellraw @s [{"color": "aqua", "text": "[Fix Dungeon]"}, {"color": "#bbbbbb", "text": " applies one-time fixes to dungeon, like filling some holes, fixing redstone or refilling completly empty droppers."}]
tellraw @s [{"text": ""}]
tellraw @s [{"color": "aqua", "text": "[Refill Droppers]"}, {"color": "#bbbbbb", "text": " sets all item counts in known droppers to 64. It requires item to be already in that dropper - but if you change some items (e.g. coins to crowns) that change will be preserved."}]
tellraw @s [{"text": ""}]
tellraw @s {"color": "#bbbbbb", "text": "For more automation you can put `function do2_refill:refill_droppers` in a command block and connect it to some existing redstone (e.g. to the button at -561 115 1974)."}
tellraw @s [{"text": ""}]
tellraw @s [{"color": "#bbbbbb", "text": "You are new "}, {"color": "gold", "text": "Dungeon Master"}, {"color": "#bbbbbb", "text": " now."}]
tellraw @s [{"color": "#bbbbbb", "text": "Use "}, {"color": "aqua", "text": "[right click]"}, {"color": "#bbbbbb", "text": " on signs to trigger dungeon maintenence."}]
tellraw @s [{"text": ""}]


fill -480 113 1968 -480 115 1971 minecraft:stone

setblock -481 114 1969 minecraft:warped_wall_sign[facing=west]{front_text: {messages: ['""', '"Fix"', '"Dungeon"', '{"text": "", "clickEvent": {"action": "run_command", "value": "function do2_refill:fix"}}'], has_glowing_text:1b, color: "white"}}
setblock -481 114 1970 minecraft:warped_wall_sign[facing=west]{front_text: {messages: ['""', '"Refill"', '"Droppers"', '{"text": "", "clickEvent": {"action": "run_command", "value": "function do2_refill:refill_droppers"}}'], has_glowing_text:1b, color: "white"}}
setblock -481 114 1971 minecraft:warped_wall_sign[facing=west]{front_text: {messages: ['"Empty"', '"Waste"', '"Barrels"', '{"text": "", "clickEvent": {"action": "run_command", "value": "function do2_refill:empty_barrels"}}'], has_glowing_text:1b, color: "white"}}
