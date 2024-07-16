from MemoryButton import MemoryButton
from ManageDisplay import ManageDisplay
import pygame, numpy, math

class ManageGrid(ManageDisplay):

    def __init__(self, screen):
        super().__init__(screen)
        self.screen_lower_limit = min(self.screen_width, self.screen_height)
        self.screen_upper_limit = max(self.screen_width, self.screen_height)
        self.block_size = int(math.floor(self.screen_lower_limit/self.matrix_size))
        self.generate_grid(self.tile_number)
        self.generate_tiles()

    def generate_grid(self, tile_number):
        self.binary_grid = numpy.ones((self.matrix_size, self.matrix_size), dtype=int)
        while tile_number > 0:
            x = numpy.random.randint(0, self.matrix_size)
            y = numpy.random.randint(0, self.matrix_size)
            if self.binary_grid[x][y] == 1:
                self.binary_grid[x][y] = 0
                tile_number = tile_number - 1

    def generate_tiles(self) -> list:
        self.tile_list = []
        for x in range(int((self.screen_upper_limit-self.screen_lower_limit)/2), 
                        int(self.screen_upper_limit-((self.screen_upper_limit-self.screen_lower_limit)/2)), self.block_size):
            x_ind = int(x/self.block_size)
            for y in range(int((self.screen_upper_limit-self.screen_lower_limit)/2), 
                            int(self.screen_upper_limit-((self.screen_upper_limit-self.screen_lower_limit)/2)), self.block_size):
                y_ind = int(y/self.block_size)
                new_tile = MemoryButton(x + 5, y + 5, self.block_size - 10, self.block_size - 10, self.binary_grid[x_ind-1][y_ind-1])
                self.tile_list.append(new_tile)
        self.start_time = self.seconds

    def tile_selected(self):
        for tile in self.tile_list:
            mouse_presses = pygame.mouse.get_pressed()
            if tile.isPressed(self.screen) and mouse_presses[0] and tile.status == 0:
                tile.change_color(tile.navy)
                tile.change_status(2)
                self.correct = self.correct + 1
            elif tile.isPressed(self.screen) and mouse_presses[0] and tile.status == 1:
                tile.change_color(tile.red)
                tile.change_status(2)
                self.incorrect = self.incorrect + 1
        self.start_time1 = self.seconds

    def update_grid(self):
        self.tile_number = self.tile_number + 1
        self.advance_level()
        self.block_size = int(math.floor(self.screen_lower_limit/self.matrix_size))