# Create some moving blocks using pygame
# James Francis, Jun 2020
#
# Adapted from a program by Al Sweigart
# See his brilliant website http://inventwithpython.com and book "Invent your own Computer Games with Python"
# Page ref http://inventwithpython.com/invent4thed/chapter18.html
#

import pygame, sys, time
from pygame.locals import *

# Set up pygame.
pygame.init()

# Set up the window.
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation')


# Set up the colors.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the block sprite
class Block:
    def __init__(self, a, b, c, d, colour):
        self.rect = pygame.Rect(a, b, c, d)
        self.colour = colour

block = Block(100,100,100,100, BLUE)

# Run the game loop.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw the white background onto the surface.
    windowSurface.fill(WHITE)

    # Draw the box onto the surface.
    pygame.draw.rect(windowSurface, block.colour, block.rect)

    # Draw the window onto the screen.
    pygame.display.update()
    time.sleep(0.02)