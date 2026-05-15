from ui import Basisanzeige
from logic import PresentationLogic

logic = PresentationLogic()
ui = Basisanzeige()

def refresh_ui():
    current = logic.get_current_block()
    next_block = logic.get_next_block()

    next_title = "--"
    if next_block:
        next_title = next_block["title"]

    ui.update_ui(
        current=current["title"],
        next_text=next_title,
        hint=current["hint"]
    )

def next_slide():
    logic.next_block()
    refresh_ui()

def prev_slide():
    logic.prev_block()
    refresh_ui()

ui.set_next_callback(next_slide)
ui.set_prev_callback(prev_slide)

refresh_ui()

ui.run()