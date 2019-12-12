import ctypes
import sys

import numpy as np
import pygame
import listeners.casilla as puzz


Brown = (13, 8, 2)


def pintar(n, casillas, DISPLAYSURF):
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


def acomodara(casillas, n):
    a = False
    for i in range(n):
        for j in range(n):
            if str(casillas[i][j]) == '-1':
                if i+1 == n:
                    ctypes.windll.user32.MessageBoxW(0, 'No se puede realizar el movimiento', 'MOVIMIENTO', 1)
                    break
                else:
                    a = True
                    temp = casillas[i][j]
                    casillas[i][j] = casillas[i+1][j]
                    casillas[i+1][j] = temp
                    break
        if a:
            break
    return casillas


def acomodarab(casillas, n):
    for i in range(n):
        for j in range(n):
            if str(casillas[i][j]) == '-1':
                if i-1 == -1:
                    ctypes.windll.user32.MessageBoxW(0, 'No se puede realizar el movimiento', 'MOVIMIENTO', 1)
                    break
                else:
                    temp = casillas[i][j]
                    casillas[i][j] = casillas[i-1][j]
                    casillas[i-1][j] = temp
                    break
    return casillas


def acomodarder(casillas, n):

    for i in range(n):
        for j in range(n):
            if str(casillas[i][j]) == '-1':
                if j-1 == -1:
                    ctypes.windll.user32.MessageBoxW(0, 'No se puede realizar el movimiento', 'MOVIMIENTO', 1)
                    break
                else:
                    temp = casillas[i][j]
                    casillas[i][j] = casillas[i][j-1]
                    casillas[i][j-1] = temp
                    break

    return casillas


def acomodarizq(casillas, n):
    for i in range(n):
        for j in range(n):
            if str(casillas[i][j]) == '-1':
                if j+1 == n:
                    ctypes.windll.user32.MessageBoxW(0, 'No se puede realizar el movimiento', 'MOVIMIENTO', 1)
                    break
                else:
                    temp = casillas[i][j]
                    casillas[i][j] = casillas[i][j+1]
                    casillas[i][j+1] = temp
                    break
    return casillas


def verificarganador(casillasjuego, casillasordenadas):
    casillas = np.ravel(casillasjuego).T
    ord = casillasordenadas[1::]
    juego = casillas[0:len(casillas)-1]
    if np.array_equal(juego, ord):
        if ctypes.windll.user32.MessageBoxW(0, 'Felicitaciones! Has ganado el juego.', 'JUEGO TERMINADO', 1):
            pygame.quit()  # Desactiva la librería Pygame
            sys.exit()


def hacermovimiento(casillas, event, n, DISPLAYSURF):

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            casillas = acomodarab(casillas, n)

        if event.key == pygame.K_UP:
            casillas = acomodara(casillas, n)

        if event.key == pygame.K_LEFT:
            casillas = acomodarizq(casillas, n)

        if event.key == pygame.K_RIGHT:
            casillas = acomodarder(casillas, n)
    pintar(n, casillas, DISPLAYSURF)
