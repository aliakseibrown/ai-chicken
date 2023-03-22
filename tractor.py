import pygame
import random
from pygame.math import Vector2

class Tractor:
    def __init__(self, parent_screen, cell_size):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(r'resources/robot2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (cell_size, cell_size+5))
        self.x = cell_size*2
        self.y = cell_size*2
        self.pos = Vector2(self.x, self.y)
        self.angle = 0
        self.direction = 'up'

    def draw(self):
        self.parent_screen.blit(pygame.transform.rotate(self.image, self.angle), (self.x, self.y))  # rotate tractor

    def move(self, direction, cell_size):
        if direction == 'up':
            self.y -= cell_size
            #self.angle = 0
        if direction == 'down':
            self.y += cell_size
            #self.angle = 180
        if direction == 'left':
            self.x -= cell_size
            #self.angle = 90
        if direction == 'right':
            self.x += cell_size
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