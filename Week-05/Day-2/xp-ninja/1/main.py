############# CONWAY'S GAME OF LIFE ###############

# RULES
# A cell with less than 2 neighbours dies (underpopulation) ====================> die
# A cell with 2 or 3 neighbours lives to next generation (stable population) ===> survive
# A cell with more than 3 neighbours dies (overpopulation)======================> die
# A cell with exactly 3 neighbours become alive (reproduction) =================> multiply

import pygame
import os
os.environ["SDI_VIDEO_CENTERED"] = '1'

# screen display
width, height = 1920, 1080
size = (width, height)

pygame.init()
pygame.display.set_caption("Conway's Game of Life by Jonathan Avidar")
# takes the # screen display 
screen = pygame.display.set_mode(size)
# set time
clock = pygame.time.Clock()
tps = 60

# main colors
black = (0,0,0)
blue = (0,14,71)
white = (255,255,255)

scaler = 40
offset = 1

Grid = grid.Grid(width, height)
Grid.random2d_array()

run = True
while  run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.quit():
            run = False

    Grid.GoL(off_color==white, on_color=blue, surface=screen)
    pygame.display.update()

pygame.quit()
