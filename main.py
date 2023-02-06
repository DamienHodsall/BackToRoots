#!/bin/python3

# standard imports
import pygame
import os
from scipy.signal import convolve2d
import numpy as np

# custom imports
import button
from Conway import Conway
pygame.font.init()

pygame.mixer.init()

DIM = WIDTH, HEIGHT = 900,500
# these should go in main
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #setting bounds of game window
pygame.display.set_caption(" Groots in Paris ") #name of the game

FPS = 30
#BORDER = pygame.Rect(WIDTH, HEIGHT)
goButtonPng = pygame.image.load("goButton.png").convert_alpha()
stopButtonPng = pygame.image.load("stopButton.png").convert_alpha()

Title_GameName = pygame.image.load(
        os.path.join('ASSETS', 'Title.png')
        )
Title_Background = pygame.image.load(
        os.path.join('ASSETS', 'eiffel tower.png')
        )
Title_Background = pygame.transform.scale(Title_Background, (900, 500))

Title_Groot_Baguette = pygame.image.load(
        os.path.join('ASSETS', 'Groot_holding_baguette.png')
        )

# os.path.join might not be necessary? relative path might be fine

'''
cells blit onto conway then conway scales and blits onto background...?
'''

# conway = Conway(start_pos)

goButton = button.Button(750, 25, goButtonPng, 0.8)
stopButton = button.Button(750,75, stopButtonPng, 0.2)

def pausedWindow():
    if goButton.draw(WIN):
        print("go")
    pygame.display.update()

def draw_window():
    WIN.blit(Title_Background, (0,0))
    WIN.blit(Title_GameName, (157,10))
    WIN.blit(Title_Groot_Baguette, (500,200))
    WIN.blit(pygame.transform.flip(Title_Groot_Baguette,1,0), (-225,200))
    pygame.display.update()

def main ():
    run = True
    clock = pygame.time.Clock()

    # temporary starting input
    '''
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
    '''

    while run:
        clock.tick(FPS)

        #pausedWindow()
        draw_window()

        if start_automation:

            conway.update_pos()
            conway.draw(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()
