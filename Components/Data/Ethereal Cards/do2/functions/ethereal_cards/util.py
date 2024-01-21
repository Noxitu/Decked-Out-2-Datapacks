import data


COLOR = "#FED83D"
ETHEREAL = "\u2732"
PERMANENT = "\u2261"


def cards():
    return data.CUSTOM_MODIFICATIONS.ETHEREAL_CARDS


def card_display_name(name):
    nbt = data.NBT.CARDS[name]
    original_display_name = nbt["tag"]["display"]["Name"]
    assert name in original_display_name
    display_name = f" {name} "

    if PERMANENT in original_display_name:
        display_name = f"{PERMANENT}{display_name}{PERMANENT}"

    display_name = f"{ETHEREAL}{display_name}{ETHEREAL}"
    display_name = f"""{{"text": "{display_name}", "color": "{COLOR}"}}"""
    return display_name


def card_model(name):
    return data.CUSTOM_MODIFICATIONS.ETHEREAL_CARDS[name]["model"]


def card_nbt(name, *, count=1, slot=None):
    display_name = card_display_name(name).replace("'", "\\'")
    model = card_model(name)

    slot = "" if slot is None else f"Slot: {slot}b,"

    return f"""{{
        id: "minecraft:gold_nugget",
        Count: {count},
        {slot}
        tag: {{
            CustomModelData: {model},
            display: {{
                Name: '{display_name}'
            }}
        }}
    }}"""
