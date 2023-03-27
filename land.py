import pygame
import random

class Land:
    def __init__(self, parent_screen, cell_size, cell_number, all_soil_body, irrigation):
        self.parent_screen = parent_screen
        self.cell_number = cell_number
        self.cell_size = cell_size
        self._irrigation = irrigation
        self.all_soil_body = all_soil_body

        self.grass_image = pygame.image.load(r'resources/grass.png').convert_alpha()
        self.grass_image = pygame.transform.scale(self.grass_image, (cell_size, cell_size))

        # self.bad_grass_image = pygame.image.load(r'resources/bad_grass.png').convert()
        # self.bad_grass_image = pygame.transform.scale(self.bad_grass_image, (cell_size, cell_size))

        self.black_earth_image = pygame.image.load(r'resources/grass.png').convert()
        self.black_earth_image = pygame.transform.scale(self.black_earth_image, (cell_size, cell_size))

        self.green_earth_image = pygame.image.load(r'resources/grass.png').convert()
        self.green_earth_image = pygame.transform.scale(self.green_earth_image, (cell_size, cell_size))

        self.fawn_soil_image = pygame.image.load(r'resources/fawn_soil.png').convert()
        self.fawn_soil_image = pygame.transform.scale(self.fawn_soil_image, (cell_size, cell_size))

        self.fen_soil_image = pygame.image.load(r'resources/grass.png').convert()
        self.fen_soil_image = pygame.transform.scale(self.fen_soil_image, (cell_size, cell_size))


    def locate_soil(self, soil_body):  # finds free places(coordinates) for soil and adds them to soil_body[]
        number_of_blocs_for_each_soil = 50

        if number_of_blocs_for_each_soil > (self.cell_number * self.cell_number) // 4:
            number_of_blocs_for_each_soil = (self.cell_number * self.cell_number) // 4
            print('Number of soil blocks exceeds the number of fields!')

        for i in range(number_of_blocs_for_each_soil):  # can't be more than: (cell_number * cell_number) // soil_types
            while True:
                rand_x = random.randint(0, self.cell_number - 1)  # to-check
                rand_y = random.randint(0, self.cell_number - 1)
                if [rand_x, rand_y] not in self.all_soil_body:
                    self.all_soil_body.append([rand_x, rand_y])
                    soil_body.append([rand_x, rand_y])
                    break

    def place_soil(self, soil_body, soil_name):
        for body in soil_body:
            x = int(body[0] * self.cell_size)
            y = int(body[1] * self.cell_size)
            if soil_name == 'black_earth':
                self.parent_screen.blit(self.black_earth_image, (x, y))
            if soil_name == 'green_earth':
                self.parent_screen.blit(self.green_earth_image, (x, y))
            if soil_name == 'fawn_soil':
                self.parent_screen.blit(self.fawn_soil_image, (x, y))
            if soil_name == 'fen_soil':
                self.parent_screen.blit(self.fen_soil_image, (x, y))

    def set_and_place_block_of_grass(self, name):
        for i in range(0, self.cell_number):
            for k in range(0, self.cell_number):
                if [k, i] not in self.all_soil_body:
                    x = int(k * self.cell_size)
                    y = int(i * self.cell_size)
                    if name == 'good':
                        self.parent_screen.blit(self.grass_image, (x, y))
                    if name == 'bad':
                        self.parent_screen.blit(self.bad_grass_image, (x, y))
