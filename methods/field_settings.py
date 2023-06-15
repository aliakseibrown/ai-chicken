import pygame
import random
import models.field_block as field_block


class FieldSettings:
    def __init__(self, surface, cell_size, cell_number):
        self.wet_grass_image = pygame.image.load(r'resources/grass.png').convert_alpha()
        self.wet_grass_image = pygame.transform.scale(self.wet_grass_image, (cell_size, cell_size))

        self.dry_grass_image = pygame.image.load(r'resources/dry_grass.png').convert()
        self.dry_grass_image = pygame.transform.scale(self.dry_grass_image, (cell_size, cell_size))

        self.cell_number = cell_number
        self.cell_size = cell_size
        self.surface = surface 
        self.all_blocks = []

    def locate_field(self, field_list, state, num_of_blocks):      # finds open space (coordinates)

        for i in range(num_of_blocks):
            while True:
                rand_x = random.randint(0, self.cell_number - 1)  # to-check
                rand_y = random.randint(0, self.cell_number - 1)
                if [rand_x, rand_y] not in self.all_blocks:
                    self.all_blocks.append([rand_x, rand_y])
                    if state == 0:
                        self.block = field_block.FieldBlock(
                            i, 'wet', 0, self.wet_grass_image, rand_x, rand_y
                        )
                    if state == 1:
                        self.block = field_block.FieldBlock(
                            i, 'dry', 1, self.dry_grass_image, rand_x, rand_y
                            )
                    field_list.append(self.block)
                    break


    def draw_grass(self, field_list):
        for obj in field_list:
            self.surface.blit(obj.image, (int(obj.xy[0] * self.cell_size), int(obj.xy[1] * self.cell_size)))