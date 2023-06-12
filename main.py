import os
import pygame
import random
import land
import tractor
import blocks
import astar_search
import neural_network.inference
from pygame.locals import *

examples = [
    ['piasek', 'sucha', 'jalowa', 'żółty'],
    ['czarnoziem', 'wilgotna', 'bogata', 'brazowa'],
    ['rzedzina', 'wilgotna', 'bogata', 'zielona'],
    ['gleby murszowe', 'wilgotna', 'bogata', 'szara'],
    ['pustynne gleby', 'sucha', 'jalowa', 'pomarańczowa'],
    ['torfowiska', 'sucha', 'jalowa', 'czerwona']
]

attributes = ['typ_gleby', 'wilgotność', 'zawartość_składników', 'kolor']

# Tworzenie obiektu TreeLearn i nauka drzewa decyzyjnego
# tree_learner = TreeLearn()
# default_class = 'nieznane'

# tree_learner.train(examples, attributes, default_class)

class TreeLearn:
    def __init__(self):
        self.tree = None
    
    def train(self, examples, attributes, default_class):
        self.tree = self.build_tree(examples, attributes, default_class)
    
    def build_tree(self, examples, attributes, default_class):
        if not examples:
            return Node(default_class)
        
        if self.all_same_class(examples):
            return Node(examples[0][-1])
        
        if not attributes:
            class_counts = self.get_class_counts(examples)
            default_class = max(class_counts, key=class_counts.get)
            return Node(default_class)
        
        best_attribute = self.choose_attribute(examples, attributes)
        root = Node(best_attribute)
        
        attribute_values = self.get_attribute_values(examples, best_attribute)
        
        for value in attribute_values:
            new_examples = self.filter_examples(examples, best_attribute, value)
            new_attributes = attributes[:]
            new_attributes.remove(best_attribute)
            new_default_class = max(self.get_class_counts(new_examples), key=lambda k: class_counts.get(k, 0))
            
            subtree = self.build_tree(new_examples, new_attributes, new_default_class)
            root.add_child(value, subtree)
        
        return root
    
    def all_same_class(self, examples):
        return len(set([example[-1] for example in examples])) == 1
    
    def get_class_counts(self, examples):
        class_counts = {}
        for example in examples:
            class_label = example[-1]
            class_counts[class_label] = class_counts.get(class_label, 0) + 1
        return class_counts
    
    def choose_attribute(self, examples, attributes):
        # Placeholder for attribute selection logic
        return attributes[0]
    
    def get_attribute_values(self, examples, attribute):
        return list(set([example[attribute] for example in examples]))
    
    def filter_examples(self, examples, attribute, value):
        return [example for example in examples if example[attribute] == value]


class Node:
    def __init__(self, label):
        self.label = label
        self.children = {}
    
    def add_child(self, value, child):
        self.children[value] = child


class Game:
    cell_size = 50
    cell_number = 15  # horizontally
    blocks_number = 20
    
    def __init__(self):

        self.dead_leaf_body = []
        self.green_leaf_body = []
        self.stone_body = []
        self.flower_body = []
        self.dead_grass_body = []
        self.grass_body = []
        self.red_block = [] #aim block

        self.fawn_seed_body = []
        self.fawn_wheat_body = []

        self.black_earth_body = []
        self.green_earth_body = []
        self.fawn_soil_body = []
        self.fen_soil_body = []
        self.allBodyPos = []

        self.entire_block = {}

        # initialize a window
        pygame.init()
        self.surface = pygame.display.set_mode((self.cell_size*self.cell_number, self.cell_size*self.cell_number))

        # finds places for every type soil and grass
        self.black_earth = land.Land(self.surface, self.cell_size, self.cell_number, self.allBodyPos, 100)
        self.black_earth.locate_soil(self.black_earth_body)
        self.green_earth = land.Land(self.surface, self.cell_size, self.cell_number, self.allBodyPos, 100)
        self.green_earth.locate_soil(self.green_earth_body)
        self.fawn_soil = land.Land(self.surface, self.cell_size, self.cell_number, self.allBodyPos, 100)
        self.fawn_soil.locate_soil(self.fawn_soil_body)
        self.fen_soil = land.Land(self.surface, self.cell_size, self.cell_number, self.allBodyPos, 100)
        self.fen_soil.locate_soil(self.fen_soil_body)
        self.grass = land.Land(self.surface, self.cell_size, self.cell_number, self.allBodyPos, 100)

        self.blocks = blocks.Blocks(self.surface, self.cell_size)
        self.blocks.locate_blocks(self.blocks_number, self.cell_number, self.dead_leaf_body)
        self.blocks.locate_blocks(self.blocks_number, self.cell_number, self.stone_body)
        self.blocks.locate_blocks(self.blocks_number, self.cell_number, self.flower_body)

        #self.blocks.locate_blocks(1, self.cell_number, self.red_block)

        # self.potato = blocks.Blocks(self.surface, self.cell_size)
        # self.potato.locate_soil('black earth', 6, 1, [])

        self.tractor = tractor.Tractor(self.surface, self.cell_size)
        self.tractor.draw()

    def run(self):
        # print(self.potato.get_soil_info().get_name())
        # print(self.potato.get_soil_info().get_acidity())
        # print(self.potato.get_soil_info().get_irrigation())
        running = True
        clock = pygame.time.Clock()

        move_tractor_event = pygame.USEREVENT + 1
        pygame.time.set_timer(move_tractor_event, 500)  # tractor moves every 1000 ms
        tractor_next_moves = []
        astar_search_object = astar_search.Search(self.cell_size, self.cell_number)

        veggies = dict()
        veggies_debug = dict()

        while running:
            clock.tick(60)  # manual fps control not to overwork the computer
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if pygame.key.get_pressed()[K_ESCAPE]:
                        running = False
                        # in case we want to use keyboard
                    if pygame.key.get_pressed()[K_UP]:
                        # self.tractor.move('up', self.cell_size, self.cell_number)
                        self.tractor.move('move', self.cell_size, self.cell_number)
                    # if pygame.key.get_pressed()[K_DOWN]:
                    #     self.tractor.move('down', self.cell_size, self.cell_number)
                    if pygame.key.get_pressed()[K_LEFT]:
                        self.tractor.move('left', self.cell_size, self.cell_number)
                    if pygame.key.get_pressed()[K_RIGHT]:
                        self.tractor.move('right', self.cell_size, self.cell_number)
                    if pygame.key.get_pressed()[K_SPACE]:
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
                        if self.red_block:
                            self.red_block.pop()
                        self.red_block.append([random_x/50, random_y/50])
                        # below line should be later moved into tractor.py
                        angles = {0: 'UP', 90: 'RIGHT', 270: 'LEFT', 180: 'DOWN'}
                        #bandaid to know about stones
                        tractor_next_moves = astar_search_object.astarsearch(
                            [self.tractor.x, self.tractor.y, angles[self.tractor.angle]], [random_x, random_y], self.stone_body, self.flower_body)
                        current_veggie = next(os.walk('./neural_network/images/test'))[1][random.randint(0, len(next(os.walk('./neural_network/images/test'))[1])-1)]
                        if(current_veggie in veggies_debug):
                            veggies_debug[current_veggie]+=1
                        else:
                            veggies_debug[current_veggie] = 1

                        current_veggie_example = next(os.walk(f'./neural_network/images/test/{current_veggie}'))[2][random.randint(0, len(next(os.walk(f'./neural_network/images/test/{current_veggie}'))[2])-1)]
                        predicted_veggie = neural_network.inference.main(f"./neural_network/images/test/{current_veggie}/{current_veggie_example}")
                        if predicted_veggie in veggies:
                            veggies[predicted_veggie]+=1
                        else:
                            veggies[predicted_veggie] = 1
                        print("Debug veggies: ", veggies_debug, "Predicted veggies: ", veggies)

                    else:
                        self.tractor.move(tractor_next_moves.pop(0)[0], self.cell_size, self.cell_number)
                elif event.type == QUIT:
                    running = False

                self.surface.fill((123, 56, 51))  # background color
                self.grass.set_and_place_block_of_grass('good')
                self.black_earth.place_soil(self.black_earth_body, 'black_earth')
                self.green_earth.place_soil(self.green_earth_body, 'green_earth')
                self.fawn_soil.place_soil(self.fawn_soil_body, 'fawn_soil')
                self.fen_soil.place_soil(self.fen_soil_body, 'fen_soil')

                # plants examples
                self.blocks.place_blocks(self.surface, self.cell_size, self.dead_leaf_body, 'leaf')
                self.blocks.place_blocks(self.surface, self.cell_size, self.green_leaf_body, 'alive')
                self.blocks.place_blocks(self.surface, self.cell_size, self.stone_body, 'stone')
                self.blocks.place_blocks(self.surface, self.cell_size, self.flower_body, 'flower')

                self.blocks.place_blocks(self.surface, self.cell_size, self.red_block, 'red')

                # seeds
                self.blocks.place_blocks(self.surface, self.cell_size, self.fawn_seed_body, 'fawn_seed')

                # wheat
                self.blocks.place_blocks(self.surface, self.cell_size, self.fawn_wheat_body, 'fawn_wheat')

                self.tractor.draw()
                pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
