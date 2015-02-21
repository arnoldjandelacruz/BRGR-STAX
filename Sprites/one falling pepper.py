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

def things6(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def things7(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def things8(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def things9(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def things10(thingx, thingy, thingw, thingh, color):
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

    thing_startx6 = random.randrange(0, display_width)
    thing_y6 = random.randrange(-400, -300)
    thing_speed6 = 7
    thing_width6 = 5
    thing_height6 = 5
    
    thing_startx7 = random.randrange(0, display_width)
    thing_y7 = random.randrange(-400, -300)
    thing_speed7 = 7
    thing_width7 = 5
    thing_height7 = 5

    thing_startx8 = random.randrange(0, display_width)
    thing_y8 = random.randrange(-400, -300)
    thing_speed8 = 7
    thing_width8 = 5
    thing_height8 = 5

    thing_startx9 = random.randrange(0, display_width)
    thing_y9 = random.randrange(-400, -300)
    thing_speed9 = 7
    thing_width9 = 5
    thing_height9 = 5

    thing_startx10 = random.randrange(0, display_width)
    thing_y10 = random.randrange(-400, -300)
    thing_speed10 = 7
    thing_width10 = 5
    thing_height10 = 5

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
    
        pepper(x,y)
        gameDisplay.fill(white)
        things1(thing_startx1, thing_y1, thing_width1, thing_height1, black)
        things2(thing_startx2, thing_y2, thing_width2, thing_height2, black)
        things3(thing_startx3, thing_y3, thing_width3, thing_height3, black)
        things4(thing_startx4, thing_y4, thing_width4, thing_height4, black)
        things5(thing_startx5, thing_y5, thing_width5, thing_height5, black)
        things6(thing_startx6, thing_y6, thing_width6, thing_height6, black)
        things7(thing_startx7, thing_y7, thing_width7, thing_height7, black)
        things8(thing_startx8, thing_y8, thing_width8, thing_height8, black)
        things9(thing_startx9, thing_y9, thing_width9, thing_height9, black)
        things10(thing_startx10, thing_y10, thing_width10, thing_height10, black)
        
        thing_y1 += thing_speed1
        thing_y2 += thing_speed2
        thing_y3 += thing_speed3
        thing_y4 += thing_speed4
        thing_y5 += thing_speed5
        thing_y6 += thing_speed1
        thing_y7 += thing_speed2
        thing_y8 += thing_speed3
        thing_y9 += thing_speed4
        thing_y10 += thing_speed5

        if thing_y1 > display_height:
            thing_y1 = 0
            thing_startx1 = random.randrange(0, display_width)
        if thing_y2 > display_height:
            thing_y2 = 0
            thing_startx2 = random.randrange(0, display_width)
        if thing_y3 > display_height:
            thing_y3 = 0
            thing_startx3 = random.randrange(0, display_width)
        if thing_y4 > display_height:
            thing_y4 = 0
            thing_startx4 = random.randrange(0, display_width)
        if thing_y5 > display_height:
            thing_y5 = 0
            thing_startx5 = random.randrange(0, display_width)
        if thing_y6 > display_height:
            thing_y6 = 0
            thing_startx6 = random.randrange(0, display_width)
        if thing_y7 > display_height:
            thing_y7 = 0
            thing_startx7 = random.randrange(0, display_width)
        if thing_y8 > display_height:
            thing_y8 = 0
            thing_startx8 = random.randrange(0, display_width)
        if thing_y9 > display_height:
            thing_y9 = 0
            thing_startx9 = random.randrange(0, display_width)
        if thing_y10 > display_height:
            thing_y10 = 0
            thing_startx10 = random.randrange(0, display_width)
                    
        pygame.display.update()
        clock.tick(60)
    
game_loop()
pygame.quit()
quit()
