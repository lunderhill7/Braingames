from Button import Button
import pygame

class MemoryButton(Button):

    def __init__(self, x_cord, y_cord, width, height, status):

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.gray = (113, 113, 113)
        self.red = (209, 68, 21)
        self.navy = (19, 21, 77)
        self.cream = (230, 216, 156)
        self.light_blue = (135, 181, 224)
        self.dark_gray = (40, 41, 46)

        super().__init__(x_cord, y_cord, width, height)
        self.status = status

        self.change_color(self.cream)

    def draw_tile(self, screen):
        pygame.gfxdraw.box(screen, self.rect, self.color)
        pygame.draw.rect(screen, self.black, self.rect, 5)

    def draw_tile_temp(self, screen):
        if self.status:
            pygame.gfxdraw.box(screen, self.rect, self.cream)
        else:
            pygame.gfxdraw.box(screen, self.rect, self.navy)
        pygame.draw.rect(screen, self.dark_gray, self.rect, 5)

    def change_status(self, status):
        self.status = status