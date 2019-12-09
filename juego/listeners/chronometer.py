import ctypes
import sys

import pygame


class Cronos:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.text = "{}:{}".format(self.minutes, self.seconds)

    def draw(self, win, outline=None, modo=None, n=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, outline, (self.x, self.y, self.width, self.height), 0)

        if modo == 1:
            self.seconds = int(pygame.time.get_ticks() / 1000)
            self.minutes = int(self.seconds / 60)
            self.seconds = self.seconds % 60
        elif modo == 2:
            # tiempo que queremos que dure
            if n == 3:
                tempo = 180000  # 3 minutos
                self.seconds = int((tempo - pygame.time.get_ticks()) / 1000)
                self.minutes = int(self.seconds / 60)
                self.seconds = self.seconds % 60
            elif n == 4:
                tempo = 240000  # 4 minutos
                self.seconds = int((tempo - pygame.time.get_ticks()) / 1000)
                self.minutes = int(self.seconds / 60)
                self.seconds = self.seconds % 60
            elif n == 5:
                tempo = 300000  # 5 minutos
                self.seconds = int((tempo - pygame.time.get_ticks()) / 1000)
                self.minutes = int(self.seconds / 60)
                self.seconds = self.seconds % 60

            if self.minutes == 0 and self.seconds == 0:
                if ctypes.windll.user32.MessageBoxW(0, 'Perdiste! Se ha terminado el tiempo.', 'JUEGO TERMINADO', 1):
                    pygame.quit()  # Desactiva la librería Pygame
                    sys.exit()

        font = pygame.font.SysFont('comicsans', 60, False, False)
        self.text = "{}:{}".format(self.minutes, self.seconds)
        text = font.render(self.text, 0, (0, 0, 0))
        win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

