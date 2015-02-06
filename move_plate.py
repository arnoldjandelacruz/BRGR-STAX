import pygame
 
pygame.init()
 
display_width = 800
display_height = 600
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('BRGR-STAX')
 
black = (0,0,0)
white = (255,255,255)
 
clock = pygame.time.Clock()
crashed = False
plateImg = pygame.image.load('plate.png')
 
 


 
def plate(x,y):
    gameDisplay.blit(plateImg, (x,y))



def game_loop():

    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    plate_speed = 0

    crashed = False

    key_right = False
    key_left = False
    
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                     key_left = True
                elif event.key == pygame.K_RIGHT:
                     key_right = True
     
            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        key_left = False
                    if event.key == pygame.K_RIGHT:
                         key_right = False
     
            if key_left == True and x > 0:
               x_change = -10
            if key_right == True and x < 599:
               x_change = 10
               
        if (key_left == True and  x > 0) or (key_right == True and x < 599) :
            x += x_change
            
        gameDisplay.fill(black)
        plate(x,y)

      
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
