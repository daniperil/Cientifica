import pygame

# Se definen algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
CYAN= (0,255,255)
PURPURA=(255,10,206)
#Se define la función HOMBRECITO. Screen es variable para que sepa en qué ventana dibujar. Coordenadas X e Y para saber
#Dónde dibujar al HOMBRECITO
def HOMBRECITO(screen, x, y):

    # Cabeza
    pygame.draw.ellipse(screen, NEGRO, [1 + x, y, 10, 10], 0)

    # Piernas            #Coordenadas: inicio         fin
    pygame.draw.line(screen, PURPURA, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, PURPURA, [5 + x, 17 + y], [x, 27 + y], 2)

    # Cuerpo
    pygame.draw.line(screen, CYAN, [5 + x, 17 + y], [5 + x, 7 + y], 2)

    # Brazo
    pygame.draw.line(screen, PURPURA, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, PURPURA, [5 + x, 7 + y], [1 + x, 17 + y], 2)


# Setup
pygame.init()

# ajustes de la pantalla (alto,largo)
dimensiones = [700, 500]
screen = pygame.display.set_mode(dimensiones)

pygame.display.set_caption("El hombrecito")

# Iteración hasta que se pulse botón salir
done = False

#Gestionar qué tan rápido se actualiza la pantalla
clock = pygame.time.Clock()

# Ocultar cursor del ratón
pygame.mouse.set_visible(0)

# -------- LOOP PRINCIPAL DEL PROGRAMA -----------
while not done:
    # PROCESAMIENTO DE EVENTOS
    for event in pygame.event.get(): #El usuario hace algo
        if event.type == pygame.QUIT: #Si el usuario presiona boton de salir
            done = True #Abandona


    #LÓGICA DEL PROGRAMA

    #Se llama a la función que dibuja al HOMBRECITO.
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    #CÓDIGO DE DIBUJO

    #Llenar la ventana con algún color

    screen.fill(BLANCO)
    HOMBRECITO(screen,x,y)

    # Avanzar y actualizar la pantalla con lo que se ha dibujado
    pygame.display.flip()

    #Limitar a 60 fotogramas por segundo
    clock.tick(60)

#Cerrar la ventana y salir

pygame.quit()