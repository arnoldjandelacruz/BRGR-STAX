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

def fall_pepper(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def game_loop():
    x = (display_width * .5)
    y = (display_height)

    x1 = random.randrange(0, display_width)
    y1 = random.randrange(-100, 0)
    s1 = 10
    w1 = 5
    h1 = 5
    
    x2 = random.randrange(0, display_width)
    y2 = random.randrange(-100, 0)
    s2 = 10
    w2 = 5
    h2 = 5

    x3 = random.randrange(0, display_width)
    y3 = random.randrange(-100, 0)
    s3 = 10
    w3 = 5
    h3 = 5

    x4 = random.randrange(0, display_width)
    y4 = random.randrange(-100, 0)
    s4 = 10
    w4 = 5
    h4 = 5

    x5 = random.randrange(0, display_width)
    y5 = random.randrange(-100, 0)
    s5 = 10
    w5 = 5
    h5 = 5

    x6 = random.randrange(0, display_width)
    y6 = random.randrange(-400, -300)
    s6 = 10
    w6 = 5
    h6 = 5
    
    x7 = random.randrange(0, display_width)
    y7 = random.randrange(-400, -300)
    s7 = 10
    w7 = 5
    h7 = 5

    x8 = random.randrange(0, display_width)
    y8 = random.randrange(-400, -300)
    s8 = 10
    w8 = 5
    h8 = 5

    x9 = random.randrange(0, display_width)
    y9 = random.randrange(-400, -300)
    s9 = 10
    w9 = 5
    h9 = 5

    x0 = random.randrange(0, display_width)
    y0 = random.randrange(-400, -300)
    s0 = 10
    w0 = 5
    h0 = 5

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
    
        gameDisplay.fill(white)
        fall_pepper(x1, y1, w1, h1, black)
        fall_pepper(x2, y2, w2, h2, black)
        fall_pepper(x3, y3, w3, h3, black)
        fall_pepper(x4, y4, w4, h4, black)
        fall_pepper(x5, y5, w5, h5, black)
        fall_pepper(x6, y6, w6, h6, black)
        fall_pepper(x7, y7, w7, h7, black)
        fall_pepper(x8, y8, w8, h8, black)
        fall_pepper(x9, y9, w9, h9, black)
        fall_pepper(x0, y0, w0, h0, black)
        
        y1 += s1
        y2 += s2
        y3 += s3
        y4 += s4
        y5 += s5
        y6 += s6
        y7 += s7
        y8 += s8
        y9 += s9
        y0 += s0

        if y1 > display_height:
            y1 = 0
            x1 = random.randrange(0, display_width)
        if y2 > display_height:
            y2 = 0
            x2 = random.randrange(0, display_width)
        if y3 > display_height:
            y3 = 0
            x3 = random.randrange(0, display_width)
        if y4 > display_height:
            y4 = 0
            x4 = random.randrange(0, display_width)
        if y5 > display_height:
            y5 = 0
            x5 = random.randrange(0, display_width)
        if y6 > display_height:
            y6 = 0
            x6 = random.randrange(0, display_width)
        if y7 > display_height:
            y7 = 0
            x7 = random.randrange(0, display_width)
        if y8 > display_height:
            y8 = 0
            x8 = random.randrange(0, display_width)
        if y9 > display_height:
            y9 = 0
            x9 = random.randrange(0, display_width)
        if y0 > display_height:
            y0 = 0
            x0 = random.randrange(0, display_width)
                    
        pygame.display.update()
        clock.tick(60)
    
game_loop()
pygame.quit()
quit()
