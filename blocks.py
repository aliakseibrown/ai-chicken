import pygame
import random
from pygame.math import Vector2
import soil


class Blocks:
    def __init__(self, parent_screen,cell_size):
        self.parent_screen = parent_screen
        self.flower_image = pygame.image.load(r'resources/flower.png').convert_alpha()
        self.flower_image = pygame.transform.scale(self.flower_image, (cell_size, cell_size))

        self.stone_image = pygame.image.load(r'resources/stone.png').convert_alpha()
        self.stone_image = pygame.transform.scale(self.stone_image, (cell_size, cell_size))

        self.leaf_image = pygame.image.load(r'resources/dead.png').convert_alpha()
        self.leaf_image = pygame.transform.scale(self.leaf_image, (cell_size, cell_size))

        self.alive_leaf_image = pygame.image.load(r'resources/alive.png').convert_alpha()
        self.alive_leaf_image = pygame.transform.scale(self.alive_leaf_image, (cell_size, cell_size))

        self.fawn_seed_image = pygame.image.load(r'resources/fawn_seed.png').convert_alpha()
        self.fawn_seed_image = pygame.transform.scale(self.fawn_seed_image, (cell_size, cell_size))

        self.fawn_wheat_image = pygame.image.load(r'resources/fawn_wheat.png').convert_alpha()
        self.fawn_wheat_image = pygame.transform.scale(self.fawn_wheat_image, (cell_size, cell_size))


        self.soil = soil.Soil()

    def locate_blocks(self, blocks_number, cell_number, body):
        for i in range(blocks_number):
            self.x = random.randint(0, cell_number-1)
            self.y = random.randint(0, cell_number-1)
            self.pos = [self.x,self.y]
            body.append(self.pos)
            #entire_block.update({self.x : 1})                # for now it may lay on each other,
        #print(entire_block)

    def place_blocks(self, parent_screen, cell_size, body, color):     #drawing blocks
        for block in body:
            x = int(block[0] * cell_size)
            y = int(block[1] * cell_size)
            if color == 'leaf':
                self.parent_screen.blit(self.leaf_image, (x, y))
            if color == 'alive':
                self.parent_screen.blit(self.alive_leaf_image, (x, y))
            if color == 'stone':
                self.parent_screen.blit(self.stone_image, (x, y))
            if color == 'flower':
                self.parent_screen.blit(self.flower_image, (x, y))
            if color == 'fawn_seed':
                self.parent_screen.blit(self.fawn_seed_image, (x, y))
            if color == 'fawn_wheat':
                self.parent_screen.blit(self.fawn_wheat_image, (x, y))



            # if color == 'potato':
            #     pass

    def locate_soil(self, name, acidity, irrigation, blocks_number):
        # for block in blocks_number:
        self.soil.set_name(name)
        self.soil.set_irrigation(irrigation)
        self.soil.set_acidity(acidity)

    def get_soil_info(self):
        return self.soil

    def draw_lines(self, parent_screen, cell_size):  # background lines
        for i in range(1, 10):
            pygame.draw.line(self.parent_screen, (228, 253, 227), (cell_size * i, 0), (cell_size * i, parent_screen), 1)
            pygame.draw.line(self.parent_screen, (228, 253, 227), (0, cell_size * i), (parent_screen, cell_size * i), 1)





