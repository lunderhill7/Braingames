import pygame

class DifficultyManager:
    def __init__(self):
        self.current_difficulty = 0

    def change_difficulty(self, difficulty: int):
        # easy == 1, medium == 2, hard == 3
       self.current_difficulty = difficulty
       return
