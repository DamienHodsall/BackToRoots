import pygame
import os
from scipy.signal import convolve2d
import numpy as np
import button

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #setting bounds of game window
pygame.display.set_caption(" Groots in Paris ") #name of the game

goButtonPng = pygame.image.load("goButton.png").convert_alpha()
stopButtonPng = pygame.image.load("stopButton.png").convert_alpha()

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

goButton = button.Button(750, 25, goButtonPng, 0.8)
stopButton = button.Button(750,75, stopButtonPng, 0.2)

def pausedWindow():
    if goButton.draw(WIN):
        print("go")
    pygame.display.update()     

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
        pausedWindow()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # current = update_pos(current)

    pygame.quit()

if __name__ == "__main__":
    main()
