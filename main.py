from ui import Basisanzeige
from logic import PresentationLogic
from recorder import AudioRecorder
import threading
import time
import os

logic = PresentationLogic()
ui = Basisanzeige(logic)
recorder = AudioRecorder()

# Ordner für Audio-Logs erstellen
if not os.path.exists("audio_logs"):
    os.makedirs("audio_logs")

def analyze_speech(file_path, index_to_update):
    """Hier passiert die Magie (später Whisper)"""
    print(f"Analysiere {file_path}...")
    
    # PLATZHALTER: Wir zählen nur die Größe der Datei als Pseudo-Analyse
    file_size = os.path.getsize(file_path)
    
    if file_size > 500000: # Nur ein Beispielwert
        hint = "Viel geredet! Etwas schneller zum Punkt kommen."
    else:
        hint = "Gutes Tempo, fass dich weiter kurz."
    
    # Logik updaten
    logic.blocks[index_to_update]["hint"] = hint
    
    # UI aktualisieren (Wichtig: UI-Updates immer im Hauptthread!)
    ui.root.after(0, refresh_ui)

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
    # 1. Alte Aufnahme stoppen und speichern
    current_idx = logic.index
    filename = f"audio_logs/folie_{current_idx}.wav"
    saved_file = recorder.stop_and_save(filename)
    
    # 2. Analyse im Hintergrund starten
    if saved_file:
        threading.Thread(target=analyze_speech, args=(saved_file, current_idx)).start()
    
    # 3. Neue Aufnahme für die nächste Folie starten
    recorder.start()

def next_slide():
    handle_transition()
    logic.next_block()
    refresh_ui()

def prev_slide():
    # Beim Zurückgehen stoppen wir meist nur oder starten neu
    recorder.stop_and_save("audio_logs/temp_back.wav")
    logic.prev_block()
    recorder.start()
    refresh_ui()

# Callbacks an UI binden
ui.set_next_callback(next_slide)
ui.set_prev_callback(prev_slide)
ui.refresh_trigger = lambda: [refresh_ui(), recorder.start()] # Startet Aufnahme beim ersten Mal

ui.run()