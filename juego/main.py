
##
import os
import pygame, sys          # import statement that imports the pygame and sys modules
from pygame.locals import *
import listeners.buttonselect as btn  # import para crear los botones
#import listeners.chronometer as chro
import listeners.radiobuttonModos as ramo # import para crear los radioButtons
#import listeners.radiobuttonSeries as rase
#import listeners.radiobuttonTamanio as rata
#import listeners.puzzle as puzz

# Se asignan valores con respecto al tamaño de la pantalla para ubicar la ventana principal en el centro
x = 180
y = 105
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

pygame.init()   # Inicializa cada módulo importado con pygame. it needs to be called first in order for many Pygame functions to work
DISPLAYSURF = pygame.display.set_mode((1050, 560))   # Tamaño en pixeles de la superficie de la ventana, tupla: (ancho,alto)
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
Green = (0,128,0)
Lime = ( 0,255, 0)
Maroon = (33, 12, 8)
Navy_Blue = (0, 0, 128)
Olive = (128, 128, 0)
Purple = (128, 0, 128)
Red = (255, 0, 0)
Silver = (192, 192, 192)
Teal = (0, 128, 128)
White = (255, 255, 255)
Yellow = (255, 255, 0)

# DISPLAYSURF.fill(Maroon)         # Método para llenar de color blanco la superficie del objeto. Método de: pygame.Surface objects

'''
Instrucciones para dibujar diferentes figuras geométricas
'''
# pygame.draw.polygon(surface, color, pointlist, width)
# pygame.draw.line(surface, color, start_point, end_point, width)
# pygame.draw.lines(surface, color, closed, pointlist, width)
# pygame.draw.circle(surface, color, center_point, radius, width)
# pygame.draw.ellipse(surface, color, bounding_rectangle, width)
# pygame.draw.rect(surface, color, rectangle_tuple, width)

# pygame.draw.polygon(DISPLAYSURF, Yellow, ((146,0), (291,105),(236,277),(45,105)))
# pygame.draw.line(DISPLAYSURF, Teal, (240, 200), (240, 300), 5)
# pygame.draw.line(DISPLAYSURF, Teal, (820, 200), (820, 300), 5)
# pygame.draw.circle(DISPLAYSURF, Lime, (250,80),50,2)

# Recuadro que sorresponde al modo de juego
# pygame.draw.rect(DISPLAYSURF, Maroon, (17, 17, 230, 90), 0)
# font = pygame.font.SysFont('comicsans', 25)
# text = font.render('Modo de juego', 0, White)
# DISPLAYSURF.blit(text, (35, 22))

# Recuadro que sorresponde a la serie numérica del juego
# pygame.draw.rect(DISPLAYSURF, Maroon, (17, 115, 230, 300), 0)
# font = pygame.font.SysFont('comicsans', 25)
# text = font.render('Serie numérica', 0, White)
# DISPLAYSURF.blit(text, (35, 120))


# Recuadro que sorresponde al tamaño del tablero del juego
# pygame.draw.rect(DISPLAYSURF, Maroon, (17, 425, 230, 125), 0)
# font = pygame.font.SysFont('comicsans', 25)
# text = font.render('Tamaño del tablero', 0, White)
# DISPLAYSURF.blit(text, (35, 430))

# Boton para comenzar un juego nuevo
buttongame = btn.ButtonSelect(Silver, 850, 100, 150, 70, 'Comenzar')
buttongame.draw(DISPLAYSURF, (0, 0, 0))

# Boton para ver la solución del juego
buttonsolution = btn.ButtonSelect(Silver, 850, 250, 150, 70, 'Ver solución')
buttonsolution.draw(DISPLAYSURF, (0, 0, 0))

# cronometro = chro.chronometer()
# cronometro.draw(DISPLAYSURF, (50, 50, 50))
# Opción del modo de juego. Aventura
# modos = ramo.Modos(White, 30, 60, 'Aventura: sin tiempo límite')
# modos.draw(DISPLAYSURF, White)
# Opción del modo de juego. Desafío
# modos2 = ramo.Modos(White, 30, 90, 'Desafío: con tiempo límite')
# modos2.draw(DISPLAYSURF, White)

#series = rase.radiobuttonSeries()
#series.draw(DISPLAYSURF, (50, 150))
#tamanio = rata.radiobuttonTamanio()
#tamanio.draw(DISPLAYSURF, (50, 200))
#rompecabezas = puzz.SlidePuzzle(400,20,2)
#rompecabezas.draw(DISPLAYSURF)

# Recuadro correspondiente al espacio del tablero del juego
# pygame.draw.rect(DISPLAYSURF, Maroon, (275, 35, 530, 490), 0)
# font = pygame.font.SysFont('comicsans', 25)
# text = font.render('Tablero del juego', 0, White)
# DISPLAYSURF.blit(text, (290, 40))

# Creando la ventana
while True: # Importante: main game loop

    for event in pygame.event.get():    # Módulo event

        pos = pygame.mouse.get_pos()

        if event.type == QUIT:  # Cuando se le da click a la X en la ventana para salir
            pygame.quit()       # Desactiva la librería Pygame
            sys.exit()          # Se encarga de terminar el programa.

        if event.type == pygame.MOUSEBUTTONDOWN:  # Cuando se da click en uno de los botones
            if buttongame.isOver(pos):
                # Se imprime en consola sólo para verificar que el botón sí está siendo escuchado
                print("Sí reacciona al click, game")
            if buttonsolution.isOver(pos):
                # Se imprime en consola sólo para verificar que el botón sí está siendo escuchado
                print("Sí reacciona al click, solution")

        if event.type == pygame.MOUSEMOTION: # Cuando el mouse pasa por encima del botón
            # Aún no funciona
            if buttongame.isOver(pos):
                buttongame.color = Olive
            else:
                buttongame.color = Black
        #modos.update_checkbox(event)

    #modos.render_checkbox()
    pygame.display.update() # draws the Surface object returned by pygame.display.set_mode() to the screen
    pygame.display.flip()
