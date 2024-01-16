from mcfunction import mcfunction


@mcfunction(tags=["do2:fix_dungeon"])
def _():
    yield "setblock -544 112 1981 minecraft:gray_shulker_box[facing=down]"
    
    yield """data merge entity 071af318-9860-4d54-b61a-1f1851265429 {
        Invulnerable: false, 
        NoGravity: true,
        Invisible: true,
        DisabledSlots: 4194303, 
        Rotation: [-90.0f, 0.0f],
        HandItems: [{}, {}],
        Pos: [-544.5d, 113.0d, 1980.5d], 
        ArmorItems: [{}, {}, {}, {
            id: "minecraft:carved_pumpkin",
            Count: 1b,
            tag: {CustomModelData: 87, CustomRoleplayData: 1b}
        }],
    }"""

    yield """data merge entity e989ba0e-56e3-46b0-92e3-65302adf4226 {
        Invulnerable: false, 
        NoGravity: true,
        Invisible: true,
        DisabledSlots: 4194303, 
        Rotation: [-90.0f, 0.0f],
        HandItems: [{}, {}],
        Pos: [-543.5d, 113.0d, 1980.5d], 
        ArmorItems: [{}, {}, {}, {
            id: "minecraft:carved_pumpkin",
            Count: 1b,
            tag: {CustomModelData: 88, CustomRoleplayData: 1b}
        }],
    }"""