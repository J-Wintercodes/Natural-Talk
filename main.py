from ui import Basisanzeige
from logic import PresentationLogic
import threading
import time

logic = PresentationLogic()
ui = Basisanzeige(logic)

def analyze_speech(audio_file_dummy):
    """
    Hier kommt später Whisper rein.
    """
    print(f"Analysiere Folie {logic.index}...")
    time.sleep(1) # Simuliert Whisper-Dauer
    
    # Beispiel-Logik:
    # text = whisper_model.transcribe(audio_file_dummy)
    # count = len(text.split())
    
    # Platzhalter Logik:
    hint = "Super Tempo!" if logic.index % 2 == 0 else "Langsamer sprechen!"
    
    # Update UI (muss über main thread laufen)
    logic.blocks[logic.index]["hint"] = hint
    refresh_ui()

def refresh_ui():
    current = logic.get_current_block()
    next_block = logic.get_next_block()
    next_title = next_block["title"] if next_block else "--"

    ui.update_ui(
        current=current["title"],
        next_text=next_title,
        hint=current["hint"]
    )

def handle_transition():
    # 1. Stop Recording (dummy)
    # 2. Starte Analyse im Hintergrund
    thread = threading.Thread(target=analyze_speech, args=("slide.mp3",))
    thread.start()
    
    # 3. Start New Recording (dummy)
    refresh_ui()

def next_slide():
    handle_transition() # Vorherige Folie analysieren
    logic.next_block()
    refresh_ui()

def prev_slide():
    logic.prev_block()
    refresh_ui()

ui.set_next_callback(next_slide)
ui.set_prev_callback(prev_slide)
ui.refresh_trigger = refresh_ui

ui.run()