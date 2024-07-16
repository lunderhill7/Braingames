import pygame, sys
pygame.init()

class ManageGame():

    def __init__(self):

        # self.screen = pygame.display.set_mode((700, 700)) # screen

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (225, 0, 0)
        self.gray = (113, 113, 113)

    # def main(self):
    #     while self.end_game():
    #         self.start_game()

    def run_game(self):
        while self.end_game():
            self.start_game()

    def start_game(self):
        self.screen.fill(self.white)
        self.process_user_input()
        self.display_tiles()
        self.check_correct()
        pygame.display.flip()

    def end_game(self):
        if self.tile_number > 18 or self.fail_count > 2:
            return False
        else:
            return True

    def process_user_input(self):
        for event in pygame.event.get():
            if event.type == self.timer:
                self.seconds = self.seconds + 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.pause:
                    self.tile_selected()
                    self.display_tiles()
            if event.type == pygame.QUIT: 
                pygame.quit()                    
                sys.exit()