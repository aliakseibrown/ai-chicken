import pygame
import random

class Tractor:
    def __init__(self, parent_screen, cell_size):
        self.parent_screen = parent_screen

        self.up = pygame.image.load(r'resources/up.png').convert_alpha()
        self.down = pygame.image.load(r'resources/down.png').convert_alpha()
        self.left = pygame.image.load(r'resources/left.png').convert_alpha()
        self.right = pygame.image.load(r'resources/right.png').convert_alpha()

        self.up = pygame.transform.scale(self.up, (cell_size+2, cell_size))
        self.down = pygame.transform.scale(self.down, (cell_size, cell_size+2))
        self.left = pygame.transform.scale(self.left, (cell_size+2, cell_size+2))
        self.right = pygame.transform.scale(self.right, (cell_size+4, cell_size+1))

        self.x = cell_size*2  # to-check: start pos may be written explicit
        self.y = cell_size*2
        #self.pos = Vector2(self.x, self.y)
        self.angle = 0
        self.direction = 'up'
        self.image = self.down


    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))  # rotate tractor


    def move(self, direction, cell_size, cell_number):
        if direction == 'up':
            if self.y != 0:
                self.y -= cell_size
            self.image = self.up
        if direction == 'down':
            if self.y != (cell_number-1)*cell_size:
                self.y += cell_size
            self.image = self.down
        if direction == 'left':
            if self.x != 0:
                self.x -= cell_size
            self.image = self.left
        if direction == 'right':
            if self.x != (cell_number-1)*cell_size:
                self.x += cell_size
            self.image = self.right
        print(self.x, self.y)

    def water(self, body_before, body_after, cell_size):
        self.pos = [self.x/cell_size, self.y/cell_size]
        if self.pos in body_before:
            body_before.remove(self.pos)
            body_after.append(self.pos)
            print('HERE!')
        #print(body)

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