# standard imports
import pygame
import os
from scipy.signal import convolve2d
import numpy as np
from pygame import mixer

# custom imports
import button
from Conway import Conway

pygame.font.init()
pygame.mixer.init()

black = (0,0,0,128)
'''
COLOR_BG = (10,10,10)
COLOR_GRID = (40,40,40)
DIE = (170,170,170)
ALIVE = (255,255,255)

def updater (screen, cells, size, with_progress = False):
   updated_cells = np.enpty((cells.shape[0], cells.shape[1]))

   for row, col in np.ndindex(cells.shape):
    alive = np.sum(cells[row-1:row+2, col - 1: col+2]) - cells[row, col]
    color = COLOR_BG if cells[row, col] == 0 else ALIVE

    if cells[row, col]  == 1:
        if alive < 2 or alive > 3:
            if with_progress:
                color = DIE
        elif 2 <= alive <= 3:
            updated_cells[row, col] = 1
            if with_progress:
                color = ALIVE
    else:
        if alive == 3:
            updated_cells[]
'''
DIM = WIDTH, HEIGHT = 900,500
# these should go in main
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #setting bounds of game window
pygame.display.set_caption(" Groots in Paris ") #name of the game

Title_Screen_Music = mixer.music.load(
        os.path.join('ASSETS', 'Groot-In-Paris-Instrumental.mp3')
        )

FPS = 30
#BORDER = pygame.Rect(WIDTH, HEIGHT)
goButtonPng = pygame.image.load("ASSETS/goButton.png").convert_alpha()
stopButtonPng = pygame.image.load("ASSETS/stopButton.png").convert_alpha()
startButtonPng = pygame.image.load("ASSETS/startButton.png").convert_alpha()
dirtBackground = pygame.image.load("ASSETS/Dirt-Background.png").convert_alpha()
returnButtonPng = pygame.image.load("ASSETS/returnButton.png").convert_alpha()


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

goButton = button.Button(750, 10, goButtonPng, 0.8)
stopButton = button.Button(750,75, stopButtonPng, 0.2)
startButton = button.Button(WIDTH/2 - 230/2, HEIGHT / 2 - 126/2, startButtonPng, 0.8)
startClicked = False
returnButton = button.Button(15, 10, returnButtonPng, 0.5)

def pausedWindow():
    WIN.blit(dirtBackground, (0,0))
    if goButton.draw(WIN):
        return "conway"
    else:
        return "paused"


def Title_window():
    WIN.blit(Title_Background, (0,0))
    WIN.blit(Title_GameName, (157,10))
    WIN.blit(Title_Groot_Baguette, (500,200))
    WIN.blit(pygame.transform.flip(Title_Groot_Baguette,1,0), (-225,200))
    if startButton.draw(WIN):
        return "paused"
    else:
        return "title"

def main ():
    STATE = 'title'
    #Title_Screen_Music.play()
    mixer.music.play()
    #pygame.time.wait(5000)
    run = True
    clock = pygame.time.Clock()

    # temporary starting input
    temp = np.array([
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

    temp = np.array([
        [0,0,1,0],
        [0,0,0,1],
        [0,1,1,1]
        ])

    conway = Conway(temp.T)

    while run:
        clock.tick(FPS)

        if STATE == "title":
            STATE = Title_window()
        elif STATE == "paused":
            STATE = pausedWindow()

        if STATE == 'conway':

            conway.draw(WIN, DIM)
            conway.update_pos()
            clock.tick(FPS//10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
