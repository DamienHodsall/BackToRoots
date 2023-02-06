"""
class for conway part of the game
"""

import pygame
import numpy as np
from scipy.signal import convolve2d

class Conway():

    def __init__(self, start_pos, width = 20, height = 10):

        self.background = pygame.image.load('ASSETS/conway-background.png').convert()
        self.cell = pygame.image.load('ASSETS/cell.png').convert()
        self.dim = self.width, self.height = width, height
        self.array = np.zeros(self.dim) # cells of playing area (dirt_background - green_top_area)
        self.init(start_pos)
        self.kernel = np.array([
            [1,1,1],
            [1,0,1],
            [1,1,1]
            ])

    def init(self, start_pos):
        '''
        can also be used for restart simulation?
        '''

        self.array = np.zeros(self.dim)

        # puts edited position into automated array
        self.array[:start_pos.shape[0], :start_pos.shape[1]] = start_pos

    def draw(self, background, dim):
        '''
        puts Grid-Fill on all True postions in self.array and draws onto background
        '''

        self.background = pygame.image.load('ASSETS/conway-background.png').convert()

        for row, col in np.ndindex(self.array.shape):

            if self.array[row, col]:

                self.background.blit(source = self.cell, dest = (8*row, 8*col))

        self.background = pygame.transform.scale(self.background, (900,450))

        background.blit(self.background, (0, 112))

    def update_pos(self):
        '''
        performs the actual logic for Conwat's game of life
        '''

        died = self.array*convolve2d(self.array, self.kernel, 'same')
        died[(died < 2) + (died > 3)] = 0

        self.array = (((self.array == 0)*convolve2d(self.array, self.kernel, 'same') == 3) + died != 0)*1
