import pygame
import numpy as np

#CREATES GRID WITH WIDTH HEIGHT AND NUMBER OF DIVISIONS Nx AND Ny

class Grid:
    def __init__(self, width, height, Nx, Ny):
        self.width = width
        self.height = height
        self.Nx = Nx
        self.Ny = Ny
        self.grid = np.zeros((self.Ny, self.Nx), dtype='int')
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Falling sand')
        self.black = (0,0,0)
        self.white = (250,250,250)
        self.orange = (255,165,0)
        self.gray = (128, 128, 128)
        self.dx = width / self.Nx
        self.dy = height / self.Ny

    def draw(self):
        for i in range(self.Ny):
            for j in range(self.Nx):
                if self.grid[i][j] == 0:
                    pygame.draw.rect(self.window, self.black, (j*self.dx, i*self.dy, j*self.dx + self.dx, i*self.dy + self.dy))
                elif self.grid[i][j] == 1:
                    pygame.draw.rect(self.window, self.orange, (j*self.dx, i*self.dy, j*self.dx + self.dx, i*self.dy + self.dy))

        pygame.display.update()

    def add_sand(self, mouse_pos):
        x = int(mouse_pos[0] // self.dx)
        y = int(mouse_pos[1] // self.dy)

        self.grid[y][x] = 1

    #RESETS GRID TO ORIGINAL STATE
    def reset(self):
        self.grid = np.zeros((self.Ny, self.Nx), dtype='int')

    #IETRATES BACKWARDS AND UPDATES SAND CUBE POSITIONS
    def update(self):
        for i in range(self.Nx-2, -1, -1):
            for j in range(self.Ny-1, -1, -1):
                #FALL
                if self.grid[i][j] == 1 and self.grid[i+1][j] == 0:
                    self.grid[i][j] = 0
                    self.grid[i+1][j] = 1
                #SCATTER
                if self.grid[i][j] == 1 and self.grid[i+1][j] == 1:
                    if j+1 <self.Ny and self.grid[i+1][j+1] == 0:
                        self.grid[i+1][j+1] = 1
                        self.grid[i][j] = 0

                    if j-1 > 0 and self.grid[i+1][j-1] == 0:
                        self.grid[i+1][j-1] = 1
                        self.grid[i][j] = 0




