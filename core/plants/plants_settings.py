import pygame
import random
from core.plants import plant



class PlantsSettings:
    def __init__(self, surface, cell_size, cell_number):
        self.cell_number = cell_number
        self.cell_size = cell_size
        self.surface = surface 
        self.all_blocks = []
    
        self.flower_image = pygame.image.load(r'resources/plants/flower.png').convert_alpha()
        self.flower_image = pygame.transform.scale(self.flower_image, (self.cell_size, self.cell_size))

        self.eggplant_image = pygame.image.load(r'resources/vegies/1.png').convert_alpha()
        self.eggplant_image = pygame.transform.scale(self.eggplant_image, (self.cell_size, self.cell_size))

        self.stone_image = pygame.image.load(r'resources/stones/stone.png').convert_alpha()
        self.stone_image = pygame.transform.scale(self.stone_image, (self.cell_size, self.cell_size))

        self.bush_image = pygame.image.load(r'resources/plants/bush.png').convert_alpha()
        self.bush_image = pygame.transform.scale(self.bush_image, (self.cell_size, self.cell_size))

        self.ivy_image = pygame.image.load(r'resources/plants/ivy.png').convert_alpha()
        self.ivy_image = pygame.transform.scale(self.ivy_image, (self.cell_size, self.cell_size))

        self.wheat_dead_image = pygame.image.load(r'resources/plants/wheat_dead.png').convert_alpha()
        self.wheat_dead_image = pygame.transform.scale(self.wheat_dead_image, (self.cell_size, self.cell_size))
        self.wheat_image = pygame.image.load(r'resources/plants/wheat.png').convert_alpha()
        self.wheat_image = pygame.transform.scale(self.wheat_image, (self.cell_size, self.cell_size))

        self.aim_image = pygame.image.load(r'resources/aim.png').convert_alpha()
        self.aim_image = pygame.transform.scale(self.aim_image, (self.cell_size, self.cell_size))

    def locate_plant(self, field_list, name, num_of_blocks):      # finds open space (coordinates)

        for i in range(num_of_blocks):
            while True:
                rand_x = random.randint(0, self.cell_number - 1)  # to check
                rand_y = random.randint(0, self.cell_number - 1)
                if [rand_x, rand_y] not in self.all_blocks:
                    self.all_blocks.append([rand_x, rand_y])
                    if name == 'wheat':
                        self.block = plant.Plant(
                            i, name, 0, self.wheat_dead_image, self.wheat_image, rand_x, rand_y, False
                        )
                    if name == 'eggplant':
                        self.block = plant.Plant(
                            i, name, 1, self.eggplant_image, self.eggplant_image, rand_x, rand_y, False
                        )
                    if name == 'ivy':
                        self.block = plant.Plant(
                            i, name, 1, self.ivy_image, self.ivy_image, rand_x, rand_y, False
                            )
                    if name == 'flower':
                        self.block = plant.Plant(
                            i, name, 1, self.flower_image,  self.flower_image, rand_x, rand_y, False
                            )
                    if name == 'stone':
                        self.block = plant.Plant(
                            i, name, 1, self.stone_image, self.stone_image, rand_x, rand_y, False
                            )
                    if name == 'buch':
                        self.block = plant.Plant(
                            i, name, 1, self.bush_image, self.bush_image, rand_x, rand_y, False
                            )
                    if name == 'aim':
                        self.block = plant.Plant(
                            999, name, 1, self.aim_image, self.aim_image, rand_x, rand_y, False
                            )
                    field_list.append(self.block)
                    break

    def locate_aim(self, field_list, x, y):
        self.block = plant.Plant(
            999, 'aim', 1, self.aim_image, self.aim_image, x, y, False
            )
        field_list.append(self.block)

    def draw_plant(self, field_list):
        for obj in field_list:
            if obj.state == 0:
                self.surface.blit(obj.image_state_zero, (int(obj.xy[0] * self.cell_size), int(obj.xy[1] * self.cell_size)))
            if obj.state == 1:
                self.surface.blit(obj.image_state_one, (int(obj.xy[0] * self.cell_size), int(obj.xy[1] * self.cell_size)))

    def draw_aim(self, aim_list):
        x = int(aim_list[0].xy[0] * self.cell_size)
        y = int(aim_list[0].xy[1] * self.cell_size)
        self.surface.blit(self.aim_image, (x, y))  # rotate tractor