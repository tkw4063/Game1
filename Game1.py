import pygame, sys, os, random
import sprite
import dino
from blocksgroup import blocks
from Buttons import button
from textobj import text_objects

# Size of our window
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
imagesize = (40,40)

# Import locals for key binding
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initializes display module
pygame.init()
pygame.display.set_caption("Hungry Dinosaur")
surface = pygame.display.set_mode(SCREEN_SIZE)

bg = pygame.image.load("C:/Users/tkw40/Documents/Clemson/Student/CPCS_6160/Game1/sand1.jpg")

pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 20)

# Screen color and character
#srectSize = rectWidth,rectHeight = 10,10
screenColor = (255,255,255)
rectPos = rectX, rectY = 100,100
rectSpeed = 1
white = (255,255,255)

def quitgame():
    pygame.quit()
    sys.exit()


# Game Intro
def introScreen():
  pygame.font.init()
  font = pygame.font.SysFont("Comic Sans MS", 20)
  intro = True
  while intro:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()

      surface.fill((255,255,255))
      TextSurf,TextRect = text_objects("Hungry Dinosaur",font)
      TextRect.center = ((500),(100))
      surface.blit(TextSurf,TextRect)

      TextSurf,TextRect = text_objects("Feed your dinosaur all the food before time runs out.",font)
      TextRect.center = ((500),(200))
      surface.blit(TextSurf,TextRect)

      TextSurf,TextRect = text_objects("Use the arrow keys to move the dinosaur to the food.",font)
      TextRect.center = ((500),(250))
      surface.blit(TextSurf,TextRect)

      button(surface,"Play",400,300,200,50,(61,202,94),(40,242,87),game_loop)
      button(surface,"Exit",400,400,200,50,(61,202,94),(40,242,87),quitgame)

      pygame.display.flip()

def winScreen():
    button(surface,"Your dinosaur is full and happy!",360,200,300,50,(40,242,87),(40,242,87))
    button(surface,"Play Again",400,300,200,50,(61,202,94),(40,242,87),game_loop)
    button(surface,"Exit",400,400,200,50,(61,202,94),(40,242,87),quitgame)

def loseScreen():
    button(surface,"You didn't feed the dinosaur in time so it ate you!",360,200,300,50,(40,242,87),(40,242,87))
    button(surface,"Play Again",400,300,200,50,(61,202,94),(40,242,87),game_loop)
    button(surface,"Exit",400,400,200,50,(61,202,94),(40,242,87),quitgame)

# Game loop
def game_loop():
    pygame.font.init()
    font = pygame.font.SysFont("Comic Sans MS", 20)
    rectColor = (255,0,0)
    dinog = dino.Dino(imagesize)

    food = pygame.sprite.Group()
    food1 = sprite.People(imagesize)
    food2 = sprite.People(imagesize)
    food3 = sprite.People(imagesize)
    food4 = sprite.People(imagesize)
    food5 = sprite.People(imagesize)
    food6 = sprite.People(imagesize)
    food7 = sprite.People(imagesize)
    food8 = sprite.People(imagesize)
    food9 = sprite.People(imagesize)
    food10 = sprite.People(imagesize)

    blocks(food1,food)
    blocks(food2,food)
    blocks(food3,food)
    blocks(food4,food)
    blocks(food5,food)
    blocks(food6,food)
    blocks(food7,food)
    blocks(food8,food)
    blocks(food9,food)
    blocks(food10,food)
    counter = 30
    timer_int = 500
    timer_event = pygame.USEREVENT +1
    pygame.time.set_timer(timer_event,timer_int)
    Timer = font.render(str(counter),True, (4,255,63))
    score = 0

    end = True

    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == timer_event:
                counter -=1
                Timer = font.render(str(counter), True, (4,255,63))
                if counter == 0:
                    pygame.time.set_timer(timer_event,0)


        pressed_keys = pygame.key.get_pressed()

        dinosaur = pygame.sprite.Group()

        dinog.movement(pressed_keys)
        dinosaur.add(dinog)

        surface.blit(bg,(0,0))
        surface.blit(Timer, (970,0))
        food.draw(surface)
        dinosaur.draw(surface)

        if pygame.sprite.groupcollide(dinosaur,food,False,True):
            score+=1

        ScoreBoard = font.render("SCORE: {}".format(score),True, (4,255,63))
        surface.blit(ScoreBoard,[0,0])

        if counter == 0:
            loseScreen()

        if score == 10:
            winScreen()
            timer_event = False
        pygame.display.flip()


introScreen()
game_loop()
