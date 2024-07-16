import pygame
import sys
from TransitionPage import TransitionPage

class ColorTransition(TransitionPage):
    def __init__(self, screen):
        super().__init__(screen)
        self.font_color = (100, 100, 100)
    
    def run_game(self):
        while not self.end_game:
            self.start_game()

    def start_game(self):
        self.screen.fill((255, 255, 255))
        self.draw_text("3: COLOR MATCH", self.title_font, self.font_color, 120, 100)
        self.draw_text("If the WORD on the TOP matches the COLOR on the BOTTOM", self.description_font, self.font_color, 80, 200)
        self.draw_text("type 't' for true, or else 'f' for false", self.description_font, self.font_color, 150, 250)
        self.draw_text("Press ANY key or click to BEGIN", self.description_font, self.font_color, 200, 400)
        self.process_user_input()
        pygame.display.flip()
