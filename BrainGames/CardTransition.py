import pygame
import sys
from TransitionPage import TransitionPage

class CardTransition(TransitionPage):
    def __init__(self, screen):
        super().__init__(screen)
        self.font_color = (100, 100, 100)
    
    def run_game(self):
        while not self.end_game:
            self.start_game()

    def start_game(self):
        self.screen.fill((255, 255, 255))
        self.draw_text("4: CARD MATCHING", self.title_font, self.font_color, 90, 100)
        self.draw_text("Classic card matching game. Find the pairs to win!", self.description_font, self.font_color, 110, 200)
        self.draw_text("Press ANY key or click to BEGIN", self.description_font, self.font_color, 200, 400)
        self.process_user_input()
        pygame.display.flip()
