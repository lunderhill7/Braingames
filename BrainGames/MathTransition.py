import pygame
import sys
from TransitionPage import TransitionPage

class MathTransition(TransitionPage):
    def __init__(self, screen):
        super().__init__(screen)
        self.font_color = (255, 255, 255)

    def run_game(self):
        while not self.end_game:
            self.start_game()

    def start_game(self):
        self.screen.fill((10, 60, 10))
        self.draw_text("1: MATH", self.title_font, self.font_color, 240, 100)
        self.draw_text("This minigame will challenge your ability to solve math equations", self.description_font, self.font_color, 50, 200)
        self.draw_text("Good luck... you'll need it", self.description_font, self.font_color, 230, 250)
        self.draw_text("Press ANY key or click to BEGIN", self.description_font, self.font_color, 200, 400)
        self.process_user_input()
        pygame.display.flip()