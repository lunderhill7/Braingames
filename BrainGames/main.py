import pygame
from MemoryGrid import MemoryGrid
from Math import Math    
from StartMenu import StartMenu
from MathTransition import MathTransition
from ScoreTracker import ScoreTracker
from GridTransition import GridTransition
from ColorTransition import ColorTransition
from ColorMatch import ColorMatch
from CardTransition import CardTransition
from EndMenu import EndMenu
from MatchGame import MatchGame

from Timer import Timer

def main():
  width = 750
  height = 750
  screen = pygame.display.set_mode((width, height))
  game_state = 0
  score = ScoreTracker()
  
  #creating function from the timer class that can be used to control the timer
  timer = Timer() # adds fucntions such as timer.startTimer(), timer.getTime(), timer.endTimer()

  # playing will always be true but user can still close the window
  playing = True

  while playing == True:
   
    # runs the start menu is game_state == 0
    if game_state == 0:
      start_menu = StartMenu(screen)
      start_menu.run_game()
      game_state = 1

    # runs games if game_state == 1
    if game_state == 1:

      # MATH GAME
      math_transition = MathTransition(screen)
      math_1 = Math(screen, 1)
      math_2 = Math(screen, 2)
  
      math_transition.run_game()
      math_1.run_game()
      math_2.run_game()
     
      score.pullMathScore(math_1)
      score.pullMathScore(math_2)
        
      # MEMORY GRID GAME
      
      grid_transition = GridTransition(screen)
      memory_1 = MemoryGrid(screen)

      grid_transition.run_game()
      memory_1.run_game()

      score.pullMemoryScore(memory_1)

      # COLOR MATCHING GAME
      color_transition = ColorTransition(screen)
      color_transition.run_game()

      color = ColorMatch(1)
      color.mainloop()

      #color2 = ColorMatch(2)
      #color2.mainloop()

      #color3 = ColorMatch(3)
      #color3.mainloop()

      score.pullColorScore(color_transition)

      # CARD MATCHING GAME
      card_transition = CardTransition(screen)
      card_transition.run_game()

      #score.pullCardScore(card_transition)
      
      our_game = MatchGame
      our_game.Go()

      ScoreTracker.calcScore(score)
      ScoreTracker.storeScore(score)
      ScoreTracker.highscore(score)

      game_state = 2

    # runs the end menu if game_state == 2
    if game_state == 2:
      end_menu = EndMenu(screen, score)
      end_menu.run_game(score)
      game_state = 0

if __name__ == '__main__':
  main()
