
import pygame

import os
from os import path
import pygame.gfxdraw

# Initializing pygame
pygame.init()


class Button(object):
    
    
    def __init__(self,x_cord,y_cord,width,height):
    
        self.x = x_cord
        self.y = y_cord
        self.rect_location = (x_cord,y_cord,width,height)
        self.rect = pygame.Rect(self.rect_location)
        self.color = (0,0,0,0)
        
        
    def change_color(self,color):
        self.color = color
        
    def isPressed(self,screen):
        """ Return true if the mouse is on the button """
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True 
        else:
            return False
        
    def Mouse_isOver(self):
        pos = pygame.mouse.get_pos()
        if pos[0] > self.x and pos[0] < self.x + self.rect_location[2]:
            if pos[1] > self.y and pos[1] < self.y + self.rect_location[3]:
                return True

        return False