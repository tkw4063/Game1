import pygame, sys, os, random
import sprite
import dino

n = 600

# Size of our window
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = n, n
imagesize = (30,30)

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

pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 20)

# Screen color and character
screenColor = (200,200,200)
#srectSize = rectWidth,rectHeight = 10,10
rectPos = rectX, rectY = 100,100
rectSpeed = 1
white = (255,255,255)

def blocks(rectangle,group):
    rectangle.rect.x = random.randrange(n-10)
    rectangle.rect.y = random.randrange(30,n-10)
    group.add(rectangle)


dinog = dino.Dino(imagesize)


def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Changing the color when mouse hovers over it
    if x+w > mouse[0] > x and y+h > mouse[1] >y:
        pygame.draw.rect(surface,ac,(x,y,w,h))
        if click[0] == 1 and action !=None:
            action()
    else:
        pygame.draw.rect(surface,ic,(x,y,w,h))

    textSurf,textRect = text_objects(msg,font)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    surface.blit(textSurf,textRect)

def quitgame():
    pygame.quit()
    sys.exit()

# Game Intro
def introScreen():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        surface.fill((255,255,255))
        TextSurf,TextRect = text_objects("Hungry Dinosaur",font)
        TextRect.center = ((300),(100))
        surface.blit(TextSurf,TextRect)

        TextSurf,TextRect = text_objects("Feed your dinosaur all the food before time runs out.",font)
        TextRect.center = ((300),(200))
        surface.blit(TextSurf,TextRect)

        TextSurf,TextRect = text_objects("Use the arrow keys to move the dinosaur to the food.",font)
        TextRect.center = ((300),(250))
        surface.blit(TextSurf,TextRect)

        button("Play",200,300,200,50,(61,202,94),(40,242,87),game_loop)
        button("Exit",200,400,200,50,(61,202,94),(40,242,87),quitgame)

        pygame.display.flip()



#End screen
def winScreen():
    TextSurf, TextRect = text_objects("Your dinosaur is full and happy!",font)
    TextRect.center = ((300,200))
    surface.blit(TextSurf,TextRect)
    button("Play Again",200,300,200,50,(61,202,94),(40,242,87),game_loop)
    button("Exit",200,400,200,50,(61,202,94),(40,242,87),quitgame)


def loseScreen():
    TextSurf, TextRect = text_objects("You didn't feed the dinosaur in time so it ate you!",font)
    TextRect.center = ((300,200))
    surface.blit(TextSurf,TextRect)
    button("Play Again",200,300,200,50,(61,202,94),(40,242,87),game_loop)
    button("Exit",200,400,200,50,(61,202,94),(40,242,87),quitgame)


# Game loop
def game_loop():
    rectColor = (255,0,0)
    food = pygame.sprite.Group()
    food1 = sprite.Sprite(rectColor)
    food2 = sprite.Sprite(rectColor)
    food3 = sprite.Sprite(rectColor)
    food4 = sprite.Sprite(rectColor)
    food5 = sprite.Sprite(rectColor)
    food6 = sprite.Sprite(rectColor)
    food7 = sprite.Sprite(rectColor)
    food8 = sprite.Sprite(rectColor)
    food9 = sprite.Sprite(rectColor)
    food10 = sprite.Sprite(rectColor)

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
    Timer = font.render(str(counter),True, (0,0,0))
    score = 0

    end = True

    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == timer_event:
                counter -=1
                Timer = font.render(str(counter), True, (0,0,0))
                if counter == 0:
                    pygame.time.set_timer(timer_event,0)


        pressed_keys = pygame.key.get_pressed()

        dinosaur = pygame.sprite.Group()

        dinog.movement(pressed_keys)
        dinosaur.add(dinog)

        surface.fill(screenColor)
        surface.blit(Timer, (570,0))
        food.draw(surface)
        dinosaur.draw(surface)

        if pygame.sprite.groupcollide(dinosaur,food,False,True):
            score+=1

        ScoreBoard = font.render("SCORE: {}".format(score),True, (0,0,0))
        surface.blit(ScoreBoard,[0,0])

        if counter == 0:
            loseScreen()

        if score == 10:
            winScreen()
            timer_event = False
        pygame.display.flip()


    #return end

introScreen()
game_loop()
#end = game_loop()
#endScreen(end)
