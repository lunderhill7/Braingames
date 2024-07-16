"""
   This is a class which presents an interface for the ColorMatch game
   author: Noah Nicoletti

"""

# import the modules
import tkinter
import random
import pygame

pygame.init()

"""GLOBAL VARIABLES"""

# Initialize score to 0
score = 0

# list to hold our cases (1 = true and 0 = false)
true_case = [1,0] 

# the game time left, initially 30 seconds.
timeleft = 30

# 5 seconds until the next phase of the game.
nextlevel = 6

"""
        A class which represents a true case in our colormatch game where we have to
        create an algorithm for a true color match case.
"""
class TrueCase:
       """
                Constructor method which takes as an argument a list of strings (colors)
                param colours : list
       """
       def __init__(self, colours : list):

               self.colours = colours
               self.base_color = self.colours[0]

"""
        A class which represents a false case in our colormatch game where we have to
        create an algorithm for a false color match case.
"""
class FalseCase:
        """
                Constructor method which takes as an argument a list of strings (colors)
                param colours : list 
        """
        def __init__(self, colours : list):

                self.colours = colours
                self.base_color = self.colours[0]
                self.base_color2 = self.colours[1]

class ColorMatch(tkinter.Tk):


        """
                Constructor method hich takes as an argument a level of type int
                param level : int
        """
        def __init__(self, level : int):
                '''DRIVER CODE'''

                super().__init__()

                # self.level = level
                self.level = level
                
                # self.master = master
                self.title("Color Match Level " + str(level))
                
                self.geometry("750x750")

                # add an instructions label  ----IMPORTANT TO NOTE I changed root to self for labels and whatnot----
                self.instructions = tkinter.Label(self, text = "Does the meaning of the top word\n"
                                                        " match the text color of the bottom word?\n(type 't' for true or 'f' for false)",
                                                                                font = ('Helvetica', 16))
                self.instructions.pack()

                # add a score label
                self.scoreLabel = tkinter.Label(self, text = "press 'Enter' to start",
                                                                                       font = ('Helvetica', 12))
                self.scoreLabel.pack()

                # add a time left label
                self.timeLabel = tkinter.Label(self, text = "Time left: " +
                                       str(timeleft), font = ('Helvetica', 12))
                                               
                self.timeLabel.pack()

                # add a label for displaying the colours
               
                self.label = tkinter.Label(self, font = ('Helvetica', 55))
                self.label.pack()

                # add a label for displaying the colours
         
                self.label2 = tkinter.Label(self, font = ('Helvetica', 55))
                self.label2.pack()

                # add a text entry box for
                # typing in colours
                self.e = tkinter.Entry(self, font=('Arial 25'))

                
                self.e.pack()

                # set focus on the entry box
                self.e.focus_set()


                '''practice code to change colors list'''
                # level 1 will contain four basic colors
                if(level == 1):
                       self.colours = ['red', 'blue', 'green', 'yellow']
                       

                # level 2 will contain all colors of the rainbow        
                elif (level == 2):
                        self.colours = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

                # level 3 will contain all the unambiguous colors
                elif (level == 3):
                        self.colours = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'black', 'brown', 'white']

                
                self.bind('<Return>', self.startGame)
                # self.startGame()
                


        """
           Function to choose and display the next colors
        """
        def nextColour(self):

                # use the globally declared 'score'
                # and 'play' variables above.
                global score
                global timeleft
                global nextlevel


                # Here I present an empty color tuple
                #  color_tuple = ( [random.choice(colours) , random.choice(colours)], [random.choice(colours), random.choice(colours)] )
                # base_color = random.choice(colours)
         
                # if a game is currently in play
                if timeleft > 0:

                        # make the text entry box active.
                        self.e.focus_set()


                        if(true_case[0] == 1 and self.e.get().lower() == "t"):
                                score += 1

                        elif(true_case[0] == 0 and self.e.get().lower() == "f"):
                                score += 1

                        # Instantiate a truecase object and a falsecase object
                        tc = TrueCase(self.colours)
                        fc = FalseCase(self.colours)

                        """Here we obtain the random color info as well as a t/f case."""       
                        random.shuffle(self.colours)
                        random.shuffle(true_case) 

                        # Here we implement a color tuple that has either a true case or false case
                        if(true_case[0] == 1):
                              """This is out true case!"""
                              # base_color = self.colours[0]
                              # change the colour to type, by changing the
                              # text _and_ the colour to a random colour value


                              # self.label.config(fg = str(random.choice(self.colours)), text = base_color)
                              # self.label2.config(fg = str(base_color), text = str(random.choice(self.colours)))
                              self.label.config(fg = str(random.choice(tc.colours)), text = tc.base_color)
                              self.label2.config(fg = str(tc.base_color), text = str(random.choice(tc.colours)))
                              
                              print("t")

                              #if (e.get().lower() == "yes"):
                                
                                  #score += 1

                              # clear the text entry box.
                              self.e.delete(0, tkinter.END)
                              # update the score.
                              self.scoreLabel.config(text = "Current score: " + str(score))



                        elif(true_case[0] == 0):
                              """This is our false case!"""       
                              # base_color = self.colours[0]
                              # base_color2 = self.colours[1]
                              # change the colour to type, by changing the
                              # text _and_ the colour to a random colour value


                              #self.label.config(fg = str(random.choice(self.colours)), text = str(base_color))
                              #self.label2.config(fg = str(base_color2), text = str(random.choice(self.colours)))

                              self.label.config(fg = str(random.choice(fc.colours)), text = str(fc.base_color))
                              self.label2.config(fg = str(fc.base_color2), text = str(random.choice(fc.colours)))

                              print("f")

                              #if (e.get().lower() == "no"):
                                
                                  #score += 1

                              # clear the text entry box.
                              self.e.delete(0, tkinter.END)
                              # update the score.
                              self.scoreLabel.config(text = "Current score: " + str(score))

                        

                
                       

                        

        """
           This is a function which represents a timer for the level
        """
        def countdown(self):

                global timeleft

                # if a game is in play
                if timeleft > 0:

                        # decrement the timer.
                        timeleft -= 1
                        
                        # update the time left label
                        self.timeLabel.config(text = "Time left: "
                                                                + str(timeleft))
                                                                        
                        # run the function again after 1 second.
                        self.timeLabel.after(1000, self.countdown)

                else:
                        # destroy all labels and entry box except for 'label' 
                        self.timeLabel.destroy()
                        self.scoreLabel.destroy()
                        self.instructions.destroy()
                        self.e.destroy()

                        # Configure label to tell the player theor time is up, their total score
                        self.label.config(fg = 'black', text = "Time is Up!\n Total score is: "+ str(score))

                        # Enter the nextphase function
                        if nextlevel == 6:
                                self.nextphase()
                        
                    

        """
           This is a function which represents a countdown  for the transition between levels
        """
        def nextphase(self):

                global nextlevel
                global timeleft

                if nextlevel > 0:

                        # decrement the timer by 1.
                        nextlevel -= 1
                        
                        # update the nextlevel label
                        self.label2.config(fg = 'black', text = 
                                                                 str(nextlevel) + '...')
                                                                        
                        # run the function again after 1 second.
                        self.label2.after(1000, self.nextphase)

                else:
                        # Re-instantiate nextlevel to 5 and timeleft to 30
                        nextlevel = 6
                        timeleft = 30
                        # End the game
                        self.destroy()

                
        """
            This is the function where the game is run
            param: event
        """
        def startGame(self, event):


                # Here I run the countdown method when timeleft == 30.             
                if timeleft == 30:
                        
                    # start the countdown timer.
                    self.countdown()
                        
                # run the function to choose the next colours.
                self.nextColour()

        def giveScore(self):                                                               # //added to give score to score class
                return int(score)