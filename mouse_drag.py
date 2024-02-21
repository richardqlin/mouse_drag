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


circle_x, circle_y=400,300
while True:
    pygame.time.delay(3)
    pygame.draw.circle(screen, red , (circle_x,circle_y),20)
    pygame.display.update()
    screen.fill(black)
    



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:       
                x,y= event.pos
                if x in range(circle_x-20,circle_x+20) and y in range(circle_y-20,circle_y+20):
                    rectangle_draging = True
                    offset_x = circle_x- x
                    offset_y = circle_y - y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:       
                rectangle_draging = False
        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                x, y = event.pos
                circle_x = x + offset_x
                circle_y = y + offset_y
        

                
