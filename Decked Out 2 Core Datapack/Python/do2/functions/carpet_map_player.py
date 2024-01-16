from mcfunction import mcfunction


@mcfunction(tags=["minecraft:load"])
def check_status():
    yield f"""
        execute unless entity @e[name=TangoCam] 
                if entity @p[name=!TangoCam] 
                run function {summon_tangocam}
        """
    
    yield """
        execute if entity @e[name=TangoCam] 
                unless entity @a[name=!TangoCam] 
                run kill TangoCam
        """
    
    yield f"schedule function {check_status} 30s replace"


@mcfunction
def summon_tangocam():
    yield "player TangoCam spawn at -484.52 59.00 1738.19 facing 0 0"
    yield "execute as @p[name=TangoCam] run gamemode spectator"

