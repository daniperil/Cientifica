import pygame


class Casilla:
    def __init__(self, color, x, y, n, text=''):
        self.color = color
        self.x = x
        self.y = y
        if n == 3:
            self.width = int(560/n) - 20
            self.height = int(700/n) - 60
        elif n == 4:
            self.width = int(560/n) - 20
            self.height = int(700/n) - 60
        elif n == 5:
            self.width = int(560/n) - 20
            self.height = int(700/n) - 60
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 4, self.y - 4, self.width + 8, self.height + 8), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 50)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False