import pygame
import sys, math
from pygame.locals import *

WIDTH = 640
HEIGHT = 480

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    for x in drange(0.0, 90.0, 0.5):        
        rect = pygame.Rect(100 + math.sin(x)*10,x*10,2,2)
        pygame.draw.rect(screen, (55,180,255), rect)
    
    for x in drange(0.0, 90.0, 0.01):        
        rect = pygame.Rect(300 + 4*math.sin((0.5*x)*(0.5*x))*10,x*10,2,2)
        pygame.draw.rect(screen, (55,180,255), rect)
    
    for x in drange(0.0, 90.0, 0.5):
        rect = pygame.Rect(x*10, 100 + math.cos(x)*10, 2, 2)
        pygame.draw.rect(screen, (255,255,255), rect)
        
    for x in drange(0.0, 90.0, 0.01):
        rect = pygame.Rect(x*10, 100 + math.tan(x)*10, 2, 2)
        pygame.draw.rect(screen, (255,180,55), rect)
    
    pygame.display.update()