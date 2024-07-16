from Button import Button
import pygame
import os
from os import path
import pygame.gfxdraw

# Initializing pygame
pygame.init()

class Math_Button(Button):
    
    def __init__(self,x_cord,y_cord,width,height,value):
        super().__init__(x_cord,y_cord,width,height)
        self.value = value
        if pygame.font:
            self.font = pygame.font.Font(os.path.join("images", 'font2.ttf'), 90)        
        self.text = self.font.render(str(value),True,(255,255,255))
        
    def draw(self,screen):
        
        pygame.draw.rect(screen,(255,255,255),self.rect_location, width=3)
        #pygame.draw.rect(screen, self.color,self.rect_location)
        pygame.gfxdraw.box(screen, self.rect, self.color)
        X = self.rect.centerx - (self.text.get_width() / 2)
        Y = self.rect.centery - (self.text.get_height() / 2)
        screen.blit(self.text,(X,Y))
    
    def get_val(self):
        return self.value
    