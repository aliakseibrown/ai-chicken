import pygame
import random

class Land:
    def __init__(self, cell_size, cell_number, grass_body):
        self.grass_image = pygame.image.load(r'resources/grass.png').convert()
        self.grass_image = pygame.transform.scale(self.grass_image, (cell_size, cell_size))

        self.bad_grass_image = pygame.image.load(r'resources/bad_grass.png').convert()
        self.bad_grass_image = pygame.transform.scale(self.bad_grass_image, (cell_size, cell_size))

        for i in range(0, cell_number):
            for k in range(0, cell_number):
                grass_body.append([i,k])
                

    def place_grass(self, parent_screen, cell_number, cell_size, grass_body, name):
        for body in grass_body:
            x = int(body[0] * cell_size)
            y = int(body[1] * cell_size)
            if(name == 'good'):
                parent_screen.blit(self.grass_image, (x, y))  # to-check: () redundant parentheses
            if(name == 'bad'):
                parent_screen.blit(self.bad_grass_image, (x, y))
                