from pathlib import Path
import shutil

from noxpack import json
from noxitu_pack_builder.output_file import output_file

from .sound_db import *


OGG_DATA = (
    Path.home()
    / "AppData/Roaming/.minecraft/profiles/h9/saves/hc9/audio_player_data_ogg"
)

ASSETS_ROOT = Path(__file__).parent / "assets"


def _copy_sound(generator, target_path):
    if not target_path.exists():
        shutil.copyfile(generator(), target_path)


def _create_sound(sound_id, sound_hash):
    source_path = OGG_DATA / f"{sound_hash}.ogg"
    target_path = f"do2/sounds/{sound_id.replace('.', '/')}.ogg"

    @output_file(save=_copy_sound, path=target_path)
    def _():
        return source_path


@json
def _():
    sounds_json = {}

    for sound_id, sound_hash in IDS.items():
        if sound_id == "" or sound_id.endswith("#"):
            continue

        _create_sound(sound_id, sound_hash)

        sound = {
            "replace": False,
            "sounds": [{"name": f"do2:{sound_id.replace('.', '/')}"}],
        }

        if sound_id in SUBTITLES:
            sound["subtitle"] = SUBTITLES[sound_id]

        sounds_json[sound_id] = sound

    for group_id, sounds in GROUPS.items():
        sound = {"replace": False, "sounds": []}

        if group_id in SUBTITLES:
            sound["subtitle"] = SUBTITLES[group_id]

        if sounds is ...:
            sounds = []
            for sound_id in sounds_json:
                if sound_id.startswith(f"{group_id}."):
                    sounds.append(sound_id)
                    sounds_json[sound_id]["erased"] = True

        for sound_id in sounds:
            sound["sounds"].extend(sounds_json[sound_id]["sounds"])

        sounds_json[group_id] = sound

    for sound_id in list(sounds_json):
        if sounds_json[sound_id].get("erased", False):
            del sounds_json[sound_id]

    return sounds_json
