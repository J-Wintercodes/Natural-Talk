import json

class PresentationLogic:
    def __init__(self):
        with open("data.json", "r", encoding ="utf-8") as f:
            self.blocks = json.load(f)

        self.index = 0

    def get_current_block(self):
        #absturz sicherung bei keinen daten
        if not self.blocks:
            return{"title": "Keine Daten", "hint": "-"}
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
            self.index -=1