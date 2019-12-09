import pygame
import random
import sys


class SlidePuzzle:
    def __init__(self, x, y, width, height, n):
        self.IMAGE_FILE = "./imagenes/back.jpg"
        self.IMAGE_SIZE = (width, height)
        self.x = x
        self.y = y
        self.TILE_WIDTH = width
        self.TILE_HEIGHT = height
        self.COLUMNS = n
        self.ROWS = n

        # bottom right corner contains no tile
        self.EMPTY_TILE = (n-1, n-1)
        self.BLACK = (0, 0, 0)

        # horizontal and vertical borders for tiles
        self.hor_border = pygame.Surface((self.TILE_WIDTH, 1))
        self.hor_border.fill(self.BLACK)
        self.ver_border = pygame.Surface((1, self.TILE_HEIGHT))
        self.ver_border.fill(self.BLACK)

        # load the image and divide up in tiles
        # putting borders on each tile also adds them to the full image
        self.image = pygame.image.load(self.IMAGE_FILE)
        self.tiles = {}
        for c in range(self.COLUMNS):
            for r in range(self.ROWS):
                tile = self.image.subsurface(
                    c*self.TILE_WIDTH, r*self.TILE_HEIGHT,
                    self.TILE_WIDTH, self.TILE_HEIGHT)
                self.tiles[(c, r)] = tile
                if (c, r) != self.EMPTY_TILE:
                    tile.blit(self.hor_border, (0, 0))
                    tile.blit(self.hor_border, (0, self.TILE_HEIGHT-1))
                    tile.blit(self.ver_border, (0, 0))
                    tile.blit(self.ver_border, (self.TILE_WIDTH-1, 0))
                    # make the corners a bit rounded
                    tile.set_at((1, 1), self.BLACK)
                    tile.set_at((1, self.TILE_HEIGHT-2), self.BLACK)
                    tile.set_at((self.TILE_WIDTH-2, 1), self.BLACK)
                    tile.set_at((self.TILE_WIDTH-2, self.TILE_HEIGHT-2), self.BLACK)
        self.tiles[self.EMPTY_TILE].fill(self.BLACK)

        # keep track of which tile is in which position
        self.state = {(col, row): (col, row)
                      for col in range(self.COLUMNS) for row in range(self.ROWS)}

        # keep track of the position of the empty tyle
        (emptyc, emptyr) = self.EMPTY_TILE

        # start game and display the completed puzzle
        pygame.init()
        self.display = pygame.display.set_mode(self.IMAGE_SIZE)
        pygame.display.set_caption("shift-puzzle")
        self.display.blit(self.image, (0, 0))
        pygame.display.flip()

    # swap a tile (c, r) with the neighbouring (emptyc, emptyr) tile
    def shift(self, c, r):
        global emptyc, emptyr
        self.display.blit(
            self.tiles[self.state[(c, r)]],
            (emptyc*self.TILE_WIDTH, emptyr*self.TILE_HEIGHT))
        self.display.blit(
            self.tiles[self.EMPTY_TILE],
            (c*self.TILE_WIDTH, r*self.TILE_HEIGHT))
        self.state[(emptyc, emptyr)] = self.state[(c, r)]
        self.state[(c, r)] = self.EMPTY_TILE
        (emptyc, emptyr) = (c, r)
        pygame.display.flip()

    # shuffle the puzzle by making some random shift moves
    def shuffle(self):
        global emptyc, emptyr
        # keep track of last shuffling direction to avoid "undo" shuffle moves
        last_r = 0
        for i in range(75):
            # slow down shuffling for visual effect
            pygame.time.delay(50)
            while True:
                # pick a random direction and make a shuffling move
                # if that is possible in that direction
                r = random.randint(1, 4)
                if last_r + r == 5:
                    # don't undo the last shuffling move
                    continue
                if r == 1 and (emptyc > 0):
                    self.shift(emptyc - 1, emptyr) # shift left
                elif r == 4 and (emptyc < self.COLUMNS - 1):
                    self.shift(emptyc + 1, emptyr) # shift right
                elif r == 2 and (emptyr > 0):
                    self.shift(emptyc, emptyr - 1) # shift up
                elif r == 3 and (emptyr < self.ROWS - 1):
                    self.shift(emptyc, emptyr + 1) # shift down
                else:
                    # the random shuffle move didn't fit in that direction
                    continue
                last_r = r
                break  # a shuffling move was made


# process mouse clicks
    # at_start = True
    # showing_solution = False
        # while True:
        # event = pygame.event.get()
            # if event.type == pygame.QUIT:
            # pygame.quit()
        # sys.exit()
            # elif event.type == pygame.MOUSEBUTTONDOWN:
                # if at_start:
                # shuffle after the first mouse click
                # shuffle()
            # at_start = False
                # elif event.dict['button'] == 1:
            # mouse left button: move if next to the empty tile
            # mouse_pos = pygame.mouse.get_pos()
                #c = mouse_pos[0] / TILE_WIDTH
                #r = mouse_pos[1] / TILE_HEIGHT
                #if (abs(c - emptyc) == 1 and r == emptyr) or (abs(r - emptyr) == 1 and c == emptyc):
                #    shift(c, r)
                #    elif event.dict['button'] == 3:
                # mouse right button: show solution image
                #saved_image = display.copy()
                #display.blit(image, (0, 0))
                # pygame.display.flip()
        # showing_solution = True
            # elif showing_solution and (event.type == pygame.MOUSEBUTTONUP):
            # stop showing the solution
            #display.blit(saved_image, (0, 0))
            # pygame.display.flip()
# showing_solution = False