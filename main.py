import pygame
import random
import tractor
import field
from pygame.locals import *
from datetime import datetime


class Game:
    cell_size = 50
    screen_size = 500

    field_matrix = [[0 for m in range(10)] for n in range(10)]
    for i in range(10):
        while True:
            field_posX = random.randint(0, 9)
            field_posY = random.randint(0, 9)

            if field_matrix[field_posY][field_posX] == 0:
                field_matrix[field_posY][field_posX] = 1
                break

    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((self.screen_size, self.screen_size))  # initialize a window


        self.field = field.Field(self.surface)
        self.field.place_field(self.field_matrix, self.surface, self.cell_size)

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
                self.field.place_field(self.field_matrix, self.surface, self.cell_size)

                self.field.draw_lines(self.screen_size, self.cell_size)
                self.tractor.draw()
                pygame.display.update()
           

            # if (time_now - last_time).total_seconds() > 1:                                # tractor moves every 1 sec
                #last_time = datetime.now()
                #self.tractor.walk()
                #print(f'x, y = ({int(self.tractor.x / 50)}, {int(self.tractor.y / 50)})')


if __name__ == '__main__':
    game = Game()
    game.run()
