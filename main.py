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
        clock.tick(FPS)
        
        #pausedWindow()
        draw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # current = update_pos(current)

    pygame.quit()

if __name__ == "__main__":
    main()
