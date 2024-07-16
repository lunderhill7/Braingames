from tkinter import *
from tkinter import messagebox
import random
import time
import os
from os import path




class MatchGame():
    
    def __init__ (self):
        
        self.root = Tk()                        #Our window
        self.correct_count = 0                  #Number of correct guesses
        self.difficulty = "easy"                #Game difficulty          
        self.reset_count = 0                    #Number of phases competed per difficulty, 3 completions ramps up the difficulty.
        
        #matches for each level
        self.matches_easy = [1,1,2,2,3,3,4,4]
        self.matches_med = [1,1,2,2,3,3,4,4,5,5,6,6]     
        self.matches_hard = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12]
        
        
        self.answer_list = []       #Contains values that are clicked by user
        self.answer_dict = {}       #Contains 
        self.count = 0          #this is for number of panels clicked, can never exceed 2
        
        self.my_frame = Frame(self.root, width = 750, height = 750)     #creating our frame
        self.my_frame.pack                              
        self.my_frame.grid()                                     #pady = 10 originally, change it back if it doesn't work.
        

        
        self.my_Label = Label(self.root, text="")                #feedback label
        self.my_Label.grid(pady=10) 
        
        self.my_score = 0                                       #user score
        self.my_score_label = Label(self.root, text =  0)
        self.my_score_label.grid(pady = 10)
        
        self.final_score = str(self.my_score)                   #converts user score into a str to be printed
        
        #establishing base panels
        self.panel_0 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_0,0), relief = "groove")
        self.panel_1 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_1,1), relief = "groove")
        self.panel_2 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_2,2), relief = "groove")
        self.panel_3 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_3,3), relief = "groove")
        self.panel_4 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_4,4), relief = "groove")
        self.panel_5 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_5,5), relief = "groove")
        self.panel_6 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_6,6), relief = "groove")
        self.panel_7 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_7,7), relief = "groove")
        self.panel_8 = Button()
        self.panel_9 = Button()
        self.panel_10 = Button()
        self.panel_11 = Button()
        self.panel_12 = Button()
        self.panel_13 = Button()
        self.panel_14 = Button()
        self.panel_15 = Button()
        
        
        self.panel_0.grid(row = 0, column = 0)
        self.panel_1.grid(row = 0, column = 1)
        self.panel_2.grid(row = 0, column = 2)
        self.panel_3.grid(row = 0, column = 3)

        self.panel_4.grid(row = 1, column = 0)
        self.panel_5.grid(row = 1, column = 1)
        self.panel_6.grid(row = 1, column = 2)
        self.panel_7.grid(row = 1, column = 3)
        
        
        
    """Function call for when the user completes a board
    
    Checks the difficulty and the number of phases of the level completed and adjusts depending on those values.
    
    """
    def win(self):
        self.my_Label.config(text = "Completed!")
        
        if self.difficulty == "easy":                                               
            self.panel_list_easy = [self.panel_0,self.panel_1,self.panel_2,self.panel_3,self.panel_4,self.panel_5,self.panel_6,self.panel_7]
            for panel in self.panel_list_easy:
                panel.config(bg = "green")
                
        elif self.difficulty == "medium":
            self.panel_8 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_8,8), relief = "groove")
            self.panel_9 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_9,9), relief = "groove")
            self.panel_10 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_10,10), relief = "groove")
            self.panel_11 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_2panel_11,11), relief = "groove")
        
            self.panel_8.grid(row = 2, column = 0)
            self.panel_9.grid(row = 2, column = 1)
            self.panel_10.grid(row = 2, column = 2)
            self.panel_11.grid(row = 2, column = 3)
        
            self.panel_list_med = [self.panel_0,self.panel_1,self.panel_2,self.panel_3,self.panel_4,self.panel_5,self.panel_6,self.panel_7,self.panel_8,self.panel_9,self.panel_10,self.panel_11]
            for panel in self.panel_list_med:
                panel.config(bg = "green")
        
    
        elif self.difficulty == "hard":
        
            self.panel_8 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_8,8), relief = "groove")
            self.panel_9 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_9,9), relief = "groove")
            self.panel_10 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_10,10), relief = "groove")
            self.panel_11 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_11,11), relief = "groove")
            self.panel_12 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_12,12), relief = "groove")
            self.panel_13 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_13,13), relief = "groove")
            self.panel_14 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_14,14), relief = "groove")
            self.panel_15 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_15,15), relief = "groove")
            
            
            self.panel_8.grid(row = 2, column = 0)
            self.panel_9.grid(row = 2, column = 1)
            self.panel_10.grid(row = 2, column = 2)
            self.panel_11.grid(row = 2, column = 3)
        
            self.panel_12.grid(row = 3, column = 0)
            self.panel_13.grid(row = 3, column = 1)
            self.panel_14.grid(row = 3, column = 2)
            self.panel_15.grid(row = 3, column = 3)
            
            self.panel_list_hard = [self.panel_0,self.panel_1,self.panel_2,self.panel_3,self.panel_4,self.panel_5,self.panel_6,self.panel_7,self.panel_8,self.panel_9,self.panel_10,self.panel_11,self.panel_12,self.panel_13,self.panel_14,self.panel_15]
            for panel in self.panel_list_hard:
                panel.config(bg = "green")
        
        time.sleep(1 * .5)
        self.reset_count +=1
        
        if self.reset_count == 3 and self.difficulty == "easy":                       #checks to se if we can move on  / change back to 3
            self.difficulty = "medium"
            self.reset_count = 0
    
        elif self.reset_count == 3 and self.difficulty == "medium":                   #checks to see if we can move on 
            self.difficulty = "hard"
            self.reset_count = 0

        elif self.reset_count == 3 and self.difficulty == "hard":                 #checks to see if we're finished
            self.my_Label.config(text = "Congratulations! You're final score is below")
            for self.panel in self.panel_list_hard:
                self.panel.config(bg = "green")
            self.clear()
        
        time.sleep(1)
        self.reset()
        
        
    """
    Resets board depending on the difficulty
        
    """
        
    def reset(self):
        self.correct_count = 0
        
        if self.difficulty == "easy":                                       #reset easy board
            self.matches_easy = [1,1,2,2,3,3,4,4]
            random.shuffle(self.matches_easy)                           #reshuffling our board
            
            self.panel_list_easy = [self.panel_0,self.panel_1,self.panel_2,self.panel_3,self.panel_4,self.panel_5,self.panel_6,self.panel_7]
            for panel in self.panel_list_easy:
                panel.config(text=" ", bg = "SystemButtonFace", state = "normal")
            #shuffle our matches
            
            
            
            
        elif self.difficulty == "medium":                                       #reset medium board
            self.matches_med = [1,1,2,2,3,3,4,4,5,5,6,6]
            random.shuffle(self.matches_med)
            
            
            self.panel_8 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_8,8), relief = "groove")
            self.panel_9 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_9,9), relief = "groove")
            self.panel_10 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_10,10), relief = "groove")
            self.panel_11 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_11,11), relief = "groove")


            self.panel_8.grid(row = 2, column = 0)
            self.panel_9.grid(row = 2, column = 1)
            self.panel_10.grid(row = 2, column = 2)
            self.panel_11.grid(row = 2, column = 3)
        
            
            
            self.panel_list_med = [self.panel_0,self.panel_1,self.panel_2,self.panel_3,self.panel_4,self.panel_5,self.panel_6,self.panel_7,self.panel_8,self.panel_9,self.panel_10,self.panel_11]
            
            for panel in self.panel_list_med:
                panel.config(text=" ", bg = "SystemButtonFace", state = "normal")
        
            
        elif self.difficulty == "hard":                                                         #reset hard board
            self.matches_hard = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
            random.shuffle(self.matches_hard)
            
            
            self.panel_8 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_8,8), relief = "groove")
            self.panel_9 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_9,9), relief = "groove")
            self.panel_10 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_10,10), relief = "groove")
            self.panel_11 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_11,11), relief = "groove")
            self.panel_12 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_12,12), relief = "groove")
            self.panel_13 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_13,13), relief = "groove")
            self.panel_14 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_14,14), relief = "groove")
            self.panel_15 = Button(self.my_frame, text = ' ', font = ("Helvetica", 30), height = 3, width = 6, command = lambda: self.button_click(self.panel_15,15), relief = "groove")
            
            
            self.panel_8.grid(row = 2, column = 0)
            self.panel_9.grid(row = 2, column = 1)
            self.panel_10.grid(row = 2, column = 2)
            self.panel_11.grid(row = 2, column = 3)
            self.panel_12.grid(row = 3, column = 0)
            self.panel_13.grid(row = 3, column = 1)
            self.panel_14.grid(row = 3, column = 2)
            self.panel_15.grid(row = 3, column = 3)
            
            
            self.panel_list_hard = [self.panel_0,self.panel_1,self.panel_2,self.panel_3,self.panel_4,self.panel_5,self.panel_6,self.panel_7,self.panel_8,self.panel_9,self.panel_10,self.panel_11,self.panel_12,self.panel_13,self.panel_14,self.panel_15]
            
            for panel in self.panel_list_hard:
                panel.config(text=" ", bg = "SystemButtonFace", state = "normal")
                
        #reset our label
        self.my_Label.config(text= "")

    
    """
    Our Button click function, which clicks our buttons and also chekcs to see whether or not the two panels match. 
    """
    
    
    def button_click(self, button, number):
        
        if button["text"] == ' ' and self.count < 2 and self.difficulty == "easy": 
            button["text"] = self.matches_easy[number]
            #add number to answer list
            self.answer_list.append(number)
            #add button and number to answer dictionary
            self.answer_dict[button] = self.matches_med[number]
            #increment our counter
            self.count += 1
        
        
        if len(self.answer_list) == 2 and self.difficulty == "easy":
            if self.matches_easy[self.answer_list[0]] == self.matches_easy[self.answer_list[1]]:
                self.my_Label.config(text = "MATCH!")
                self.my_score +=3
                self.my_score_label.config(text = self.my_score)
                for key in self.answer_dict:
                    key["state"] = "disabled"
                
                #resets after a match
                self.count = 0
                self.answer_list = []
                self.answer_dict = {}
                #increment correct guesses
                self.correct_count += 1
                
                if self.correct_count == 4:
                    self.win()
        
            else:
                self.my_Label.config(text = "WRONG!")
                
                self.my_score -= 1
                self.my_score_label.config(text = self.my_score)
                
                self.count = 0
                self.answer_list = []
                #pop up box - probably not going to use this 
                messagebox.showinfo('Incorrect!',"Incorrect")
                
                #resest the panels
                
                #time.sleep(1)
                
                
                for key in self.answer_dict:
                    key["text"] = " "
                
                self.answer_dict = {}
            
        if button["text"] == ' ' and self.count < 2 and self.difficulty == "medium": 
            button["text"] = self.matches_med[number]
            #button["image"] = photo
            #add number to answer list
            self.answer_list.append(number)
            #add button and number to answer dictionary
            self.answer_dict[button] = self.matches_med[number]
            #increment our counter
            self.count += 1
        
    #Start to determine if our answers are correct or not
    
        if len(self.answer_list) == 2 and self.difficulty == "medium":
            if self.matches_med[self.answer_list[0]] == self.matches_med[self.answer_list[1]]:
                self.my_Label.config(text = "MATCH!")
                
                self.my_score +=5
                self.my_score_label.config(text = self.my_score)
                
                for key in self.answer_dict:
                    key["state"] = "disabled"
                
                #resets after a match
                self.count = 0
                self.answer_list = []
                self.answer_dict = {}
                #increment correct guesses
                self.correct_count += 1
                
                
                if self.correct_count == 6:
                    self.win()
                    
            else:
                self.my_Label.config(text = "WRONG!")
                
                self.my_score -= 1
                self.my_score_label.config(text = self.my_score)
                
                self.count = 0
                self.answer_list = []
                #pop up box - probably not going to use this 
                messagebox.showinfo('Incorrect!',"Incorrect")
                
                #resest the panels
                
                
                for key in self.answer_dict:
                    key["text"] = " "
                
                self.answer_dict = {}
                
                
        if button["text"] == ' ' and self.count < 2 and self.difficulty == "hard": 
            button["text"] = self.matches_hard[number]
            #button["image"] = photo
            #add number to answer list
            self.answer_list.append(number)
            #add button and number to answer dictionary
            self.answer_dict[button] = self.matches_hard[number]
            #increment our counter
            self.count += 1
        
    #Start to determine if our answers are correct or not
    
        if len(self.answer_list) == 2 and self.difficulty == "hard":
            if self.matches_hard[self.answer_list[0]] == self.matches_hard[self.answer_list[1]]:
                self.my_Label.config(text = "MATCH!")
                
                self.my_score += 10
                self.my_score_label.config(text = self.my_score)
                
                for key in self.answer_dict:
                    key["state"] = "disabled"
                
                #resets after a match
                self.count = 0
                self.answer_list = []
                self.answer_dict = {}
                #increment correct guesses
                self.correct_count += 1
                
                
                if self.correct_count == 8:
                    self.win()
                    
            else:
                self.my_Label.config(text = "WRONG!")
                
                self.my_score -= 1
                self.my_score_label.config(text = self.my_score)

                self.count = 0
                self.answer_list = []
                #pop up box - probably not going to use this 
                messagebox.showinfo('Incorrect!',"Incorrect")
                
                #resest the panels
                
                #time.sleep(1)
                
                
                for key in self.answer_dict:
                    key["text"] = " "
                
                self.answer_dict = {}
    
    
    """
    clears board once you win
    """
    
    def clear(self):
        
        #self.root.quit()
        
        #end_game = Toplevel()
        #end_game.geometry("750x750+350+100")
        #end_frame = Frame(self.root)
        #end_frame.grid(pady=10)  

        self.final_score = str(self.my_score)
        self.my_Label = Label(self.root, text="Congratulations. Your final score is: " + self.final_score, font = ("Arial",25), fg = "green")
        self.my_Label.grid(pady=50, padx = 75) 
        
        #self.my_score_label = Label(text = self.my_score, font = ("Arial", 25))
        
        
        
    
    
        """start of the game
        
        """
    def start(self):
        
        """"""
        """Shuffles the matches list to give random placement on the board"""
        
        self.root.geometry("750x750+350+100")
        random.shuffle(self.matches_easy)

        """Defining our button frame"""

        #my_frame = Frame(root)
        #my_frame.grid(pady=10)  
        
        
            
        #Create a menu - we're gonna edit this
        my_menu = Menu(self.root)
        self.root.config(menu=my_menu)

        #Create an Options Dropdown Menu
        option_menu = Menu(my_menu, tearoff = False)
        my_menu.add_cascade(label = "Options", menu = option_menu)
        option_menu.add_command(label="Reset Game", command = self.reset)
        option_menu.add_separator()
        option_menu.add_command(label="Exit Game", command = self.root.quit)
        

        self.root.mainloop()

        


    
    
    
    def Go():
        
        our_game = MatchGame()
        #our_game.clear()
        our_game.start()
        
    #go() 
    
