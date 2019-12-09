
##
import os

import pygame  # import statement that imports the pygame and sys modules
from pygame.locals import *
from tkinter import *
import listeners.buttonselect as btn  # import para crear los botones
import raiz as raiz
import back.funciones as fun
import listeners.chronometer as chro
import listeners.casilla as puzz

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

# DISPLAYSURF.fill(Maroon)         # Método para llenar de color blanco la superficie del objeto. Método de: pygame.Surface objects

# Boton para comenzar un juego nuevo
buttongame = btn.ButtonSelect(White, 700, 100, 150, 50, 'Comenzar')
buttongame.draw(DISPLAYSURF, (0, 0, 0))

# Boton para ver la solución del juego
buttonsolution = btn.ButtonSelect(White, 700, 250, 150, 50, 'Ver solución')
buttonsolution.draw(DISPLAYSURF, (0, 0, 0))

#tablero = puzz.SlidePuzzle(100, 150, 500, 150, raiz.tamaniotablero())
#tablero.draw(DISPLAYSURF)

cronometro = chro.Cronos(700, 400, 150, 50)
cronometro.draw(DISPLAYSURF, (238, 217, 193))

# Recuadro correspondiente al espacio del tablero del juego
# pygame.draw.rect(DISPLAYSURF, Maroon, (275, 35, 530, 490), 0)
# font = pygame.font.SysFont('comicsans', 25)
# text = font.render('Tablero del juego', 0, White)
# DISPLAYSURF.blit(text, (290, 40))

serie = []


def ver():

    global serie
    n = raiz.tamaniotablero()
    if raiz.serie() == 1:
        serie = fun.fibonacci(n)
        #random.shuffle(serie)
        casillas = fun.arregloAMatriz(serie, n)
        xi = 20
        for i in range(n):
            yi = 15
            for j in range(n):
                if str(casillas[i][j]) == '-1':
                    casilla = puzz.Casilla(Brown, yi, xi, n, '')
                    casilla.draw(DISPLAYSURF, Brown)
                else:
                    casilla = puzz.Casilla((238, 217, 193), yi, xi, n, str(casillas[i][j]))
                    casilla.draw(DISPLAYSURF, Brown)
                yi = yi + int(560 / n) - 20
            xi = xi + int(700 / n) - 40
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


# Creando la ventana
while True:  # Importante: main game loop

    cronometro.draw(DISPLAYSURF, (238, 217, 193))

    if raiz.v.get == 0 or raiz.w.get() == 0 or raiz.x.get() == 0:
        pygame.quit()
        sys.exit()

    ver()

    for event in pygame.event.get():    # Módulo event

        pos = pygame.mouse.get_pos()

        if event.type == QUIT:  # Cuando se le da click a la X en la ventana para salir
            pygame.quit()       # Desactiva la librería Pygame
            sys.exit()          # Se encarga de terminar el programa.

        if event.type == pygame.MOUSEBUTTONDOWN:  # Cuando se da click en uno de los botones
            if buttongame.isOver(pos):
                # Se imprime en consola sólo para verificar que el botón sí está siendo escuchado
                print("Sí reacciona al click, game", ver())
            if buttonsolution.isOver(pos):
                # Se imprime en consola sólo para verificar que el botón sí está siendo escuchado
                print("Sí reacciona al click, solution")

    pygame.display.update() # draws the Surface object returned by pygame.display.set_mode() to the screen
    pygame.display.flip()


