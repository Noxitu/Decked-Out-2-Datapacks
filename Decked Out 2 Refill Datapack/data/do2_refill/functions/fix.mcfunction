
# Apply one-time fixes

function do2_refill:check_loaded

tellraw @s {"text": "Runing one-time fixes..."}

function do2_refill:fix_droppers
function do2_refill:fix_dungeon
function do2_refill:fix_redstone

tellraw @s {"text": "Fixed dungeon."}
