import tkinter as tk

class Basisanzeige:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Natural Talk Basisfunktionen")
        self.root.geometry("500x350") # Etwas höher für besseren Platz
        self.root.attributes("-topmost", True)

        # Aktuell
        tk.Label(self.root, text="AKTUELL", font=("Arial", 14, "bold")).pack(pady=5)
        self.current_label = tk.Label(
            self.root,
            text="noch nichts",
            font=("Arial", 20)
        )
        self.current_label.pack(pady=10) # Korrigiert: current_label statt next_label

        # Nächstes
        tk.Label(self.root, text="Nächster Punkt", font=("Arial", 12, "bold")).pack()
        self.next_label = tk.Label(
            self.root,
            text="noch nichts",
            font=("Arial", 16)
        )
        self.next_label.pack(pady=5)

        # Hinweis
        tk.Label(self.root, text="Hinweis", font=("Arial", 12, "bold")).pack()
        self.hint_label = tk.Label(
            self.root,
            text="langsamer",
            font=("Arial", 16),
            fg="red"
        )
        self.hint_label.pack(pady=10)

        #Weiter Button
        self.next_button = tk.Button(
            self.root,
            text="WEITER",
            font=("Arial", 12, "bold"),
            bg="green",
            fg="white",
            height=2,
            width=15
        )
        self.next_button.pack(pady=20)

        #zurück button
        self.prev_button = tk.Button(
            self.root,
            text="zurück",
            font=("Arial", 10),
            bg="grey",
            fg="white",
            height=1,
            width=10
        )
        self.prev_button.pack(pady=5)

    def set_prev_callback(self, callback):
        self.prev_button.config(command=callback)
                              

    def update_ui(self, current, next_text, hint):
        self.current_label.config(text=current)
        self.next_label.config(text=next_text)
        self.hint_label.config(text=hint)

    def set_next_callback(self, callback):
        self.next_button.config(command=callback)
        # Beispiel: Leertaste oder Klick löst nächsten Block aus
        self.root.bind("<space>", lambda e: callback())
        
    def run(self):
        self.root.mainloop()