import pygame
from Button import Button

class MenuButton(Button):

    def __init__(self, x_cord, y_cord, width, height):
        super().__init__(x_cord, y_cord, width, height)
        # self.change_color(self.white)
    
    def draw(self, screen):
        pygame.gfxdraw.box(screen, self.rect, (0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 3)


    