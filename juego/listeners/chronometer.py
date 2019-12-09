import pygame


class Cronos:

    def __init__(self, x, y, width, height):
        self.clock = pygame.time.Clock()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.hours = 0
        self.text = "{}:{}:{}".format(self.hours, self.minutes, self.seconds)

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, outline, (self.x, self.y, self.width, self.height), 0)
        self.seconds = int(pygame.time.get_ticks() / 1000)
        if self.seconds == 10:
            self.clock = pygame.time.Clock()
            self.minutes += 1
            self.seconds = 0
        if self.minutes == 10 and self.seconds == 0:
            self.hours += 1
            self.minutes = 0
        font = pygame.font.SysFont('comicsans', 60, False, False)
        self.text = "{}:{}:{}".format(self.hours, self.minutes, self.seconds)
        text = font.render(self.text, 0, (0, 0, 0))
        win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    # while True:  # game loop
        # do stuff here
    #    if self.milliseconds > 1000:
    #        self.seconds += 1
    #        self.milliseconds -= 1000
    #    if self.seconds > 60:
    #        self.minutes += 1
    #        self.seconds -= 60

        # print("{}:{}".format(minutes, seconds))

    #    milliseconds += clock.tick_busy_loop(60)
