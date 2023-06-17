import pygame
import random

class Chicken:
    def __init__(self, surface, cell_size, cell_number):
        self.surface = surface
        self.lastVisitedBlocks = []  # Chicken stores last 3 visited blocks

        self.up = pygame.image.load(r'resources/chicken/up.png').convert_alpha()
        self.down = pygame.image.load(r'resources/chicken/down.png').convert_alpha()
        self.left = pygame.image.load(r'resources/chicken/left.png').convert_alpha()
        self.right = pygame.image.load(r'resources/chicken/right.png').convert_alpha()

        self.up = pygame.transform.scale(self.up, (cell_size+2, cell_size))
        self.down = pygame.transform.scale(self.down, (cell_size, cell_size+2))
        self.left = pygame.transform.scale(self.left, (cell_size+2, cell_size+2))
        self.right = pygame.transform.scale(self.right, (cell_size+4, cell_size+1))

        self.x = 1 # to-check: start pos may be written explicit
        self.y = 1
        self.angle = 180
        self.direction = 'up'
        self.image = self.down
        self.step = 0
        self.cell_size = cell_size
        self.cell_number = cell_number
        
    def move(self, direction):
        print('MOVE')
        if direction == 'move':
            if self.angle == 0 and self.y != 0:
                self.y -= 1
            if self.angle == 90 and self.x != (self.cell_number-1):
                self.x += 1
            if self.angle == 180 and self.y != (self.cell_number-1):
                self.y += 1
            if self.angle == 270 and self.x != 0:
                self.x -= 1
        if direction == 'right':
            self.angle += 90
            if self.angle == 360:
                self.angle = 0
        if direction == 'left':
            self.angle -= 90
            if self.angle == -90:
                self.angle = 270

        if self.angle == 0:
            self.image = self.up
        if self.angle == 90:
            self.image = self.right
        if self.angle == 180:
            self.image = self.down
        if self.angle == 270:
            self.image = self.left

        self.step = self.step + 1
        print(self.x, self.y)
        print('step: ', self.step)
        
    def water(self, xy , plant_list):
        for obj in plant_list:
            if obj.xy == xy:
                obj.state = 1

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

    def draw(self):
        self.surface.blit(self.image, (self.x * self.cell_size, self.y * self.cell_size))  # rotate tractor
