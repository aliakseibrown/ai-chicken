import pygame
import random
from pygame.math import Vector2

class Blocks:
    def __init__(self, parent_screen,cell_size):
        self.parent_screen = parent_screen
        self.vege_image = pygame.image.load(r'resources/flower.png').convert_alpha()
        self.vege_image = pygame.transform.scale(self.vege_image, (cell_size, cell_size))

        self.lief_image = pygame.image.load(r'resources/stone.png').convert_alpha()
        self.lief_image = pygame.transform.scale(self.lief_image, (cell_size, cell_size))

        self.carrot_image = pygame.image.load(r'resources/dead.png').convert_alpha()
        self.carrot_image = pygame.transform.scale(self.carrot_image, (cell_size, cell_size))


    def locate_blocks(self, blocks_number, cell_number, body):
        for i in range(blocks_number):
            self.x = random.randint(0, cell_number-1)
            self.y = random.randint(0, cell_number-1)
            self.pos = Vector2(self.x, self.y)
            body.append(self.pos)
            #block_dict.update({self.x : 1})                # for now it may lay on each other,
        print(body)

    def place_blocks(self, parent_screen, cell_size, body, color):     #drawing blocks
        for block in body:
            x = int(block.x * cell_size)
            y = int(block.y * cell_size)
            if color == 'carrot':
                self.parent_screen.blit(self.carrot_image, (x, y))
            if color == 'leaf':
                self.parent_screen.blit(self.lief_image, (x, y))
            if color == 'vege':
                self.parent_screen.blit(self.vege_image, (x, y))
            


    def draw_lines(self, parent_screen, cell_size):  # background lines
        for i in range(1, 10):
            pygame.draw.line(self.parent_screen, (228, 253, 227), (cell_size * i, 0), (cell_size * i, parent_screen), 1)
            pygame.draw.line(self.parent_screen, (228, 253, 227), (0, cell_size * i), (parent_screen, cell_size * i), 1)
