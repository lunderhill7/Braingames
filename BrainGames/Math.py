import pygame
import random
import os
from os import path
import pygame.gfxdraw
import math, sys
from Button import Button
from Math_Button import Math_Button
from Timer import Timer
# Initializing pygame
pygame.init()

# Clock and frame rat

class Math:


    def __init__(self, screen, level):
        # creating an instance of a math game
        
        # init screen 
        self.screen = screen

        #timer functions
        self.timer = Timer(30)
       
        # Create font for the "chalk board " feel and load background image
        self.score_font = pygame.font.Font(os.path.join("images", 'font2.ttf'), 100)
        self.background: pygame.Surface
        self.background=pygame.image.load(path.join("images", "board.jpg")).convert()
        
        self.level=level # the current difficulty level
        
        self.num1 = 0 #first number of an equation
        self.num2 = 0 #second number of an equation
        self.result = 0 #result of an equation 
        self.op = "" #the mathematical operation
        
        self.correct = False #keep track if current equation is true or false
        self.done_with_level = False # see if we are done with the current level
        self.reset = False #reset an equation
        
        self.solution_buttons = [] #a list of multiple choice buttons
        self.problem_count = 5*level+1 #the number of problems in the current level
        self.num_correct = 0 #the numver of correct answers chosen by user
        self.questions_wrong = 0 #the number of incorrect choices made by user
        self.problems_done = 1 #the number of problems completed
        self.max_differential = 10*level # the max number that an equation can use 
       
      
        # self.s = pygame.Surface((100,100))# the size of your rect
        # self.s.set_alpha(128)                # alpha level
        # self.s.fill((255,255,255))           # this fills the entire surface

        self.set_problem() #initalize the first equation 


    def run_game(self):
        #the call to run game which will start the game and check to see if we are finished 
        pygame.display.set_caption('Math Game Level ' +str(self.level))
        self.timer.startTimer()
        while self.end_game():
            self.start_game()
   

    def start_game(self):
        #start inital game logic
        self.process_user_input()
        self.display()
        

    def end_game(self):
        #function call to know we are done with the game
        if self.timer.isFinished() : #function to check if timer is finished
            pygame.time.wait(1000)
            return self.done_with_level# if the timer reaches zero before the user is done then game will move on wihtout "great job screen"

        return not self.done_with_level #if the user does not run out of time the game will continue as normal
        
      
        
       

    def addition(self):
        """ set num 1 and num 2 and return answer """
        a = random.randint(0,self.max_differential)
        b = random.randint(0,self.max_differential)
        self.num1 = a
        self.num2 = b
        self.result = a + b
        self.op = "+"



    def subtraction(self):
        """ set num 1 and num 2 and return answer """
        a = random.randint(0,self.max_differential)
        b = random.randint(0,self.max_differential)
        if a > b:
            self.num1 = a
            self.num2 = b
            self.result = a - b
        else:
            self.num1 = b
            self.num2 = a
            self.result = b - a
        self.op = "-"

    def multiplication(self):
        """ set num 1 and num 2 and return answer"""
        a = random.randint(0,self.max_differential)
        b = random.randint(0,self.max_differential)
        self.num1 = a
        self.num2 = b
        self.result = a * b
        self.op = "x"

    def division(self):
        """ set num 1 and num 2 and return answer for the equation """
        divisor = random.randint(1,self.max_differential)
        dividend = divisor * random.randint(1,self.max_differential)
        quotient = dividend / divisor
        self.num1 = dividend
        self.num2 = divisor
        self.result = math.trunc(quotient)
        self.op = "/"            


    def process_user_input(self): # ,screen):  
        #gathering user events and checking for mouse clicks    
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If user clicked close
                pygame.quit()                    
                sys.exit()
                # return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.check_result()
                
        return False
    
    def set_problem(self) -> None:
        # we will randomize the next equations operation
        x = random.randint(1,4)
        #now create new values
        if x == 1:
            self.op = "+"
            self.addition()
    
        elif x == 2:
            self.op = "-"
            self.subtraction()
           
        elif x == 3:
            self.op = "x"
            self.multiplication()
          
        elif x == 4:
            self.op = "/"
            self.division()
        #create new multiple choice buttons 
        self.solution_buttons = self.get_result_as_button()
        
            
    def get_result_as_button(self):
        # a 'getter' that will return a list of buttons in a random order and define their results/values
        buttons = []
        Y_cord = 350
        #define a random index for where the answer is located
        answer_index = random.randint(1,4)

        #for each button...
        for i in range (1,5):
            #we are the answer button
            if(i == answer_index):
                result_button = Math_Button(i*130,Y_cord,100,100,self.result)
                buttons.append(result_button)
            #generate false values
            else:
                incorrect_button = Math_Button(i*130,Y_cord,100,100,random.randint(self.result-15,self.result+15))
                buttons.append(incorrect_button)
        
        return buttons
        
    def check_result(self): # ,screen):
        #for each button...
        for i in self.solution_buttons:
            #check if it is pressed
            if i.isPressed(self.screen):
                #change correct button to green and update class values
                if i.get_val() == self.result:
                    self.correct = True
                    i.change_color((0,200,0,128))
                    self.num_correct +=1
                else:
                    #change incorrect button to red and update class values
                    self.questions_wrong = self.questions_wrong + 1
                    i.change_color((255,0,0,128))
                    
                self.reset = True

    def giveScore(self):
        #calculate a score value
        self.score = int((self.num_correct/self.problems_done)*100)                                                                   # //added to give score to score class
        return self.score
        
    def display(self): # ,screen):
        #handle screen enitities
        
        self.screen.blit(self.background, (-128, 0))
        white = (255,255,255)

        #display for timer
        
        self.font = pygame.font.SysFont(None, 100)
        self.text = self.font.render("Time Left: "+ str(math.ceil(self.timer.getTime())), True, (255, 255, 255))
        self.screen.blit(self.text, (8,8))
  
        
        wait = False
        
        #end of level screen 
        if self.problems_done == self.problem_count:
            self.done_with_level = True
            msg_1 = "Great job!"
            label1 = self.score_font.render(msg_1,True,white)

            self.screen.blit(label1,(295,335))
            self.count = 0
            wait = True
            # show our buttons 
        else:
            
            equation = self.score_font.render(str(self.num1)+ " " +str(self.op) + " "+ str(self.num2)+ " = ?",True,white)
            self.screen.blit(equation,((self.screen.get_width()/2) - (equation.get_width()/2),225))
           
            for i in self.solution_buttons:
                i.draw(self.screen)
                
        pygame.display.flip()
            
        #reset screen and values
        if self.reset:
            # wait 1 second
            pygame.time.wait(1000)
            self.set_problem()
            # Increase count by 1
            self.problems_done+=1
            self.reset = False 
        elif wait:
            # wait three seconds
            pygame.time.wait(1000)  
