import pygame
import random
from core.plants import plant
from core.constants import strings

constant = strings.ConStrings


class PlantsSettings:
    def __init__(self, surface, cell_size, cell_number):
        self.cell_number = cell_number
        self.cell_size = cell_size
        self.surface = surface 
        self.all_plants = []
        self.all_fruits = []
        #plants
        self.flower_image = pygame.image.load(constant.flower).convert_alpha()
        self.flower_image = pygame.transform.scale(self.flower_image, (self.cell_size, self.cell_size))
        self.bush_image = pygame.image.load(constant.bush).convert_alpha()
        self.bush_image = pygame.transform.scale(self.bush_image, (self.cell_size, self.cell_size))
        self.ivy_image = pygame.image.load(constant.ivy).convert_alpha()
        self.ivy_image = pygame.transform.scale(self.ivy_image, (self.cell_size, self.cell_size))
        self.wheat_dead_image = pygame.image.load(constant.wheat_dead).convert_alpha()
        self.wheat_dead_image = pygame.transform.scale(self.wheat_dead_image, (self.cell_size, self.cell_size))
        self.wheat_image = pygame.image.load(constant.wheat).convert_alpha()
        self.wheat_image = pygame.transform.scale(self.wheat_image, (self.cell_size, self.cell_size))
        #vegies
        self.eggplant_image = pygame.image.load(constant.eggplant).convert_alpha()
        self.eggplant_image = pygame.transform.scale(self.eggplant_image, (self.cell_size, self.cell_size))
        self.tomato_image = pygame.image.load(constant.tomato).convert_alpha()
        self.tomato_image = pygame.transform.scale(self.tomato_image, (self.cell_size, self.cell_size))
        self.carrot_image = pygame.image.load(constant.carrot).convert_alpha()
        self.carrot_image = pygame.transform.scale(self.carrot_image, (self.cell_size, self.cell_size))
        self.pumpkin_image = pygame.image.load(constant.pumpkin).convert_alpha()
        self.pumpkin_image = pygame.transform.scale(self.pumpkin_image, (self.cell_size, self.cell_size))
        self.papaya_image = pygame.image.load(constant.papaya).convert_alpha()
        self.papaya_image = pygame.transform.scale(self.papaya_image, (self.cell_size, self.cell_size))
        self.pepper_image = pygame.image.load(constant.pepper).convert_alpha()
        self.pepper_image = pygame.transform.scale(self.pepper_image, (self.cell_size, self.cell_size))
        #fruits
        self.strawberry_image = pygame.image.load(constant.strawberry).convert_alpha()
        self.strawberry_image = pygame.transform.scale(self.strawberry_image, (self.cell_size, self.cell_size))
        self.grapes_image = pygame.image.load(constant.grapes).convert_alpha()
        self.grapes_image = pygame.transform.scale(self.grapes_image, (self.cell_size-12, self.cell_size))
        self.apple_image = pygame.image.load(constant.apple).convert_alpha()
        self.apple_image = pygame.transform.scale(self.apple_image, (self.cell_size, self.cell_size))
        self.banana_image = pygame.image.load(constant.banana).convert_alpha()
        self.banana_image = pygame.transform.scale(self.banana_image, (self.cell_size, self.cell_size))

        self.stone_image = pygame.image.load(constant.stone).convert_alpha()
        self.stone_image = pygame.transform.scale(self.stone_image, (self.cell_size, self.cell_size))

        self.aim_image = pygame.image.load(constant.aim).convert_alpha()
        self.aim_image = pygame.transform.scale(self.aim_image, (self.cell_size, self.cell_size))

    def locate_plant(self, field_list, name, num_of_blocks):      # finds open space (coordinates)
        for i in range(num_of_blocks):
            while True:
                rand_x = random.randint(0, self.cell_number - 1)  # to check
                rand_y = random.randint(0, self.cell_number - 1)
                if [rand_x, rand_y] not in self.all_plants:
                    self.all_plants.append([rand_x, rand_y])
                    if name == 'wheat':
                        self.block = plant.Plant(
                            i, name, 0, self.wheat_dead_image, self.wheat_image, constant.wheat_dead, rand_x, rand_y, False
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

    def locate_fruit(self, field_list, name, num_of_blocks):      # finds open space (coordinates)
        for i in range(num_of_blocks):
            while True:
                rand_x = random.randint(0, self.cell_number - 1)  # to check
                rand_y = random.randint(0, self.cell_number - 1)
                if [rand_x, rand_y] not in self.all_fruits:
                    self.all_fruits.append([rand_x, rand_y])
                    if name == 'wheat':
                        self.block = plant.Plant(
                            i, name, 0, self.wheat_dead_image, self.wheat_image, constant.wheat_dead, rand_x, rand_y, False
                        )
                    if name == 'strawberry':
                        self.block = plant.Plant(
                            i, name, 1, self.strawberry_image, self.strawberry_image, constant.strawberry, rand_x, rand_y, False
                        )
                    if name == 'grapes':
                        self.block = plant.Plant(
                            i, name, 1, self.grapes_image, self.grapes_image,constant.grapes, rand_x, rand_y, False
                        )
                    if name == 'apple':
                        self.block = plant.Plant(
                            i, name, 1, self.apple_image, self.apple_image,constant.apple, rand_x, rand_y, False
                            )
                    if name == 'banana':
                        self.block = plant.Plant(
                            i, name, 1, self.banana_image,  self.banana_image,constant.banana, rand_x, rand_y, False
                            )
                    if name == 'stone':
                        self.block = plant.Plant(
                            i, name, 1, self.stone_image, self.stone_image, constant.stone, rand_x, rand_y, False
                            )
                    field_list.append(self.block)
                    break

    def locate_veggies(self, field_list, name, num_of_blocks):      # finds open space (coordinates)
        for i in range(num_of_blocks):
            while True:
                rand_x = random.randint(0, self.cell_number - 1)  # to check
                rand_y = random.randint(0, self.cell_number - 1)
                if [rand_x, rand_y] not in self.all_fruits:
                    self.all_fruits.append([rand_x, rand_y])
                    if name == 'wheat':
                        self.block = plant.Plant(
                            i, name, 0, self.wheat_dead_image, self.wheat_image, constant.wheat_dead, rand_x, rand_y, False
                        )
                    if name == 'pumpkin':
                        self.block = plant.Plant(
                            i, name, 1, self.pumpkin_image, self.pumpkin_image, constant.pumpkin, rand_x, rand_y, False
                        )
                    if name == 'pepper':
                        self.block = plant.Plant(
                            i, name, 1, self.pepper_image, self.pepper_image, constant.pepper, rand_x, rand_y, False
                        )
                    if name == 'papaya':
                        self.block = plant.Plant(
                            i, name, 1, self.papaya_image, self.papaya_image, constant.papaya, rand_x, rand_y, False
                        )
                    if name == 'carrot':
                        self.block = plant.Plant(
                            i, name, 1, self.carrot_image, self.carrot_image, constant.carrot, rand_x, rand_y, False
                        )
                    if name == 'tomato':
                        self.block = plant.Plant(
                            i, name, 1, self.tomato_image, self.tomato_image, constant.tomato, rand_x, rand_y, False
                            )
                    if name == 'stone':
                        self.block = plant.Plant(
                            i, name, 1, self.stone_image, self.stone_image, constant.stone, rand_x, rand_y, False
                            )
                    field_list.append(self.block)
                    break




    def locate_aim(self, field_list, x, y):
        self.block = plant.Plant(
            999, 'aim', 1, self.aim_image, self.aim_image, constant.aim, x, y, False
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