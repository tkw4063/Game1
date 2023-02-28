import pygame, sys, os, random

def blocks(rectangle,group):
    rectangle.rect.x = random.randrange(960)
    rectangle.rect.y = random.randrange(30,560)
    group.add(rectangle)
