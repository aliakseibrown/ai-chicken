import random
import os
import pygame
from pygame.locals import *
from core.chicken import chicken as chick
from core.field import field_settings
from core.plants import plants_settings

from agent.neural_network import inference
#import agent.neural_network.inference
#import neural_network.inference
# import core.plants.plant as plant
# import core.plants.plants_settings as plants_settings
import agent.methods.graph_search as graph_search


#import models.field_block as field_block


class Game:
    cell_size = 50
    cell_number = 15  # horizontally
    blocks_number = 20
    dry_grass_number = 50
    wet_grass_number = (cell_number*cell_number) - dry_grass_number

    def __init__(self):
        # initialize a window
        pygame.init()
        self.surface = pygame.display.set_mode((self.cell_size*self.cell_number, self.cell_size*self.cell_number))

        self.grass_list = [] # 1-level
        self.plant_list = [] # 2-level
        self.stone_list = [] # 3-level
        self.aim_list = []   # 4-level

        self.Field = field_settings.FieldSettings(self.surface, self.cell_size, self.cell_number)
        self.Field.locate_field(self.grass_list, 0, self.wet_grass_number) # wet grass
        self.Field.locate_field(self.grass_list, 1, self.dry_grass_number) # dry grass

        self.Plants = plants_settings.PlantsSettings(self.surface, self.cell_size, self.cell_number)
        
        self.Plants.locate_plant(self.plant_list, 'wheat', self.blocks_number)
        self.Plants.locate_plant(self.plant_list, 'flower', self.blocks_number)
        self.Plants.locate_plant(self.plant_list, 'eggplant', self.blocks_number)

        self.Plants.locate_aim(self.aim_list, 0, 0)

        self.Plants.locate_plant(self.stone_list, 'stone', self.blocks_number)

        #self.image_wheat = self.Plants.wheat_watered()
        self.chicken = chick.Chicken(self.surface, self.cell_size, self.cell_number)
        self.chicken.draw()

    def run(self):
        running = True
        clock = pygame.time.Clock()
        move_chicken_event = pygame.USEREVENT + 1
        pygame.time.set_timer(move_chicken_event, 500)  # chicken moves every 1000 ms
        self.search_object = graph_search.Search(self.cell_size, self.cell_number)
        chicken_next_moves = []


        veggies = dict()
        veggies_debug = dict()

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
                        self.chicken.water(self.dead_leaf_body, self.green_leaf_body, self.cell_size)

                if event.type == move_chicken_event:
                    if len(chicken_next_moves) == 0:

                        angles = {0: 'UP', 90: 'RIGHT', 270: 'LEFT', 180: 'DOWN'}
                        closest_wheat = self.search_object.closest_point(self.chicken.x, self.chicken.y, 'wheat', self.plant_list)
                        self.aim_list[0].xy[0] = closest_wheat[0]
                        self.aim_list[0].xy[1] = closest_wheat[1]
                        chicken_next_moves = self.search_object.astarsearch(
                            [self.chicken.x, self.chicken.y, angles[self.chicken.angle]], [closest_wheat[0], closest_wheat[1]], self.stone_list, self.plant_list)
                        
                        #neural_network
                        current_veggie = next(os.walk('./agent/neural_network/images/test'))[1][random.randint(0, len(next(os.walk('./agent/neural_network/images/test'))[1])-1)]
                        if(current_veggie in veggies_debug):
                            veggies_debug[current_veggie]+=1
                        else:
                            veggies_debug[current_veggie] = 1

                        current_veggie_example = next(os.walk(f'./agent/neural_network/images/test/{current_veggie}'))[2][random.randint(0, len(next(os.walk(f'./agent/neural_network/images/test/{current_veggie}'))[2])-1)]
                        predicted_veggie = inference.main(f"./agent/neural_network/images/test/{current_veggie}/{current_veggie_example}")
                        if predicted_veggie in veggies:
                            veggies[predicted_veggie]+=1
                        else:
                            veggies[predicted_veggie] = 1
                        print("Debug veggies: ", veggies_debug, "Predicted veggies: ", veggies)
                    else:
                        self.chicken.move(chicken_next_moves.pop(0)[0])
                        if len(chicken_next_moves) == 0:
                            self.chicken.water([self.aim_list[0].xy[0], self.aim_list[0].xy[1]], self.plant_list)
                        print(self.chicken.x, self.chicken.y)

                elif event.type == QUIT:
                    running = False

                self.surface.fill((123, 56, 51))  # background color
                self.Field.draw_grass(self.grass_list)
                self.Plants.draw_plant(self.plant_list)
                self.Plants.draw_plant(self.stone_list)

                self.Plants.draw_aim(self.aim_list)

                self.chicken.draw()
                pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
