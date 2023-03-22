import pygame
import random
import tractor
import field
import blocks
from pygame.locals import *
from datetime import datetime


class Game:
    cell_size = 50
    cell_number = 15
    blocks_number = 15
    block_dict = {}

    def __init__(self):
        self.leaf_body = []
        self.vege_body = []
        self.carrot_body = []
    
        pygame.init()
        self.surface = pygame.display.set_mode((self.cell_size*self.cell_number, self.cell_size*self.cell_number))  # initialize a window

        self.grass_image = pygame.image.load(r'resources/grass3.png').convert()
        self.grass_image = pygame.transform.scale(self.grass_image, (self.cell_size, self.cell_size))

        self.blocks = blocks.Blocks(self.surface,self.cell_size)
        self.blocks.locate_blocks(self.blocks_number, self.cell_number, self.leaf_body)
        self.blocks.locate_blocks(self.blocks_number, self.cell_number, self.vege_body)
        self.blocks.locate_blocks(self.blocks_number, self.cell_number, self.carrot_body)


        self.blocks.place_blocks(self.surface, self.cell_size, self.leaf_body, 'leaf')
        self.blocks.place_blocks(self.surface, self.cell_size, self.vege_body, 'vege')
        self.blocks.place_blocks(self.surface, self.cell_size, self.carrot_body, 'carrot')

        for i in range(0, self.cell_number*self.cell_number):
            x = int(i * self.cell_size)
            y = int(i * self.cell_size)
            self.surface.blit(self.grass_image, (x, y))

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
                        self.tractor.move('up',self.cell_size)
                    if pygame.key.get_pressed()[K_DOWN]:
                        self.tractor.move('down',self.cell_size)
                    if pygame.key.get_pressed()[K_LEFT]:
                        self.tractor.move('left',self.cell_size)
                    if pygame.key.get_pressed()[K_RIGHT]:
                        self.tractor.move('right',self.cell_size)
                elif event.type == QUIT:
                    running = False

                self.surface.fill((140, 203, 97))  # background color

                for i in range(0, self.cell_number):
                    for k in range(0, self.cell_number):
                        x = int(i * self.cell_size)
                        y = int(k * self.cell_size)
                        self.surface.blit(self.grass_image, (x, y))
                

                #self.blocks.draw_lines(self.cell_number*self.cell_size, self.cell_size)

                self.blocks.place_blocks(self.surface, self.cell_size, self.leaf_body, 'leaf')
                self.blocks.place_blocks(self.surface, self.cell_size, self.vege_body, 'vege')
                self.blocks.place_blocks(self.surface, self.cell_size, self.carrot_body, 'carrot')


                self.tractor.draw()
                pygame.display.update()
           

            # if (time_now - last_time).total_seconds() > 1:                                # tractor moves every 1 sec
                #last_time = datetime.now()
                #self.tractor.walk()
                #print(f'x, y = ({int(self.tractor.x / 50)}, {int(self.tractor.y / 50)})')


if __name__ == '__main__':
    game = Game()
    game.run()
