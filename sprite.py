import pygame, sys, os, random

class People(pygame.sprite.Sprite):
    def __init__(self,defaultimagesize):
        super(People,self).__init__()
        self.image = pygame.image.load("C:/Users/tkw40/Documents/Clemson/Student/CPCS_6160/Game1/person.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,defaultimagesize)
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
