def text_button(text, color, scoreboard, trigger, hint):
    return f"""{{
        "color": "{color}",
        "text": "[{text}]",
        "clickEvent": {{"action": "run_command", "value": "/trigger {scoreboard} set {trigger}"}},
        "hoverEvent": {{"action": "show_text", "contents": "{hint}"}}
    }}"""
