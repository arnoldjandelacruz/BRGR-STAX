import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

white = (255,255,255)

green = (0,200,0)
red = (200, 0, 0)
light_red = (255, 0, 0)
light_green = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Start_Up')
clock = pygame.time.Clock()


def game_intro():
    #intro = False

    #while not intro:
        #for event in pygame.event.get():
            #print(event)
            #if event.type == pygame.QUIT:
            #     pygame.quit()
            #     quit()
                 
    gameDisplay.fill(white)
    
    mouse = pygame.mouse.get_pos()
    if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
        pygame.draw.rect(gameDisplay, light_green, (150,450,100,50))
    else:
        pygame.draw.rect(gameDisplay, green, (150,450,100,50))
            

    pygame.draw.rect(gameDisplay, red, (550,450,100,50))
            
    
    pygame.display.update()

    clock.tick(15)

def game_loop():
    x = (display_width * .5)
    y = (display_height)

   
    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                    
        pygame.display.update()
        clock.tick(60)

game_intro()    
game_loop()
pygame.quit()
quit()

