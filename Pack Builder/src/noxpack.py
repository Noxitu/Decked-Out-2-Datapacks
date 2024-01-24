from noxitu_pack_builder.output_file import output_file as _output_file
from noxitu_pack_builder.formats.copy import copy as _copy
from noxitu_pack_builder.formats.json import json as _json
from noxitu_pack_builder.formats.png import png as _png
from noxitu_pack_builder.formats.mcfunction import mcfunction as _mcfunction


copy = _output_file(save=_copy)
json = _output_file(save=_json, suffix=".json")
png = _output_file(save=_png, suffix=".png")
mcfunction = _output_file(save=_mcfunction, suffix=".mcfunction")
