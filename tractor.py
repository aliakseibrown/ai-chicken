import pygame
import random
from pygame.math import Vector2

class Tractor:
    def __init__(self, parent_screen, cell_size):

        self.up = pygame.image.load(r'resources/up.png').convert_alpha()
        self.down = pygame.image.load(r'resources/down.png').convert_alpha()
        self.left = pygame.image.load(r'resources/left.png').convert_alpha()
        self.right = pygame.image.load(r'resources/right.png').convert_alpha()

        self.parent_screen = parent_screen
        #self.image = pygame.image.load(r'resources/robot3.png').convert_alpha()

        self.up = pygame.transform.scale(self.up, (cell_size, cell_size))
        self.down = pygame.transform.scale(self.down, (cell_size, cell_size+2))
        self.left = pygame.transform.scale(self.left, (cell_size+2, cell_size+2))
        self.right = pygame.transform.scale(self.right, (cell_size+3, cell_size+1))


        self.x = cell_size*2
        self.y = cell_size*2
        self.pos = Vector2(self.x, self.y)
        self.angle = 0
        self.direction = 'up'
        self.image = self.down


    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))  # rotate tractor

    def move(self, direction, cell_size):
        if direction == 'up':
            self.y -= cell_size
            self.image = self.up
            #self.angle = 0
        if direction == 'down':
            self.y += cell_size
            self.image = self.down
            #self.angle = 180
        if direction == 'left':
            self.x -= cell_size
            self.image = self.left
            #self.angle = 90
        if direction == 'right':
            self.x += cell_size
            self.image = self.right
            #self.angle = 270

    def walk(self):
        choice = ['up', 'down', 'left', 'right']

        if self.x == 450:
            choice.pop(3)
        if self.x == 0:
            choice.pop(2)
        if self.y == 0:
            choice.pop(0)
        if self.y == 450:
            choice.pop(1)

        self.direction = random.choice(choice)
        self.move(self.direction)