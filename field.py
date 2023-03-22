import pygame

class Field:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load(r'resources/field.png').convert()
    #def draw_blocks():

    def place_field(self, field_matrix, parent_screen, cell_size): #drawing blocks
        for m, posY in enumerate(field_matrix):
            for n, posX in enumerate(posY):
                if field_matrix[m][n] == 1:
                    self.parent_screen.blit(self.block, (n * cell_size, m * cell_size))

    def draw_lines(self, parent_screen, cell_size):  # background lines
        for i in range(1, 10):
            pygame.draw.line(self.parent_screen, (228, 253, 227), (cell_size * i, 0), (cell_size * i, parent_screen), 1)
            pygame.draw.line(self.parent_screen, (228, 253, 227), (0, cell_size * i), (parent_screen, cell_size * i), 1)
