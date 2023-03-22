import pygame
import random
import tractor
import blocks
from pygame.locals import *
from datetime import datetime


class Game:
    cell_size = 50
    cell_number = 15        #horizontally 
    blocks_number = 15
    
    def __init__(self):
        self.dead_leaf_body = []
        self.green_leaf_body = []
        self.stone_body = []
        self.flower_body = []
        
    
        self.entire_block = {}

        pygame.init()
        self.surface = pygame.display.set_mode((self.cell_size*self.cell_number, self.cell_size*self.cell_number))  # initialize a window

        self.grass_image = pygame.image.load(r'resources/grass.png').convert()
        self.grass_image = pygame.transform.scale(self.grass_image, (self.cell_size, self.cell_size))

        self.bad_grass_image = pygame.image.load(r'resources/bad_grass.png').convert()
        self.bad_grass_image = pygame.transform.scale(self.bad_grass_image, (self.cell_size, self.cell_size))

        self.blocks = blocks.Blocks(self.surface,self.cell_size)

        self.blocks.locate_blocks(self.blocks_number, self.cell_number, self.dead_leaf_body)
        self.blocks.locate_blocks(self.blocks_number, self.cell_number, self.stone_body)
        self.blocks.locate_blocks(self.blocks_number, self.cell_number, self.flower_body)

        self.tractor = tractor.Tractor(self.surface, self.cell_size)
        self.tractor.draw()

    def run(self):
        running = True
        clock = pygame.time.Clock()
        last_time = datetime.now()

        while running:
            clock.tick(60)  # manual fps control not to overwork the computer
            time_now = datetime.now()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if pygame.key.get_pressed()[K_ESCAPE]:
                        running = False
                        # in case we want to use keyboard
                    if pygame.key.get_pressed()[K_UP]:
                        self.tractor.move('up',self.cell_size, self.cell_number)
                    if pygame.key.get_pressed()[K_DOWN]:
                        self.tractor.move('down',self.cell_size, self.cell_number)
                    if pygame.key.get_pressed()[K_LEFT]:
                        self.tractor.move('left',self.cell_size, self.cell_number)
                    if pygame.key.get_pressed()[K_RIGHT]:
                        self.tractor.move('right',self.cell_size, self.cell_number)
                    if pygame.key.get_pressed()[K_SPACE]:
                        self.tractor.water(self.dead_leaf_body, self.green_leaf_body, self.cell_size) 
                elif event.type == QUIT:
                    running = False

                self.surface.fill((140, 203, 97))  # background color

                for i in range(0, self.cell_number):
                    for k in range(0, self.cell_number):
                        x = int(i * self.cell_size)
                        y = int(k * self.cell_size)
                        self.surface.blit(self.grass_image, (x, y))
                

                self.blocks.place_blocks(self.surface, self.cell_size, self.dead_leaf_body, 'leaf')
                self.blocks.place_blocks(self.surface, self.cell_size, self.green_leaf_body, 'alive')
                self.blocks.place_blocks(self.surface, self.cell_size, self.stone_body, 'stone')
                self.blocks.place_blocks(self.surface, self.cell_size, self.flower_body, 'flower')


                self.tractor.draw()
                pygame.display.update()
           

            # if (time_now - last_time).total_seconds() > 1:                                # tractor moves every 1 sec
                #last_time = datetime.now()
                #self.tractor.walk()
                #print(f'x, y = ({int(self.tractor.x / 50)}, {int(self.tractor.y / 50)})')


if __name__ == '__main__':
    game = Game()
    game.run()
