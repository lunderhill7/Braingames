import pygame
import sys

class TransitionPage:
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.SysFont('freesansbold.ttf', 80)
        self.description_font = pygame.font.SysFont('freesansbold.ttf', 30)
        self.end_game = False
    
    def process_user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                self.end_game = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def draw_text(self, text, font, text_color, x, y):
        rendered_font = font.render(text, True, text_color)
        self.screen.blit(rendered_font, (x, y))