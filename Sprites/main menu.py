import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

white = (255,255,255)
black = (0,0,0)

green = (0,200,0)
red = (200, 0, 0)
light_red = (255, 0, 0)
light_green = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Start_Up')
clock = pygame.time.Clock()
bg = pygame.image.load('start-up menu.jpg')

def backg():
    pygame.display.update()
    gameDisplay.blit(bg, (0,0))
    pygame.display.update()
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

backg()    
game_loop()
pygame.quit()
quit()
