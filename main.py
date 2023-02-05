import pygame
import os
from scipy.signal import convolve2d

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #setting bounds of game window
pygame.display.set_caption(" Name Pending ") #name of the game

# for update_pos
kernel = np.array([
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ])

def update_pos(current):

    died = current*convolve2d(current, kernel, 'same')
    died[(died < 2) + (died > 3)] = 0

    return (((current == 0)*convolve2d(current, kernel, 'same') == 3) + died != 0)*1

def main ():
    run = True

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

        # current = update_pos(current)

    pygame.quit()

if __name__ == "__main__":
    main()
