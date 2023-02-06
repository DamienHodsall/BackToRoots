# standard imports
import pygame
import os
from scipy.signal import convolve2d
import numpy as np
# from pygame import mixer

# custom imports
import button
from Conway import Conway

# pygame.font.init()
# pygame.mixer.init()
DIM = WIDTH, HEIGHT = 900,564

WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #setting bounds of game window
pygame.display.set_caption(" Back To Roots ") #name of the game

FPS = 30
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
returnButton = button.Button(15, 10, returnButtonPng, 0.5)
# restartButton = button.Button(600, 10, restartButtonPng, 0.8)

def editor():

    WIN.blit(dirtBackground, (0,0))

    if goButton.draw(WIN):

        return "conway"

    else:

        return "editor"

def Title_window():

    WIN.blit(Title_Background, (0,0))
    WIN.blit(Title_GameName, (157,10))

    if startButton.draw(WIN):

        return "editor"

    else:

        return "title"

def conway_window(start_pos):

    conway = Conway(start_pos)

    if stopButton.draw(WIN):

        return 'title'

    elif restartButton.draw(WIN):

        conway.init(start_pos)

        return 'conway'

    else:

        return 'editor'

def main ():

    STATE = 'title'
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

    temp1 = np.array([
            [0,0,0,0],
            [0,0,0,1],
            [0,1,1,0],
            [0,0,1,0]
            ])

    temp1 = np.array([
        [0,0,0],
        [0,0,1],
        [0,0,1],
        [0,0,1],
        [0,0,1]
        ])

    # input needs to be transposed if it is hardcoded
    conway = Conway(temp.T)

    while run:

        clock.tick(FPS)

        if STATE == "title":

            STATE = Title_window()

        elif STATE == "editor":

            STATE = editor()

        if STATE == 'conway':

            conway.draw(WIN, DIM)
            conway.update_pos()
            clock.tick(FPS//10)

            if stopButton.draw(WIN):

                STATE = 'title'
                conway.init(temp.T)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":

    main()
