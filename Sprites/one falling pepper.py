import pygame
import time
import random

pygame.init()

display_width = 400
display_height = 600

white = (255,255,255)
black = (0,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('raining Pepper')
clock = pygame.time.Clock()

icon = pygame.image.load('pepper.png')
pygame.display.set_icon(icon)

pepImg = pygame.image.load('pepper.png')

def pepper(x,y):
    gameDisplay.blit(pepImg,(x,y))

def things1(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def things2(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def things3(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def things4(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def things5(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def game_loop():
    x = (display_width * .5)
    y = (display_height)

    thing_startx1 = random.randrange(0, display_width)
    thing_y1 = random.randrange(-100, 0)
    thing_speed1 = 7
    thing_width1 = 5
    thing_height1 = 5
    
    thing_startx2 = random.randrange(0, display_width)
    thing_y2 = random.randrange(-100, 0)
    thing_speed2 = 7
    thing_width2 = 5
    thing_height2 = 5

    thing_startx3 = random.randrange(0, display_width)
    thing_y3 = random.randrange(-100, 0)
    thing_speed3 = 7
    thing_width3 = 5
    thing_height3 = 5

    thing_startx4 = random.randrange(0, display_width)
    thing_y4 = random.randrange(-100, 0)
    thing_speed4 = 7
    thing_width4 = 5
    thing_height4 = 5

    thing_startx5 = random.randrange(0, display_width)
    thing_y5 = random.randrange(-100, 0)
    thing_speed5 = 7
    thing_width5 = 5
    thing_height5 = 5

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
    
        pepper(x,y)
        gameDisplay.fill(white)
        things1(thing_startx1, thing_y1, thing_width1, thing_height1, black)
        things2(thing_startx2, thing_y2, thing_width2, thing_height2, black)
        things1(thing_startx3, thing_y3, thing_width3, thing_height3, black)
        things2(thing_startx4, thing_y4, thing_width4, thing_height4, black)
        things1(thing_startx5, thing_y5, thing_width5, thing_height5, black)
        
        thing_y1 += thing_speed1
        thing_y2 += thing_speed2
        thing_y3 += thing_speed3
        thing_y4 += thing_speed4
        thing_y5 += thing_speed5

        if thing_y1 > display_height:
            thing_y1 = 0 - 100
            thing_startx1 = random.randrange(0, display_width)
        if thing_y2 > display_height:
            thing_y2 = 0 - 100
            thing_startx2 = random.randrange(0, display_width)
        if thing_y3 > display_height:
            thing_y3 = 0 - 100
            thing_startx3 = random.randrange(0, display_width)
        if thing_y4 > display_height:
            thing_y4 = 0 - 100
            thing_startx4 = random.randrange(0, display_width)
        if thing_y5 > display_height:
            thing_y5 = 0 - 100
            thing_startx5 = random.randrange(0, display_width)
                    
        pygame.display.update()
        clock.tick(60)
    
game_loop()
pygame.quit()
quit()
