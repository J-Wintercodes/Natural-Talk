import json

class PresentationLogic:
    def __init__(self):
        try:
            with open("data.json", "r", encoding="utf-8") as f:
                self.blocks = json.load(f)
        except FileNotFoundError:
            self.blocks = [{"title": "Beispiel", "hint": "Bereit?", "belege": ["", "", ""]}]
        self.index = 0

    def save_data(self, new_blocks):
        self.blocks = new_blocks
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(self.blocks, f, indent=4)

    def get_current_block(self):
        if not self.blocks:
            return {"title": "Keine Daten", "hint": "-", "belege": []}
        return self.blocks[self.index]
    
    def get_next_block(self):
        if self.index + 1 < len(self.blocks):
            return self.blocks[self.index + 1]
        return None
    
    def next_block(self):
        if self.index + 1 < len(self.blocks):
            self.index += 1

    def prev_block(self):
        if self.index > 0:
            self.index -= 1