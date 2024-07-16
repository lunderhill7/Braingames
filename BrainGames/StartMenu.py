import pygame
import sys
from MenuButton import MenuButton
from TransitionPage import TransitionPage

class StartMenu(TransitionPage):
    def __init__(self, screen):
        super().__init__(screen)
        self.play_button = MenuButton(240, 400, 230, 80)
        self.menu_title_font = pygame.font.SysFont('freesansbold.ttf', 100)
        self.button_font = self.title_font
        self.font_color = (255, 255, 255)

    def run_game(self):
        while not self.end_game:
            self.start_game()

    def start_game(self):
        self.screen.fill((52, 78, 100))
        self.play_button.draw(self.screen)
        self.draw_text("BRAIN GAME", self.title_font, self.font_color, 180, 100)
        self.draw_text("This game has multiple levels that will each test", self.description_font, self.font_color, 125, 200)
        self.draw_text("your quick thinking and memory... have fun!", self.description_font, self.font_color, 140, 250)
        self.draw_text("PLAY", self.button_font, self.font_color, 285, 414)
        self.process_user_input_menu()
        pygame.display.flip()

    def button_clicked(self):
        if (pygame.mouse.get_pressed()[0] and self.play_button.isPressed(self.screen)):
            self.end_game = True

    def process_user_input_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.button_clicked()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()