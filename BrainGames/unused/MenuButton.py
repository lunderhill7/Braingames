from Button import Button
import pygame
import os
from os import path
import pygame.gfxdraw

pygame.init()

class MenuButton(Button):
    def __init__(self, x_cord, y_cord, width, height, difficulty_name):
        super().__init__(x_cord, y_cord, width, height)
        if pygame.font:
            self.font = pygame.font.Font(os.path.join("images", 'font2.ttf'), 90)        
        self.text = self.font.render(str(difficulty_name), True, (255,255,255))

    def draw(self,screen):
        pygame.draw.rect(screen, (255,255,255), self.rect_location, width = 3)
        pygame.gfxdraw.box(screen, self.rect, self.color)
        X = self.rect.centerx - (self.text.get_width() / 2)
        Y = self.rect.centery - (self.text.get_height() / 2)
        screen.blit(self.text, (X, Y))