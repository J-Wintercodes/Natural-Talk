import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import threading

class AudioRecorder:
    def __init__(self):
        self.fs = 44100  # Samplerate
        self.recording = []
        self.is_recording = False
        self.thread = None

    def _record_loop(self):
        # Startet den Stream
        with sd.InputStream(samplerate=self.fs, channels=1, callback=self._callback):
            while self.is_recording:
                sd.sleep(100)

    def _callback(self, indata, frames, time, status):
        if status:
            print(status)
        self.recording.append(indata.copy())

    def start(self):
        self.recording = []
        self.is_recording = True
        self.thread = threading.Thread(target=self._record_loop)
        self.thread.start()
        print("Aufnahme gestartet...")

    def stop_and_save(self, filename):
        self.is_recording = False
        if self.thread:
            self.thread.join()
        
        if self.recording:
            # Kombiniert alle Schnipsel zu einer Datei
            audio_data = np.concatenate(self.recording, axis=0)
            write(filename, self.fs, audio_data)
            print(f"Datei gespeichert: {filename}")
            return filename
        return None