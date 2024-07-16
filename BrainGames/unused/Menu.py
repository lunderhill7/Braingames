import pygame
import os
# from os import path
# import pygame.gfxdraw
from MenuButton import MenuButton
from DifficultyManager import DifficultyManager
from MemoryGrid import MemoryGrid
from Math import Math

pygame.init()

class Menu: 
    def __init__(self):
        screen_height = 700
        screen_width = 700
        self.screen = pygame.display.set_mode((screen_height, screen_width))
        pygame.display.set_caption("Main Menu")
        fps = 60
        self.menu_font = pygame.font.Font('freesansbold.ttf', 24)
        # self.menu_font = pygame.font.Font(os.path.join("images", 'font2.ttf'), 100)
        # self.background: pygame.Surface
        # self.background = pygame.image.load(path.join("images", "board.jpg")).convert()
        # self.s = pygame.Surface((100, 100)) # the size of your rect
        # self.s.set_alpha(128) # alpha level
        # self.s.fill((255, 255, 255))
        self.menu = True
        self.difficulty = DifficultyManager()
        self.display_menu()

    def display_menu(self):
        
        easy_button = MenuButton(200, 150, 100, 100, "easy")
        medium_button = MenuButton(200, 350, 100, 100, "medium")
        hard_button = MenuButton(200, 550, 100, 100, "hard")

        while self.menu:
            green = (100, 255, 255)
            self.screen.fill(green)
            black = (0, 0, 0)
            self.draw_text("BRAIN GAME", self.menu_font, black, 100, 100)
            easy_button.draw(self.screen)
            medium_button.draw(self.screen)
            hard_button.draw(self.screen)

            if easy_button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]: 
                self.difficulty.change_difficulty(1)
                print(self.menu)
                # Math()
                # ColorMatch()
                # MemoryGrid()
            if medium_button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                self.difficulty.change_difficulty(2)
                print(self.menu)

            if hard_button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                self.difficulty.change_difficulty(3)
                print(self.menu)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu = False
            
            pygame.display.flip()
        pygame.quit()
    
    def draw_text(self, text, font, text_color, x, y):
        rendered_font = font.render(text, True, text_color)
        self.screen.blit(rendered_font, (x, y))
    
menu = Menu()