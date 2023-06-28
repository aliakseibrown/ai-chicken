import random
import os
import pygame
<<<<<<< HEAD
from pygame.locals import *
from core.chicken import chicken as chick
from core.field import field_settings
from core.plants import plants_settings
from agent.methods.genetic_algorithm import genetic_algorithm
from agent.methods import a_star

import numpy as np

from agent.neural_network import inference
#import agent.neural_network.inference
#import neural_network.inference
# import core.plants.plant as plant
# import core.plants.plants_settings as plants_settings


#import models.field_block as field_block
=======
import random
import land
import tractor
import blocks
import nn
import astar_search
from pygame.locals import *
import numpy as np
>>>>>>> main


class Game:
    cell_size = 50
    cell_number = 15  # horizontally
    blocks_number = 20
    dry_grass_number = 50
    wet_grass_number = (cell_number*cell_number) - dry_grass_number

    def __init__(self):
<<<<<<< HEAD
=======

        self.dead_leaf_body = []
        self.green_leaf_body = []
        self.stone_body = []
        self.flower_body = []
        self.dead_grass_body = []
        self.grass_body = []
        self.red_block = [] #aim block

        #self.one_body = []

        self.fawn_seed_body = []
        self.fawn_wheat_body = []

        self.black_earth_body = []
        self.green_earth_body = []
        self.fawn_soil_body = []
        self.fen_soil_body = []
        self.allBodyPos = []

        self.entire_block = {}

>>>>>>> main
        # initialize a window
        pygame.init()
        self.surface = pygame.display.set_mode((self.cell_size*self.cell_number, self.cell_size*self.cell_number))

        self.grass_list = [] # 1-level
        self.plant_list = [] # 2-level - test
        self.veggies_list = [] # 2-level - first model agent
        self.fruits_list = [] # 2-level - second model agent
        self.stone_list = [] # 3-level
        self.aim_list = []   # 4-level

        self.Field = field_settings.FieldSettings(self.surface, self.cell_size, self.cell_number)
        self.Field.locate_field(self.grass_list, 0, self.wet_grass_number) # wet grass
        self.Field.locate_field(self.grass_list, 1, self.dry_grass_number) # dry grass

        self.Plants = plants_settings.PlantsSettings(self.surface, self.cell_size, self.cell_number)
        
        #plant_list
        # self.Plants.locate_plant(self.plant_list, 'wheat', self.blocks_number)
        # self.Plants.locate_plant(self.plant_list, 'flower', self.blocks_number)
        # self.Plants.locate_plant(self.plant_list, 'bush', self.blocks_number)

        # #fruits_list
        # self.Plants.locate_fruit(self.fruits_list, 'apple', self.blocks_number-5)
        # self.Plants.locate_fruit(self.fruits_list, 'banana', self.blocks_number-5)
        # self.Plants.locate_fruit(self.fruits_list, 'strawberry', self.blocks_number-5)
        # self.Plants.locate_fruit(self.fruits_list, 'grapes', self.blocks_number-5)
        # self.Plants.locate_fruit(self.fruits_list, 'wheat', self.blocks_number)

<<<<<<< HEAD
        #vegies_list
        self.Plants.locate_veggies(self.veggies_list, 'pepper', self.blocks_number-5)
        self.Plants.locate_veggies(self.veggies_list, 'carrot', self.blocks_number-5)
        self.Plants.locate_veggies(self.veggies_list, 'papaya', self.blocks_number-5)
        self.Plants.locate_veggies(self.veggies_list, 'wheat', self.blocks_number)


        self.Plants.locate_aim(self.aim_list, 0, 0)

        self.Plants.locate_veggies(self.stone_list, 'stone', self.blocks_number)

        #self.image_wheat = self.Plants.wheat_watered()
        self.chicken = chick.Chicken(self.surface, self.cell_size, self.cell_number)
        self.chicken.draw()
=======
        #class_names = ['Pumpkin', 'Tomato', 'Carrot']

        self.neural_network = nn.NNModel("neural_network/save/second_model.pth")

        # self.pumpkin_batch = self.neural_network.input_image("resources/pampkin.png")
        # self.tomato_batch = self.neural_network.input_image("resources/tomato.png")
        # self.carrot_batch = self.neural_network.input_image("resources/carrot.png")
        

        self.tractor = tractor.Tractor(self.surface, self.cell_size)
        self.tractor.draw()
>>>>>>> main

    def run(self):
        running = True
        clock = pygame.time.Clock()
        move_chicken_event = pygame.USEREVENT + 1
        pygame.time.set_timer(move_chicken_event, 1000)  # chicken moves every 1000 ms
        self.search_object = a_star.Search(self.cell_size, self.cell_number)
        chicken_next_moves = []

        veggies = dict()
        veggies_debug = dict()

        wheat_list = [obj for obj in self.veggies_list if obj.name == "wheat" and obj.state == 0]

        new_list = [()]
        a = 1
        for obj in wheat_list:
            new_list.append ((obj.xy[0], obj.xy[1]))
        
        new_list[0] = (1, 1)
        best_path = genetic_algorithm(new_list)

        while running:
            clock.tick(60)  # manual fps control not to overwork the computer
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if pygame.key.get_pressed()[K_ESCAPE]:
                        running = False
                    if pygame.key.get_pressed()[K_UP]:
                        # self.chicken.move('up', self.cell_size, self.cell_number)
                        self.chicken.move('move', self.cell_size, self.cell_number)
                    # if pygame.key.get_pressed()[K_DOWN]:
                    #     self.chicken.move('down', self.cell_size, self.cell_number)
                    if pygame.key.get_pressed()[K_LEFT]:
                        self.chicken.move('left', self.cell_size, self.cell_number)
                    if pygame.key.get_pressed()[K_RIGHT]:
                        self.chicken.move('right', self.cell_size, self.cell_number)
                    if pygame.key.get_pressed()[K_SPACE]:
<<<<<<< HEAD
                        self.chicken.water(self.dead_leaf_body, self.green_leaf_body, self.cell_size)

                if event.type == move_chicken_event:
                    if len(chicken_next_moves) == 0:
=======
                        self.tractor.water(self.dead_leaf_body, self.green_leaf_body, self.cell_size)
                        # self.tractor.water(self.grass_body, self.dead_grass_body, self.cell_size)
                    if pygame.key.get_pressed()[K_q]:
                        self.tractor.harvest(self.fawn_seed_body, self.fawn_wheat_body, self.cell_size)
                        self.tractor.put_seed(self.fawn_soil_body, self.fawn_seed_body, self.cell_size)
                if event.type == move_tractor_event:
                    if len(tractor_next_moves) == 0:
                        random_x = random.randrange(0, self.cell_number * self.cell_size, 50)
                        random_y = random.randrange(0, self.cell_number * self.cell_size, 50)
                        print("Generated target: ",random_x, random_y)
                        #aim-blue block
                        if self.red_block:
                            self.red_block.pop()
                        self.red_block.append([random_x/50, random_y/50])

                        self.path_image = "resources/2.png"
                        self.aim_batch = self.neural_network.input_image(self.path_image)
                        self.predicate = self.neural_network.predicte(self.aim_batch)


                        # below line should be later moved into tractor.py
>>>>>>> main
                        angles = {0: 'UP', 90: 'RIGHT', 270: 'LEFT', 180: 'DOWN'}
                        closest_wheat = self.search_object.closest_point(self.chicken.x, self.chicken.y, 'wheat', self.veggies_list)
                        # self.aim_list[0].xy[0] = closest_wheat[0]
                        # self.aim_list[0].xy[1] = closest_wheat[1]
                        self.aim_list[0].xy[0] = best_path[a][0]
                        self.aim_list[0].xy[1] = best_path[a][1]
                        # a += 1
                        # target = wheat_list[a]
                        # chicken_next_moves = self.search_object.astarsearch(
                        #   [self.chicken.x, self.chicken.y, angles[self.chicken.angle]], [closest_wheat[0], closest_wheat[1]], self.stone_list, self.veggies_list)
                        
                        chicken_next_moves = self.search_object.astarsearch(
                          [self.chicken.x, self.chicken.y, angles[self.chicken.angle]], [best_path[a][0], best_path[a][1]], self.stone_list, self.veggies_list)

                        a += 1
                        # #neural_network
                        # current_veggie = next(os.walk('./agent/neural_network/images/test'))[1][random.randint(0, len(next(os.walk('./agent/neural_network/images/test'))[1])-1)]
                        # if(current_veggie in veggies_debug):
                        #     veggies_debug[current_veggie]+=1
                        # else:
                        #     veggies_debug[current_veggie] = 1

                        # current_veggie_example = next(os.walk(f'./agent/neural_network/images/test/{current_veggie}'))[2][random.randint(0, len(next(os.walk(f'./agent/neural_network/images/test/{current_veggie}'))[2])-1)]
                        # predicted_veggie = inference.main(f"./agent/neural_network/images/test/{current_veggie}/{current_veggie_example}")
                        # if predicted_veggie in veggies:
                        #     veggies[predicted_veggie]+=1
                        # else:
                        #     veggies[predicted_veggie] = 1
                        # print("Debug veggies: ", veggies_debug, "Predicted veggies: ", veggies)
                    else:
                        self.chicken.move(chicken_next_moves.pop(0)[0])
                        if len(chicken_next_moves) == 0:
                            self.chicken.water([self.aim_list[0].xy[0], self.aim_list[0].xy[1]], self.veggies_list)
                        print(self.chicken.x, self.chicken.y)
                    current_block = ''
                    for obj in self.veggies_list:
                        if obj.xy == [self.chicken.x, self.chicken.y]:
                            if obj.name != 'wheat':
                                current_block = obj.image_path
                    if current_block == '':
                        print('the block is empty')
                    else:
                        veggies_images = inference.main(current_block)
                        print('Current veggie: ',veggies_images)
                elif event.type == QUIT:
                    running = False

                self.surface.fill((123, 56, 51))  # background color
                self.Field.draw_grass(self.grass_list)
                #self.Plants.draw_plant(self.plant_list)
                #self.Plants.draw_plant(self.fruits_list)
                self.Plants.draw_plant(self.stone_list)
                self.Plants.draw_plant(self.veggies_list)

                self.Plants.draw_aim(self.aim_list)

                self.chicken.draw()
                pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
