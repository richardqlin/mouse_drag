import pygame
import time
import random
from pygame.locals import *
pygame.init()
width =800
height=600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('drag a circle with mouse button click')
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)


rectangle_draging = False


x= y=x2=y2=0
while True:
    pygame.time.delay(3)
    pygame.draw.rect(screen, red , (x,y,x2-x,y2-y),2)
    pygame.display.update()
    screen.fill(black)
    



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:       
                x,y= event.pos
                
                rectangle_draging = True
                   

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                x2,y2=event.pos
                rectangle_draging = False
        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                x2, y2 = event.pos
              
        

                
