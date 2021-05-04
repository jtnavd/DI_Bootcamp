import pygame
import numpy as np
import random

# display the grid
class Grid:
    def __init__(self, height, scale, offset):
        # scale takes the total number which is divide by 2 for x and y
        self.scale = scale
        # X
        self.columns = int(height/2)
        # Y
        self.rows = int(width/2)
        self.size= (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=(self.size))
        self.offset = offset

    # binary randomizer
    # default status
    def random2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0,1)


    def GoL(self, off_color, on_color, surface):
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale
                
                if self.grid_array[x][y] = 1:
                    pygame.draw.rect(Surface, on_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                else:
                    pygame.draw.rect(Surface, on_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
        next = up.ndarray(shape=(self.size))
        for x in range(self.rows):
            for y in range(self.columns):
                state = self.grid_array[x][y]
                neighbor = self.get_neighbor(x,y)
                #  if there's 3 neighbours, cells multiply
                if state == 0 and neighbor == 3:
                    next[x][y]=1
                #  if there's less than 2 or bigger than 3 neighbours, cells die
                elif state == 1 and (neighbor < 2 or neighbor > 3):
                    next[x][y]=0
                #  pass to next generation, cells survive
                else:
                    next[x][y] = state
            self.grid_array = next

    def get_neighbor(self, x, y):
        total = 0
        for n in range(-1,2):
            for m in range(-1,2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total