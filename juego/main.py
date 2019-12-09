
##
import os
import random
import numpy as np
import pygame  # import statement that imports the pygame and sys modules
from pygame.locals import *
from tkinter import *
import listeners.buttonselect as btn  # import para crear los botones
import raiz as raiz
import back.funciones as fun
import listeners.chronometer as chro
import listeners.casilla as puzz
import listeners.puzzle as puzzle

# Se asignan valores con respecto al tamaño de la pantalla para ubicar la ventana principal en el centro

x = 180
y = 105
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

pygame.init()   # Inicializa cada módulo importado con pygame. it needs to be called first in order for many Pygame functions to work
DISPLAYSURF = pygame.display.set_mode((900, 560))   # Tamaño en pixeles de la superficie de la ventana, tupla: (ancho,alto)
pygame.display.set_caption('SCIENTIFIC PUZZLE')  # Se asigna el nombre de la ventana

# Se asigna y se pinta la imagen del logo para la ventana
logo = pygame.image.load('./imagenes/logo.png')
pygame.display.set_icon(logo)

# Se asigna y se pinta la imagen de fondo
background = pygame.image.load('./imagenes/back.jpg')
x = 0
y = 0
DISPLAYSURF.blit(background, (x, y))


# RGB Values
Aqua = (0, 255, 255)
Black = (0, 0, 0)
Blue = (0, 0, 255)
Fuchsia = (255, 0, 255)
Gray = (128, 128, 128)
Green = (0, 128, 0)
Lime = (0, 255, 0)
Maroon = (33, 12, 8)
Navy_Blue = (0, 0, 128)
Olive = (128, 128, 0)
Purple = (128, 0, 128)
Red = (255, 0, 0)
Silver = (192, 192, 192)
Teal = (0, 128, 128)
White = (255, 255, 255)
Yellow = (255, 255, 0)
Brown = (13, 8, 2)


# Boton para comenzar un juego nuevo
buttongame = btn.ButtonSelect(White, 650, 100, 200, 50, 'Comenzar')
buttongame.draw(DISPLAYSURF, (0, 0, 0))

# Boton para ver la solución del juego
buttonsolution = btn.ButtonSelect(White, 650, 250, 200, 50, 'Ver solución')
buttonsolution.draw(DISPLAYSURF, (0, 0, 0))

cronometro = chro.Cronos(670, 400, 150, 50)

serie = []


def ver():

    global serie
    n = raiz.tamaniotablero()
    if raiz.serie() == 1:
        serie = fun.fibonacci(n)
    elif raiz.serie() == 2:
        serie = fun.cuadratica(raiz.tamaniotablero())
    elif raiz.serie() == 3:
        serie = fun.primos(raiz.tamaniotablero())
    elif raiz.serie() == 4:
        serie = fun.potenciasDeDos(raiz.tamaniotablero())
    elif raiz.serie() == 5:
        serie = fun.pares(raiz.tamaniotablero())
    elif raiz.serie() == 6:
        serie = fun.impares(raiz.tamaniotablero())

    random.shuffle(serie)
    casillas = fun.arregloAMatriz(serie, n)
    xi = 15
    for i in range(n):
        yi = 50
        for j in range(n):
            if str(casillas[i][j]) == '-1':
                casilla = puzz.Casilla(Brown, yi, xi, n, '')
                casilla.draw(DISPLAYSURF, Brown)
            else:
                casilla = puzz.Casilla((238, 217, 193), yi, xi, n, str(casillas[i][j]))
                casilla.draw(DISPLAYSURF, Brown)
            if n == 5:
                yi = yi + int(560 / n)
            elif n == 4:
                yi = yi + int(560 / n) - 8
            elif n == 3:
                yi = yi + int(560 / n) - 10
        if n == 5:
            xi = xi + int(700 / n) - 35
        elif n == 4:
            xi = xi + int(700 / n) - 45
        elif n == 3:
            xi = xi + int(700 / n) - 55

    return casillas


casillas = ver()

# Creando la ventana
while True:  # Importante: main game loop

    cronometro.draw(DISPLAYSURF, (238, 217, 193), raiz.modojuego(), raiz.tamaniotablero())

    if raiz.v.get == 0 or raiz.w.get() == 0 or raiz.x.get() == 0:
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():    # Módulo event

        pos = pygame.mouse.get_pos()

        if event.type == QUIT:  # Cuando se le da click a la X en la ventana para salir
            pygame.quit()       # Desactiva la librería Pygame
            sys.exit()          # Se encarga de terminar el programa.

        if event.type == pygame.MOUSEBUTTONDOWN:  # Cuando se da click en uno de los botones
            if buttongame.isOver(pos):
                # Se reinician los valores del juego
                casillas = ver()
            if buttonsolution.isOver(pos):
                # Se imprime en consola sólo para verificar que el botón sí está siendo escuchado
                print("Sí reacciona al click, solution")

        puzzle.hacermovimiento(casillas, event, raiz.tamaniotablero(), DISPLAYSURF)
        puzzle.verificarganador(np.array(casillas), np.sort(casillas, axis=None))

    pygame.display.update()  # draws the Surface object returned by pygame.display.set_mode() to the screen
    pygame.display.flip()


