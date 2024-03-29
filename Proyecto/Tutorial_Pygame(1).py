
##
#import numpy as np

import pygame, sys          # import statement that imports the pygame and sys modules
from pygame.locals import *

pygame.init()   # Inicializa cada módulo importado con pygame. it needs to be called first in order for many Pygame functions to work
superficie = pygame.display.set_mode((600, 500))   # Tamaño en pixeles de la superficie de la ventana, tupla: (ancho,alto)
pygame.display.set_caption('Juego!')
clock = pygame.time.Clock()     # Asignamos a la variable clock, la función que se encarga de manejar el tiempo del juego

# Logo

logo = pygame.image.load('console.png')
pygame.display.set_icon(logo)


# Imagen

carImg = pygame.image.load('car.png')
def car(x,y):
    superficie.blit(carImg, (x,y))
x =  (50)
y = (100)

x_change = 0
y_change = 0
car_speed = 0


# RGB Values
Aqua = ( 0, 255, 255)
Black = ( 0, 0, 0)
Blue = ( 0, 0, 255)
Fuchsia = (255, 0, 255)
Gray = (128, 128, 128)
Green = (0,128,0)
Lime = ( 0,255, 0)
Maroon = (128, 0, 0)
Navy_Blue = ( 0, 0,128)
Olive = (128, 128, 0)
Purple = (128, 0, 128)
Red = (255, 0, 0)
Silver = (192, 192, 192)
Teal = ( 0, 128, 128)
White = (255, 255, 255)
Yellow = (255, 255, 0)

superficie.fill(Silver)         # Método para llenar de color blanco la superficie del objeto. Método de: pygame.Surface objects

'''
Instrucciones para dibujar diferentes figuras geométricas
'''
# pygame.draw.polygon(surface, color, pointlist, width)
# pygame.draw.line(surface, color, start_point, end_point, width)
# pygame.draw.lines(surface, color, closed, pointlist, width)
# pygame.draw.circle(surface, color, center_point, radius, width)
# pygame.draw.ellipse(surface, color, bounding_rectangle, width)
# pygame.draw.rect(surface, color, rectangle_tuple, width)

pygame.draw.polygon(superficie, Yellow, ((146,0), (291,105),(236,277),(45,105)))
pygame.draw.line(superficie,Teal,(40,40),(120,60),8)
pygame.draw.circle(superficie, Lime, (250,80),50,2)


# Creando la ventana
while True: # Importante: main game loop

    for event in pygame.event.get():    # Módulo event
        if event.type == pygame.KEYDOWN:
            # Mira si ha sido una de las flechas. Si es así
            # ajusta la velocidad.
            if event.key == pygame.K_LEFT:
                x_change =- 3
            elif event.key == pygame.K_RIGHT:
                x_change = 3
            elif event.key == pygame.K_UP:
                y_change =- 3
            elif event.key == pygame.K_DOWN:
                y_change = 3
                  
        # El usuario deja de presionar la tecla
        elif event.type == pygame.KEYUP:
            # Si es una de las flechas, resetea el vector a cero.
            if event.key == pygame.K_LEFT:
                x_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 0
            elif event.key == pygame.K_UP:
                y_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = 0

        
    x += x_change
    y += y_change
    superficie.fill(White)
    car(x,y)

    pygame.display.update() # draws the Surface object returned by pygame.display.set_mode() to the screen
    #pygame.display.flip() hace lo mismo que pygame.display.update() solo que hace el procesamiento de nuevo volviendo a cargar el programa de nuevao
    clock.tick(60)              # 30 Frames per second

    pygame.quit()