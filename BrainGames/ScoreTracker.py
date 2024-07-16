from datetime import date
import pygame.gfxdraw
from Math import Math
from MemoryGrid import MemoryGrid
from ColorMatch import ColorMatch

pygame.init()


class ScoreTracker:
    """Takes the score from all the games, averages them,
    and then stores them into a text file"""

    def __init__(self):
        self.math = 0
        self.card = 0
        self.color = 0
        self.memory = 0
        self.high = 0
        self.score = 0

    def pullMathScore(self, game):
        """pulls the score from the games to be added to the final score
        
        :param self the score of the specified game
        :returns the score pulled from the game
        """

        self.math = int(Math.giveScore(game))

    def pullMemoryScore(self, game):
        """pulls the score from the games to be added to the final score
        
        :param self the score of the specified game
        :returns the score pulled from the game
        """

        self.memory = int(MemoryGrid.give_score(game))

    def pullColorScore(self, game):
        """pulls the score from the games to be added to the final score
        
        :param self the score of the specified game
        :returns the score pulled from the game
        """

        self.color = int(ColorMatch.giveScore(game))

    def pullCardScore(self, game):
        """pulls the score from the games to be added to the final score
        
        :param self the score of the specified game
        :returns the score pulled from the game
        """

        #self.card = int(MemoryGrid.giveScore(game))

    def calcScore(self):
        """calculate the average score among the four games

        :param self the score added up
        :returns an average of all the games
        """

        self.score = self.math + self.memory + self.color + self.card
        self.score /= 4
        return self.score
    
    def highscore(self):
        """pulls highscore from the text document to be presented on final screen
        
        :param none
        :returns the highscore"""  

        with open('allScores.txt') as f:
            score_list = f.readlines()
        self.high = max(score_list)
        self.high = float(self.high)

    def giveScores(self):
        """gives all the score data to the final screen to be presented
        
        :param nothing i think
        :returns all the scores"""

        return self.score, self.high

    def storeScore(self):
        """stores the score within a text document as if it is a database
        
        :param self the averaged score from all the games
        :returns a line to be added to a text document storing the date and score"""

        today = date.today()
        line = ['\n', 'Date: ', str(today), ', Score: ', str(self.score)]
        line2 = ['\n' , str(self.score)]
        with open('userData.txt', 'a') as f:
            f.writelines(line)

        with open('allScores.txt', 'a') as f:
            f.writelines(line2)

