import pygame
import sys
from MenuButton import MenuButton
from TransitionPage import TransitionPage
from ScoreTracker import ScoreTracker

class EndMenu(TransitionPage, ScoreTracker):
    def __init__(self, screen, score):
        super().__init__(screen)
        self.return_button = MenuButton(210, 400, 320, 80)
        self.menu_title_font = pygame.font.SysFont('freesansbold.ttf', 100)
        self.button_font = self.title_font
        self.font_color = (255, 255, 255)

        score.score
        score.high

    def run_game(self, score):
        while not self.end_game:
            self.start_game(score)

    def start_game(self, score):
        
        track1 = 'Your Score: ', score.score
        track2 = 'HighScore: ', score.high

        self.screen.fill((86, 29, 94))
        self.return_button.draw(self.screen)
        self.draw_text("Thanks for Playing!", self.title_font, self.font_color, 100, 100)
        self.draw_text(str(track1), self.description_font, self.font_color, 200, 235)
        self.draw_text(str(track2), self.description_font, self.font_color, 200, 285)
        self.draw_text("RETURN", self.button_font, self.font_color, 255, 414)
        self.process_user_input_menu()
        pygame.display.flip()

    def button_clicked(self):
        if (pygame.mouse.get_pressed()[0] and self.return_button.isPressed(self.screen)):
            self.end_game = True

    def process_user_input_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.button_clicked()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()