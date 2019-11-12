import pygame as pyg, sys
from pygame.locals import *

pyg.init()
DISPLAYSURF = pyg.display.set_mode((400,300))
pyg.display.set_caption('Pygame!')

while True:
    for event in pyg.event.get():
        if event.type == QUIT:
            pyg.quit()
            sys.exit()
    pyg.display.update()


teal = (0,128,128)
white = (255,255,255)
yellow = (255,255,0)

DISPLAYSURF.fill(teal)
