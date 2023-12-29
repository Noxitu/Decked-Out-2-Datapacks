execute store result score last_slot do2_refill run data get entity @p recipeBook.isGuiOpen
scoreboard players set next_index do2_refill 0
schedule function do2_refill:dev/tp_pos2 5t

