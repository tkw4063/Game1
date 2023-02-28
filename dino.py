import pygame, sys, os, random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


class Dino(pygame.sprite.Sprite):
    def __init__(self,defaultimagesize):
        super(Dino,self).__init__()
        self.image = pygame.image.load("C:/Users/tkw40/Documents/Clemson/Student/CPCS_6160/Game1/dinosaur.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,defaultimagesize)
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()

    def movement(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1,0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1000:
            self.rect.right = 1000
        if self.rect.top <= 30:
            self.rect.top = 30
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
