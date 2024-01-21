from noxpack import mcfunction

STORAGE = "do2:gui_customization"
# TAG_ENABLED = "sdo2.tags.enable_gui"
TAG_CALIBRATING = "do2.tags.calibrating"
TAG_MARKER = "do2.tags.calibrating_marker"

NOW_CALIBRATING = f"storage {STORAGE} NowCalibrating"

@mcfunction(tags=["minecraft:load"])
def init():
    yield f"execute as Noxitu run function {start}"

@mcfunction
def start():
    yield f"tag @e[tag={TAG_CALIBRATING}] remove {TAG_CALIBRATING}"
    yield f"tag @s add {TAG_CALIBRATING}"

    yield f"data modify {NOW_CALIBRATING} set value {{}}"
    yield f"data modify {NOW_CALIBRATING}.Pos set from entity @s Pos"
    # yield f"data modify {NOW_CALIBRATING}.Rotation set from entity @s Rotation"
    yield f"kill @e[tag={TAG_MARKER}]"

    yield f"""
        execute at @s
                run summon minecraft:marker ^ ^ ^32 {{Tags: ["{TAG_MARKER}"]}}
        """

    yield f"""
        execute at @s
                run summon minecraft:armor_stand ^ ^ ^32 {{Marker: true}}
        """

    yield f"""
                summon minecraft:armor_stand ^ ^ ^32 {{Marker: true}}
        """

    yield f"function {calibrating}"


@mcfunction
def calibrating():
    yield f"""
        execute as @a[tag={TAG_CALIBRATING}]
                run function {calibrating_player}
        """

    yield f"""
        execute unless entity @a[tag={TAG_CALIBRATING},limit=1]
                run return 0
        """
    
    yield f"schedule function {calibrating} 1t replace"


@mcfunction
def calibrating_player():
    yield f"""title @s subtitle "Calibrating" """

    yield f"""
        execute store success {NOW_CALIBRATING}.PosChanged int 1 
                run data modify {NOW_CALIBRATING}.Pos set from entity @s Pos
        """
    
    yield f"""
        execute at @s
                facing entity @e[tag={TAG_MARKER}] eyes
                run tp @s ~ ~ ~ ~ ~
        """

    yield f"""
        execute if data {NOW_CALIBRATING}{{PosChanged: 1}}
                run function {end_calibrating_player}
        """
    
    yield f"""title @s title "GUI Calibration" """


@mcfunction
def end_calibrating_player():
    yield f"""title @s subtitle {{"color": "#00ff00", "text": "Finished"}} """
    yield f"tag @s remove {TAG_CALIBRATING}"
    yield f"data remove {NOW_CALIBRATING}"
    yield f"kill @e[tag={TAG_MARKER}]"
