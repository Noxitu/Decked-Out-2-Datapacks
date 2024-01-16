from mcfunction import mcfunction
import data


def _create(desc):
    function_name = f"""do2:play_sound/{desc["id"]}"""
    name = desc["sound"]
    condition = ""
    at = desc["at"]
    distance = desc.get("range", 16)

    @mcfunction(function_name=function_name)
    def _():
        command = [
            "execute",
            condition,
            f"positioned {at}",
            f"as @a[tag=do2.cmd_sound,distance=..{distance}]",
            "at @s",
            f"run playsound do2:{name} master @s",
            # at,
        ]

        if at is not None:
            command.append(at)

        command = " ".join(part for part in command if part)
        yield command


systems = data.SOUNDS

for desc in systems:
    if "delay" in desc:
        _create(desc)