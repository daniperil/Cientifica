import pygame, sys, os, random


# This class needs to have 3 arguments the grid size, the size of the tiles and the size of the margin
class SlidePuzzle:
    def __init__(self, gs, ts, ms):
        self.gs, self.ts, self.ms = gs, ts, ms
        # Determines that there is going to be one tile less
        self.tiles_len = gs[0]*gs[1]-1
        self.tiles = [(x,y) for y in range(gs[1]) for x in range(gs[0])]

        self.tilepos = {(x,y):(x*(ts+ms)+ms,y*(ts+ms)+ms) for y in range(gs[1]) for x in range(gs[0])}
        self.prev = None

        # This is going to implement the letters

        self.images = []; font = pygame.font.Font(None, 120)
        for i in range(self.tiles_len):
            # This part is to be able to import the images
            image = pygame.Surface((ts,ts)); image.fill((0,255,0))
            text = font.render(str(i+1),2,(0,0,0)); w,h = text.get_size()
            # The ts-w/2 and ts-h/2 is to put the numbers in the center
            image.blit(text,((ts-w)/2,(ts-h)/2)); self.images+=[image]


    # Function to get the blank space of the puzzle
    def getBlank(self): return self.tiles[-1]
    # Function to create a new blank
    def setBlank(self, pos): self.tiles[-1] = pos
    opentile = property(getBlank, setBlank)
    # Method for switching tiles (we are always going to swap with the blank, and the blank is always going to be
    # at the end of the array (opentile)
    def switch(self,tile): self.tiles[self.tiles.index(tile)], self.opentile, self.prev = self.opentile,tile,self.opentile
    def in_grid(self,tile): return tile[0]>=0 and tile[0]<self.gs[0] and tile[1]>=0 and tile[1]<self.gs[1]

    # Method to identify if the tiles are adjacent or not
    def adjacent(self): x,y =self.opentile; return (x-1,y),(x+1,y), (x,y-1),(x,y+1)

    def random(self):
        adj = self.adjacent(); self.switch(random([pos for pos in adj if self.in_grid(pos) and pos!=self.prev]))

    def update(self,dt):
    # Defines relation with mouse
        mouse = pygame.mouse.get_pressed()
        mpos = pygame.mouse.get_pos()

    # Now we decalre a relation between the tile and the mouse
        if mouse[0]:
            # x is to solve the problem of the margin
            x,y = mpos[0]%(self.ts+self.ms), mpos[1]%(self.ts+self.ms)
            if x>self.ms and y>self.ms:
                tile = mpos[0]//self.ts,mpos[1]//self.ts
                #this part is what allows to switch tiles using the mouse
                if self.in_grid(tile) and tile in self.adjacent(): self.switch(tile)

    #
    def draw(self, screen):
        for i in range(self.tiles_len):
            x, y = self.tilepos[self.tiles[i]]
            screen.blit(self.images[i],(x,y))

    # This method is what helps the user interact with the game with the keyboard
    def events(self,event):
        if event.type == pygame.KEYDOWN:
            for key, dx, dy in ((pygame.K_w,0,-1),(pygame.K_s,0,1),(pygame.K_a,-1,0),(pygame.K_d,1,0)):
                if event.key == key:
                    x,y = self.opentile;tile = x+dx,y+dy
                    if self.in_grid(tile): self.switch(tile)

            if event.key == pygame.K_SPACE:
                for i in range (100): self.random()


def main():
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption('Slide Puzzle')
    screen = pygame.display.set_mode((800,600))
    fpsclock = pygame.time.Clock()
    # Shows the main screen determines the sizes
    program = SlidePuzzle((3,3), 160, 5)

    while True:
        dt = fpsclock.tick()/100
        screen.fill((0,0,0))
        program.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:pygame.quit(); sys.exit()
            program.events(event)

        program.update(dt)


if __name__ == '__main__':
    main()