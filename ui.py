import tkinter as tk
from tkinter import ttk

class Basisanzeige:
    def __init__(self, logic):
        self.logic = logic
        self.root = tk.Tk()
        self.root.title("Natural Talk - Setup")
        self.root.geometry("600x500")
        
        self.main_container = tk.Frame(self.root)
        self.main_container.pack(fill="both", expand=True)
        
        self.show_homescreen()

    def show_homescreen(self):
        # Lösche alten Inhalt
        for widget in self.main_container.winfo_children():
            widget.destroy()

        tk.Label(self.main_container, text="Präsentation Bearbeiten", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Scrollbereich für die Blöcke
        canvas = tk.Canvas(self.main_container)
        scrollbar = ttk.Scrollbar(self.main_container, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas)

        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        self.entries = []
        for i, block in enumerate(self.logic.blocks):
            frame = tk.LabelFrame(scroll_frame, text=f"Folie {i+1}", padx=10, pady=5)
            frame.pack(fill="x", padx=20, pady=5)

            tk.Label(frame, text="Titel:").grid(row=0, column=0)
            t_entry = tk.Entry(frame, width=40)
            t_entry.insert(0, block.get("title", ""))
            t_entry.grid(row=0, column=1)
            
            # Belege (einfachheitshalber als Komma-getrennte Liste)
            tk.Label(frame, text="Belege:").grid(row=1, column=0)
            b_entry = tk.Entry(frame, width=40)
            b_entry.insert(0, ", ".join(block.get("belege", [])))
            b_entry.grid(row=1, column=1)
            
            self.entries.append((t_entry, b_entry))

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        btn_frame = tk.Frame(self.main_container)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Speichern & Starten", bg="blue", fg="white", 
                  command=self.start_presentation).pack()

    def start_presentation(self):
        # Daten aus UI in Logik speichern
        new_data = []
        for t_e, b_e in self.entries:
            new_data.append({
                "title": t_e.get(),
                "belege": [x.strip() for x in b_e.get().split(",")],
                "hint": "Warte auf Analyse..."
            })
        self.logic.save_data(new_data)
        
        # Wechsel zum Präsentations-Layout
        self.setup_presentation_ui()

    def setup_presentation_ui(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()
        
        self.root.geometry("500x400")
        
        # UI Elemente (wie in deinem Original, nur im main_container)
        tk.Label(self.main_container, text="AKTUELL", font=("Arial", 14, "bold")).pack(pady=5)
        self.current_label = tk.Label(self.main_container, text="", font=("Arial", 20))
        self.current_label.pack(pady=10)

        tk.Label(self.main_container, text="Nächster Punkt", font=("Arial", 12, "bold")).pack()
        self.next_label = tk.Label(self.main_container, text="", font=("Arial", 16))
        self.next_label.pack(pady=5)

        tk.Label(self.main_container, text="Hinweis (Live)", font=("Arial", 12, "bold")).pack()
        self.hint_label = tk.Label(self.main_container, text="-", font=("Arial", 16), fg="red")
        self.hint_label.pack(pady=10)

        self.next_button = tk.Button(self.main_container, text="WEITER", bg="green", fg="white", height=2, width=15)
        self.next_button.pack(pady=20)
        
        self.prev_button = tk.Button(self.main_container, text="zurück", bg="grey", fg="white")
        self.prev_button.pack()

        # Callbacks müssen neu gesetzt werden (passiert in main.py)
        if hasattr(self, 'on_next'): self.set_next_callback(self.on_next)
        if hasattr(self, 'on_prev'): self.set_prev_callback(self.on_prev)
        self.refresh_trigger()

    def update_ui(self, current, next_text, hint):
        self.current_label.config(text=current)
        self.next_label.config(text=next_text)
        self.hint_label.config(text=hint)

    def set_next_callback(self, callback):
        self.on_next = callback
        if hasattr(self, 'next_button'):
            self.next_button.config(command=callback)
            self.root.bind("<space>", lambda e: callback())

    def set_prev_callback(self, callback):
        self.on_prev = callback
        if hasattr(self, 'prev_button'):
            self.prev_button.config(command=callback)

    def run(self):
        self.root.mainloop()

    def refresh_trigger(self):
        # Dummy-Methode, wird von main.py überschrieben
        pass