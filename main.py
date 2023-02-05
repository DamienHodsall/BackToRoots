import pygame
import os
from scipy.signal import convolve2d
import numpy as np

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #setting bounds of game window
pygame.display.set_caption("Groots in Paris ") #name of the game

FPS = 30
BORDER = pygame.Rect(WIDTH, HEIGHT)

# for update_pos
kernel = np.array([
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ])

class Conway():

    def __init__(self):

        # rectangle to contain conway part
        self.dim = self.width, self.width = 20, 10
        self.rect = pygame.Rect(self.dim)

def update_pos(current):

    died = current*convolve2d(current, kernel, 'same')
    died[(died < 2) + (died > 3)] = 0

    return (((current == 0)*convolve2d(current, kernel, 'same') == 3) + died != 0)*1

def update_screen(surface, current, size):

    pass

def main ():
    run = True
    clock = pygame.time.Clock()

    # temporary starting input
    current = np.array([
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0],
        [0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        ])

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # this is the actual updating part
        # current = update_pos(current)

        # this is important. nothing will change without this
        # surface.update()

    pygame.quit()

if __name__ == "__main__":
    main()
