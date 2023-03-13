import pygame
import random
from pygame.locals import *
from datetime import datetime

#main variables
class Configurations:
    cell_size = 50
    screen_size = 500
   # def _init_(self): 
        
class Lines:
    def __init__(self, parent_scr):
        self.parent_scr = parent_scr
        

    def draw_lines(self):  # background lines
        conf = Configurations()
        for i in range(1, 10):
            pygame.draw.line(self.parent_scr, (228, 253, 227), (conf.cell_size * i, 0), (conf.cell_size * i, conf.screen_size), 1)
            pygame.draw.line(self.parent_scr, (228, 253, 227), (0, conf.cell_size * i), (conf.screen_size, conf.cell_size * i), 1)
        pygame.display.flip()


class Tractor:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load(r'resources/arrow.png').convert()
        self.x = 100
        self.y = 100
        self.angle = 0
        self.direction = 'up'

    def draw(self):
        #self.parent_screen.fill((120, 120, 0))  # background color
        self.parent_screen.blit(self.block, (self.x, self.y))
        self.parent_screen.blit(pygame.transform.rotate(self.block, self.angle), (self.x, self.y))  # rotate tractor
        pygame.display.flip()  # updating screen

    def move(self, direction):
        conf = Configurations()
        if direction == 'up':
            self.y -= conf.cell_size
            self.angle = 0
        if direction == 'down':
            self.y += conf.cell_size
            self.angle = 180
        if direction == 'left':
            self.x -= conf.cell_size
            self.angle = 90
        if direction == 'right':
            self.x += conf.cell_size
            self.angle = 270
        #self.draw()

    def walk(self):
        choice = ['up', 'down', 'left', 'right']

        if self.x == 450:
            choice.pop(3)
        if self.x == 0:
            choice.pop(2)
        if self.y == 0:
            choice.pop(0)
        if self.y == 450:
            choice.pop(1)

        self.direction = random.choice(choice)
        self.move(self.direction)


class Field:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load(r'resources/field.png').convert()

    def place_field(self, field_matrix):
        conf = Configurations()
        for m, posY in enumerate(field_matrix):
            for n, posX in enumerate(posY):
                if field_matrix[m][n] == 1:
                    self.parent_screen.blit(self.block, (n * conf.cell_size, m * conf.cell_size))

        pygame.display.flip()


class Game:
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
        self.conf = Configurations()
        # self.screenWidth = 500
        # self.screenHeight = 500
        self.surface = pygame.display.set_mode((self.conf.screen_size, self.conf.screen_size))  # initialize a window
        # self.surface.fill((255, 255, 255))  # background color (overwritten by tractor)

        

        self.lines = Lines(self.surface)
        self.field = Field(self.surface)
        self.field.place_field(self.field_matrix)

        self.tractor = Tractor(self.surface)
        self.tractor.draw()

    def run(self):
        running = True
        clock = pygame.time.Clock()
        last_time = datetime.now()
        #self.lines.draw_lines()

        while running:
            clock.tick(60)  # manual fps control not to overwork the computer
            time_now = datetime.now()

            

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if pygame.key.get_pressed()[K_ESCAPE]:
                        running = False
                        # in case we want to use keyboard
                    if pygame.key.get_pressed()[K_UP]:
                        self.tractor.move('up')
                    if pygame.key.get_pressed()[K_DOWN]:
                        self.tractor.move('down')
                    if pygame.key.get_pressed()[K_LEFT]:
                        self.tractor.move('left')
                    if pygame.key.get_pressed()[K_RIGHT]:
                        self.tractor.move('right')
                elif event.type == QUIT:
                    running = False

                self.surface.fill((120, 120, 0))  # background color
                self.field.place_field(self.field_matrix)
                self.lines.draw_lines()
                self.tractor.draw()
           

            if (time_now - last_time).total_seconds() > 1:  # tractor moves every 1 sec
                last_time = datetime.now()
                #self.tractor.walk()
                #print(f'x, y = ({int(self.tractor.x / 50)}, {int(self.tractor.y / 50)})')


if __name__ == '__main__':
    game = Game()
    game.run()
