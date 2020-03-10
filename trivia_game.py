#!/usr/bin/python3
# Christian Anderson
# 3/9/2020

"A gui-based program that plays a trivia game."

#---Imports---
import pickle
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

#---Constants---
TITLE_FONT = ("Times New Roman", 48)
BUTTON_FONT = ("Arial", 24)
LABEL_FONT = ("Arial", 18)

#---Classes---
class Screen(tk.Frame):
    
    current = 0
    
    def __init__(self):
        tk.Frame.__init__(self)
        
    def switch_frame():
        screens[Screen.current].tkraise()
        
        
class MainMenu(Screen):
    
    def __init__(self):
        Screen.__init__(self)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=1)

        
        self.lbl_title = tk.Label(self,text="Trivia Game", font=TITLE_FONT)
        self.lbl_title.grid(row=0,column=0,rowspan=2,columnspan=4,sticky="news")        
        
        self.btn_games = tk.Button(self,text="  Games  ",font=BUTTON_FONT,command=self.go_trivia_games)
        self.btn_games.grid(row=3,column=1,sticky="news")  
        
        self.btn_geography = tk.Button(self,text="Geography",font=BUTTON_FONT,command=self.go_trivia_geography)
        self.btn_geography.grid(row=3,column=2,sticky="news")
        
        self.btn_history = tk.Button(self,text="History",font=BUTTON_FONT,command=self.go_trivia_history)
        self.btn_history.grid(row=4,column=1,sticky="news")
        
        self.btn_music = tk.Button(self,text="Music",font=BUTTON_FONT,command=self.go_trivia_music)
        self.btn_music.grid(row=4,column=2,sticky="news")
        
        self.btn_random = tk.Button(self,text="Random",font=BUTTON_FONT,command=self.go_trivia_random)
        self.btn_random.grid(row=5,column=1,sticky="news")     
        
        self.btn_gauntlet = tk.Button(self,text="Gauntlet",font=BUTTON_FONT,command=self.go_trivia_gauntlet)
        self.btn_gauntlet.grid(row=5,column=2,sticky="news")
        
        self.btn_highscores = tk.Button(self,text="Highscores",font=BUTTON_FONT,command=self.go_highscores)
        self.btn_highscores.grid(row=7,column=1,columnspan=2,sticky="news")        
        
        
    def go_trivia_games(self): 
        self.going_trivia = 1
        Screen.current=1
        Screen.switch_frame()
        
    def go_trivia_geography(self): 
        self.going_trivia = 2
        Screen.current=1
        Screen.switch_frame()
        
    def go_trivia_history(self): 
        self.going_trivia = 3
        Screen.current=1
        Screen.switch_frame()
        
    def go_trivia_music(self): 
        self.going_trivia = 4
        Screen.current=1
        Screen.switch_frame()
        
    def go_trivia_random(self):   
        self.going_trivia = 5
        Screen.current=1
        Screen.switch_frame()
        
    def go_trivia_gauntlet(self):
        self.going_trivia = 6
        Screen.current=1
        Screen.switch_frame() 
        
    def go_highscores(self):
        Screen.current=3
        Screen.switch_frame()     
        
class Trivia(Screen):
    
    def __init__(self):
        Screen.__init__(self)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1) 

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=1)
        
        
        self.lbl_question_num = tk.Label(self,text="Question:", font=LABEL_FONT)
        self.lbl_question_num.grid(row=0,column=0,sticky="news")
        
        self.lbl_question_num_out_of_num = tk.Label(self,text="# / #", font=LABEL_FONT)
        self.lbl_question_num_out_of_num.grid(row=1,column=0,sticky="news")
        
        self.lbl_trivia_score = tk.Label(self,text="Your Score: #", font=LABEL_FONT)
        self.lbl_trivia_score.grid(row=0,column=3,sticky="news")
        
        self.lbl_trivia_highscore = tk.Label(self,text="High Score: #", font=LABEL_FONT)
        self.lbl_trivia_highscore.grid(row=1,column=3,sticky="news")
        
        self.lbl_trivia_highscore = tk.Label(self,text="Question", font=TITLE_FONT)
        self.lbl_trivia_highscore.grid(row=2,column=0,rowspan=2, columnspan=4,sticky="news")
        
        self.frm_filters = AnswerButtons(self)
        self.frm_filters.grid(row=4,column=0,rowspan=3,columnspan=4,sticky="news")
        
        '''self.lbl_trivia_highscore = tk.Label(self,text="", font=LABEL_FONT)
        self.lbl_trivia_highscore.grid(row=,column=,sticky="news") '''       
        

        
        
        

class Conclusion(Screen):
    
    def __init__(self):
        Screen.__init__(self)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        
        
class Highscores(Screen):
    
    def __init__(self):
        Screen.__init__(self)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)


class AnswerButtons(tk.Frame):
    
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        
        self.btn_comedy = tk.Radiobutton(self, text = "Comedy", value = "comedy.")#, variable = self.favorite, command = self.update_text)
        self.btn_comedy.grid(row = 0, column = 0, sticky = "news")
       
        self.btn_drama = tk.Radiobutton(self, text = "Drama", value = "drama.")#, variable = self.favorite, command = self.update_text)
        self.btn_drama.grid(row = 1, column = 0, sticky = "news")
       
        self.btn_romance = tk.Radiobutton(self, text = "Romance", value = "romance.")#, variable = self.favorite, command = self.update_text)
        self.btn_romance.grid(row = 2, column = 0, sticky = "news")
        
        
#---Global Functions---


#---Main---
if __name__ == "__main__":
    datafile = open("question_trivia_library.pickle","rb")
    questions = pickle.load(datafile)
    datafile.close()
    
    datafile = open("highscore_trivia_library.pickle","rb")
    highscores = pickle.load(datafile)
    datafile.close()
    
    
    root = tk.Tk()
    root.title("Trivia Game")
    root.geometry("480x600")
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    
    screens = [MainMenu(), Trivia(), Conclusion(), Highscores()]
    screens[0].grid(row=0,column=0,sticky="news")
    screens[1].grid(row=0,column=0,sticky="news")
    screens[2].grid(row=0,column=0,sticky="news")
    screens[3].grid(row=0,column=0,sticky="news")
    
    
    screens[0].tkraise()
    root.mainloop()    