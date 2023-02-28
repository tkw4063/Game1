import pygame, sys, os, random

def blocks(rectangle,group):
    rectangle.rect.x = random.randrange(590)
    rectangle.rect.y = random.randrange(30,590)
    group.add(rectangle)
