
# Missing "Dropper #7" on Deadly Difficulty
data modify block -560 109 1982 Items append value {Slot: 3b, id: "minecraft:iron_nugget", Count: 64b, tag: {RepairCost: 0, display: {Name: '{"text":"Dropper #7"}'}}}

# Missing Embers on Level 1 Jump Boost spot
data modify block -518 53 2011 Items set from block -515 46 2031 Items

# Missing items in mystery box
data modify storage tmp tmp set from block -502 104 1972 Items[0]
data modify storage tmp tmp.Slot set value 1b
data modify block -502 104 1972 Items append from storage tmp tmp

data modify storage tmp tmp set from block -507 104 1972 Items[0]
data modify storage tmp tmp.Slot set value 6b
data modify block -502 104 1972 Items append from storage tmp tmp

data remove storage tmp tmp