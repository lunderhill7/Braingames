from MemoryButton import MemoryButton
from ManageGame import ManageGame
import pygame, numpy, math

class GenerateGrid(ManageGame):

    def __init__(self, screen): # , screen_width, screen_height):
        super().__init__()

        self.screen = screen
        self.screen_width = pygame.display.get_window_size()[0]
        self.screen_height = pygame.display.get_window_size()[1]

        # self.screen_width_center = self.screen_width/2
        # self.screen_height_center = self.screen_height/2

        self.block_size = int(math.floor(self.screen_width/self.matrix_size))

        self.correct = 0
        self.incorrect = 0
        self.fail_count = 0

        self.score = 0
        self.num_correct = 0
        self.problems_done = 0

        self.timer = pygame.USEREVENT
        pygame.time.set_timer(self.timer, 1000)

        self.seconds = 0
        self.start_time = 0

        self.pause = True
        self.advance = False
        self.not_advance = False

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
        for x in range(0, self.screen_width, self.block_size):
            x_ind = int(x/self.block_size)
            for y in range(0, self.screen_height, self.block_size):
                y_ind = int(y/self.block_size)
                new_tile = MemoryButton(x + 5, y + 5, self.block_size - 10, self.block_size - 10, self.binary_grid[x_ind-1][y_ind-1])
                self.tile_list.append(new_tile)
        self.start_time = self.seconds

    def tile_selected(self):
        for tile in self.tile_list:
            mouse_presses = pygame.mouse.get_pressed()
            if tile.isPressed(self.screen) and mouse_presses[0] and tile.status == 0:
                tile.change_color(tile.black)
                tile.change_status(2)
                self.correct = self.correct + 1
            elif tile.isPressed(self.screen) and mouse_presses[0] and tile.status == 1:
                tile.change_color(tile.red)
                tile.change_status(2)
                self.incorrect = self.incorrect + 1
        self.start_time1 = self.seconds


    def display_tiles(self):
        if self.seconds - self.start_time < 5:
            self.puase = False

            if self.level == 1:
                self.generate_messages(4)
            if self.level == 2:
                self.generate_messages(5)
            if self.level == 3:
                self.generate_messages(6)

            if self.advance:
                self.generate_messages(0)
            elif self.not_advance:
                self.generate_messages(1)

            self.generate_messages(2)
            self.generate_messages(3)

        elif (self.seconds - self.start_time) >= 5 and (self.seconds - self.start_time) < 8:
            self.pause = False
            for tile in self.tile_list:
                tile.draw_tile_temp(self.screen)
            self.advance = False
            self.not_advance = False
        else:
            self.pause = True
            for tile in self.tile_list:
                tile.draw_tile(self.screen)

    def update_grid(self):
        self.tile_number = self.tile_number + 1
        self.advance_level()
        self.block_size = int(math.floor(self.screen_width/self.matrix_size))

    def check_correct(self) -> bool:

        self.num_correct += self.correct
        self.problems_done += self.tile_number

        if self.correct + self.incorrect >= self.tile_number:
            self.pause = False
            if self.seconds - self.start_time1 > 0:
                if self.correct == self.tile_number and self.incorrect == 0:
                    self.correct = 0
                    self.incorrect = 0

                    self.update_grid()
                    self.generate_grid(self.tile_number)
                    self.generate_tiles()

                    self.advance = True
                elif self.incorrect > 0:
                    self.correct = 0
                    self.incorrect = 0

                    self.generate_grid(self.tile_number)
                    self.generate_tiles()

                    self.not_advance = True
                    self.fail_count = self.fail_count + 1