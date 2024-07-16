import pygame, sys
pygame.init()

class ManageDisplay():

    def __init__(self, screen):

        self.screen = screen
        self.seconds = 0
        self.game_over = False

        self.screen_width = pygame.display.get_window_size()[0]
        self.screen_height = pygame.display.get_window_size()[1]

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (209, 68, 21)
        self.gray = (113, 113, 113)
        self.navy = (19, 21, 77)
        self.teal = (44, 135, 158)
        self.cream = (230, 216, 156)
        self.dark_gray = (40, 41, 46)
        self.tan = (176, 171, 120)
        self.green = (24, 112, 61)

        self.timer = pygame.USEREVENT
        pygame.time.set_timer(self.timer, 1000)
        pygame.display.set_caption("MemoryGrid")

    def run_game(self):
        while self.end_game():
            self.start_game()

    def start_game(self):
        self.screen.fill(self.teal)
        self.process_user_input()
        self.display_tiles()
        self.display_score()
        self.check_correct()
        pygame.display.flip()

    def end_game(self):
        if self.tile_number > 18 or self.fail_count > 2:
            self.game_over = True
            self.update_score()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return False
                if event.type == pygame.QUIT: 
                    pygame.quit()                    
                    sys.exit()
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

    def generate_messages(self, msg_number):
        if msg_number == 0:
            message_font = pygame.font.SysFont('helvetica', int((40/700)*self.screen_width), bold=True)
            message = message_font.render("Good Job,", True, self.green)
            self.screen.blit(message, ((255/700)*self.screen_width, (260/700)*self.screen_height))
        elif msg_number == 1:
            message_font = pygame.font.SysFont('helvetica', int((40/700)*self.screen_width), bold=True)
            message = message_font.render("Try Again,", True, self.red)
            self.screen.blit(message, ((255/700)*self.screen_width, (260/700)*self.screen_height))
        elif msg_number == 2:
            message_font = pygame.font.SysFont('helvetica', int((40/700)*self.screen_width))
            message = message_font.render("Get Ready For " + str(self.tile_number) + " Tiles!", True, self.dark_gray)
            self.screen.blit(message, ((150/700)*self.screen_width, (330/700)*self.screen_height))
        elif msg_number == 3:
            message_font = pygame.font.SysFont('helvetica', int((80/700)*self.screen_width))
            message = message_font.render(str(5 - ((self.seconds - self.start_time))), True, self.dark_gray)
            self.screen.blit(message, ((320/700)*self.screen_width, (440/700)*self.screen_height))
        elif msg_number == 4:
            message_font = pygame.font.SysFont('helvetica', int((70/700)*self.screen_width), bold=True)
            message = message_font.render("Level 1", True, self.dark_gray)
            self.screen.blit(message, ((235/700)*self.screen_width, (150/700)*self.screen_height))
        elif msg_number == 5:
            message_font = pygame.font.SysFont('helvetica', int((70/700)*self.screen_width), bold=True)
            message = message_font.render("Level 2", True, self.dark_gray)
            self.screen.blit(message, ((235/700)*self.screen_width, (150/700)*self.screen_height))
        elif msg_number == 6:
            message_font = pygame.font.SysFont('helvetica', int((70/700)*self.screen_width), bold=True)
            message = message_font.render("Level 3", True, self.dark_gray)
            self.screen.blit(message, ((235/700)*self.screen_width, (150/700)*self.screen_height))
        elif msg_number == 7:
            message_font = pygame.font.SysFont('helvetica', int((70/700)*self.screen_width), bold=True)
            message = message_font.render(str(self.score), True, self.red)
            self.screen.blit(message, ((280/700)*self.screen_width, (440/700)*self.screen_height))
        elif msg_number == 8:
            message_font = pygame.font.SysFont('helvetica', int((70/700)*self.screen_width), bold=True)
            message = message_font.render("Game Over!", True, self.dark_gray)
            self.screen.blit(message, ((150/700)*self.screen_width, (150/700)*self.screen_height))
        elif msg_number == 9:
            message_font = pygame.font.SysFont('helvetica', int((50/700)*self.screen_width))
            message = message_font.render("Your Score", True, self.dark_gray)
            self.screen.blit(message, ((220/700)*self.screen_width, (350/700)*self.screen_height))
    
    def display_tiles(self):
        if not self.game_over:
            if self.seconds - self.start_time < 5:
                self.puase = False

                rect = pygame.Rect(((50/750)*self.screen_width), ((50/750)*self.screen_height), 
                                ((650/750)*self.screen_width), ((650/750)*self.screen_height))
                pygame.gfxdraw.box(self.screen, rect, self.cream)
                pygame.draw.rect(self.screen, self.tan, rect, 5)

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

    def display_score(self):
        if self.game_over:
            # if self.seconds - self.start_time2 < 5:
                rect = pygame.Rect(((50/750)*self.screen_width), ((50/750)*self.screen_height), 
                                ((650/750)*self.screen_width), ((650/750)*self.screen_height))
                pygame.gfxdraw.box(self.screen, rect, self.cream)
                pygame.draw.rect(self.screen, self.tan, rect, 5)

                self.generate_messages(7)
                self.generate_messages(8)
                self.generate_messages(9)