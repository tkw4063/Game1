import pygame, sys, os, random

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.image.fill((color))
        self.rect = self.image.get_rect()
