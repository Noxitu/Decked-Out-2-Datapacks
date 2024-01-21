from noxpack import mcfunction
import data


def _create(desc):
    path = f"""do2/functions/audio/play/{desc["id"]}"""
    name = desc["sound"]
    condition = ""
    at = desc.get("at", desc["command_block"])
    distance = desc.get("range", 16)

    @mcfunction(path=path)
    def _():
        command = [
            "execute",
            condition,
            f"positioned {at}",
            f"as @a[tag=do2.cmd_sound,distance=..{distance}]",
            "at @s",
            f"run playsound do2:{name} master @s",
        ]

        # if at is not None:
        #     command.append(at)

        command = " ".join(part for part in command if part)
        yield command


for systems in data.SOUNDSYSTEMS.Items:
    for desc in systems:
        if "delay" in desc:
            _create(desc)


_create({
    "id": "cards_reckless_charge",
    "command_block": "-546 -55 1925",
    "sound": "cards.reckless_charge",
    "range": 177,
})