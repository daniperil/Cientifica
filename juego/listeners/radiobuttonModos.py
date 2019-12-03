import pygame


class Modos:
    def __init__(self, color, x, y, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.text = text
        self.width = 4
        self.height = 4

    def draw(self, win, color):
        # Call this method to draw the button on the screen
        if color:
            pygame.draw.circle(win, color, (self.x - 2, self.y - 2), self.width, 0)

        pygame.draw.circle(win, self.color, (self.x, self.y), self.width, 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 23)
            text = font.render(self.text, 0, (0, 0, 0))
            win.blit(text, (self.x + 10, self.y - 10))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

    def comenzar(self):
        # Se comienza
        return 0

    def mostrarsolucion(self):
        return 0