from ManageGrid import ManageGrid
import pygame

class MemoryGrid(ManageGrid):

    def __init__(self, screen):
        self.level = 1
        self.update_level()

        super().__init__(screen)

        self.correct = 0
        self.incorrect = 0
        self.fail_count = 0

        self.advance = False
        self.not_advance = False
        self.pause = True

    def update_level(self):
        if self.level == 1:
            self.tile_number = 6
            self.matrix_size = 5
            self.fail_count = 0
        elif self.level == 2:
            self.tile_number = 10
            self.matrix_size = 6
            self.fail_count = 0
        elif self.level == 3:
            self.tile_number = 14
            self.matrix_size = 7
            self.fail_count = 0

    def advance_level(self):
        if self.tile_number == 10:
            self.level = 2
            self.update_level()
        elif self.tile_number == 14:
            self.level = 3
            self.update_level()

    def check_correct(self) -> bool:
        if self.correct + self.incorrect >= self.tile_number:
            for tile in self.tile_list:
                if tile.status == 1:
                    tile.change_color(self.gray)
                if tile.status == 0:
                    tile.change_color(self.navy)
                self.display_tiles()
            self.pause = False
            if self.seconds - self.start_time1 > 2:
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

    def update_score(self):
        self.score = (self.tile_number * 5.5) + 1

    def give_score(self):
        return self.score