import pygame
import time
import random
from random import randrange

pygame.init()

display_largura = 550
display_altura = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,200,0)
red2 = (255,0,0)
green2 = (0,150,0)


score = 0

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
font_text = pygame.font.SysFont('Comic Sans MS', 30)

textsurface = font_text.render('Score: {}'.format(score), False, (1, 0, 0))


gameDisplay = pygame.display.set_mode((display_largura,display_altura))
pygame.display.set_caption('Piano tiles')
clock = pygame.time.Clock()



def new_tecla(teclax, teclay, teclaw, teclah, color):
    return pygame.draw.rect(gameDisplay, color, [teclax, teclay, teclaw, teclah])
    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_loop():
   
    tecla_startx = randrange(0,1)
    tecla_starty = -175
    tecla_speed = 4
    tecla_width = display_largura/4
    tecla_height = 175   
    score = 0
    
    gameExit = False
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
                gameExit = True

            if tecla_starty > display_altura:
                tecla_starty = 0 - tecla_height
                tecla_startx = random.randrange(0, display_largura)
                   
        gameDisplay.fill(white) 
        tecla = new_tecla(tecla_startx, tecla_starty, tecla_width, tecla_height, black)
        
        pos = pygame.mouse.get_pos()
        #--------pressed2 = pygame.mouse.get
        # Check if the rect collided with the mouse pos
        # and if the left mouse button was pressed.
        if tecla.collidepoint(pos) and event.type == pygame.MOUSEBUTTONUP:
            score += 1
            print(score)
            
        tecla_starty += tecla_speed  
        
        textsurface = font_text.render('Score: {}'.format(score), False, (255, 0, 0))
        gameDisplay.blit(textsurface,(10,10))
        
        
        pygame.display.update()   
        clock.tick(60)

def act_bt_start():
    print('Hellow...')
    
    
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == 'Iniciar':
                print('Iniciar...')
                game_loop()
            elif action == 'Sair':
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
        
    smallText = pygame.font.Font('freesansbold.ttf',20)
    textSurf, textRect = text_objects('Iniciar',smallText)
    textRect.center = ((x+(100/2)), (450 +(50/2)))
    gameDisplay.blit(textSurf , textRect)

def game_intro():
    
    intro = True
    clock.tick(15)  

  
    while intro:
        
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RETURN :
                    intro = False
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('Piano',largeText)
        TextRect.center = ((display_largura/2), (display_altura/2))
        gameDisplay.blit(TextSurf,TextRect)
        
        button('Iniciar',150,450,100,50,green,green2,action="Iniciar")
        button('Sair',550,450,100,50,red,red2,action='Sair')

        pygame.draw.rect(gameDisplay, red,(550,450,100,50))
       
        
    
        pygame.display.update()
        
game_intro()        
game_loop()
pygame.quit()
quit()