#!/usr/bin/python3
# Christian Anderson
# 3/9/2020

"A gui-based program that plays a trivia game."

#---Imports---
import pickle
import tkinter as tk
import random as rd
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

#---Constants---
TITLE_FONT = ("Times New Roman", 40)
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

        
        self.lbl_title = tk.Label(self, text="Trivia Game", font=TITLE_FONT)
        self.lbl_title.grid(row=0, column=0, rowspan=2, columnspan=4, sticky="news")        
        
        self.btn_games = tk.Button(self, text="  Games  ", font=BUTTON_FONT, command=self.go_trivia_games)
        self.btn_games.grid(row=3, column=1, sticky="news")  
        
        self.btn_geography = tk.Button(self, text="Geography", font=BUTTON_FONT, command=self.go_trivia_geography)
        self.btn_geography.grid(row=3, column=2, sticky="news")
        
        self.btn_history = tk.Button(self, text="History", font=BUTTON_FONT, command=self.go_trivia_history)
        self.btn_history.grid(row=4, column=1, sticky="news")
        
        self.btn_music = tk.Button(self, text="Music", font=BUTTON_FONT, command=self.go_trivia_music)
        self.btn_music.grid(row=4, column=2, sticky="news")
        
        self.btn_random = tk.Button(self, text="Random", font=BUTTON_FONT, command=self.go_trivia_random)
        self.btn_random.grid(row=5, column=1, sticky="news")     
        
        self.btn_gauntlet = tk.Button(self, text="Gauntlet", font=BUTTON_FONT, command=self.go_trivia_gauntlet)
        self.btn_gauntlet.grid(row=5, column=2, sticky="news")
        
        self.btn_highscores = tk.Button(self, text="Highscores", font=BUTTON_FONT, command=self.go_highscores)
        self.btn_highscores.grid(row=7, column=1, columnspan=2, sticky="news")        
        
        
    def go_trivia_games(self):
        pop_up = tk.Tk()
        pop_up.title("Info")
        
        frm_trivia_info=TriviaSummary(pop_up, "Games", "all kinds of video games.")
        frm_trivia_info.grid(row=0,column=0)
        
    def go_trivia_geography(self): 
        pop_up = tk.Tk()
        pop_up.title("Info")
        
        frm_trivia_info=TriviaSummary(pop_up, "Geography", "lands and locations of today.")
        frm_trivia_info.grid(row=0,column=0)
        
    def go_trivia_history(self): 
        pop_up = tk.Tk()
        pop_up.title("Info")
        
        frm_trivia_info=TriviaSummary(pop_up, "History", "historical events and people.")
        frm_trivia_info.grid(row=0,column=0)
        
    def go_trivia_music(self): 
        pop_up = tk.Tk()
        pop_up.title("Info")
        
        frm_trivia_info=TriviaSummary(pop_up, "Music", "songs, from the modern to the classical.")
        frm_trivia_info.grid(row=0,column=0)
        
    def go_trivia_random(self):   
        pop_up = tk.Tk()
        pop_up.title("Info")
        
        frm_trivia_info=TriviaSummary(pop_up, "Random", "every category, testing your knowledge.")
        frm_trivia_info.grid(row=0,column=0)
        
    def go_trivia_gauntlet(self):
        pop_up = tk.Tk()
        pop_up.title("Info")
        
        frm_trivia_info=TriviaSummary(pop_up, "Gauntlet", "to test your mettle and flex your brain.")
        frm_trivia_info.grid(row=0,column=0) 
        
    def go_highscores(self):
        Screen.current=3
        Screen.switch_frame() 
        
        
class Trivia(Screen):
    
    def __init__(self, trivia_category):
        Screen.__init__(self)
        self.question_number = 0
        
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
        
        
        self.lbl_question_num = tk.Label(self, text="Question:             ", font=LABEL_FONT)
        self.lbl_question_num.grid(row=0, column=0, sticky="ews")
        
        self.lbl_question_num_out_of_num = tk.Label(self, text="__/10                 ", font=LABEL_FONT)
        self.lbl_question_num_out_of_num.grid(row=1, column=0, sticky="new")
        
        self.lbl_trivia_score = tk.Label(self, text="Your Score: ___/100", font=LABEL_FONT)
        self.lbl_trivia_score.grid(row=0, column=3, sticky="ews")
        
        self.lbl_trivia_highscore = tk.Label(self, text="High Score: ___/100", font=LABEL_FONT)
        self.lbl_trivia_highscore.grid(row=1, column=3, sticky="new")
        
        self.lbl_trivia_question_1 = tk.Label(self, text="Question Part 1", font=TITLE_FONT)
        self.lbl_trivia_question_1.grid(row=2,column=0, columnspan=4, sticky="ews")
        
        self.lbl_trivia_question_2 = tk.Label(self, text="Question Part 2", font=TITLE_FONT)
        self.lbl_trivia_question_2.grid(row=3,column=0, columnspan=4, sticky="new")        
        
        self.frm_answers = AnswerButtons(self)
        self.frm_answers.grid(row=4,column=0,rowspan=3,columnspan=4, sticky="ew")
        
        self.btn_trivia_continue = tk.Button(self, text="Continue", font=BUTTON_FONT, command=self.go_conclusion)
        self.btn_trivia_continue.grid(row=8, column=0, columnspan=4, sticky="news") 
        
    
    def go_conclusion(self):
        messagebox.showinfo(message="Your answer was: Correct/Wrong")
        if self.question_number == 10:
            self.question_number = 0
            Screen.current=2
            Screen.switch_frame()  
        else:
            self.question_number += 1
            '''pop_up = tk.Tk()
            pop_up.title("Answer")
            
            frm_trivia_answer=QuestionAnswered(pop_up)
            frm_trivia_answer.grid(row=0,column=0)'''            
            
        
        
    
        

class Conclusion(Screen):
    
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
        
        
        self.lbl_conclusion_title = tk.Label(self, text="Your Score is:", font=TITLE_FONT)
        self.lbl_conclusion_title.grid(row=0, column=0, rowspan=2, columnspan=4, sticky="news") 
        
        self.lbl_conclusion_score = tk.Label(self, text="___/100", font=LABEL_FONT)
        self.lbl_conclusion_score.grid(row=2, column=1, columnspan=2, sticky="new")
        
        self.lbl_old_highscore = tk.Label(self, text="Old Highscores:", font=LABEL_FONT)
        self.lbl_old_highscore.grid(row=3, column=0, columnspan=4, sticky="news")
        
        self.scr_old_highscore = ScrolledText(self, height=3)
        self.scr_old_highscore.grid(row=4, column=0, columnspan=4,sticky="news")        
        
        self.lbl_new_highscore = tk.Label(self, text="New Highscores:", font=LABEL_FONT)
        self.lbl_new_highscore.grid(row=5, column=0, columnspan=4, sticky="news")
        
        self.scr_new_highscore = ScrolledText(self, height=3)
        self.scr_new_highscore.grid(row=6, column=0, columnspan=4, sticky="news")        
        
        self.btn_retry = tk.Button(self, text="Retry", font=BUTTON_FONT, command=self.go_trivia)
        self.btn_retry.grid(row=8, column=0, columnspan=2, sticky="news")
        
        self.btn_quit = tk.Button(self, text="Quit ", font=BUTTON_FONT, command=self.go_main_menu)
        self.btn_quit.grid(row=8, column=2, columnspan=2, sticky="news") 
        
        
    def go_main_menu(self):
        Screen.current=0
        Screen.switch_frame()
        
    def go_trivia(self):
        Screen.current=1
        Screen.switch_frame()        
        
        
class Highscores(Screen):
    
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
    

        self.lbl_games = tk.Label(self, text="  Games  ", font=TITLE_FONT)
        self.lbl_games.grid(row=0, column=0, columnspan=2, sticky="news")  
        
        self.scr_games = ScrolledText(self, height=3)
        self.scr_games.grid(row=1, column=0, columnspan=2, sticky="news")        
        
        self.lbl_geography = tk.Label(self, text="Geography", font=TITLE_FONT)
        self.lbl_geography.grid(row=0, column=2, columnspan=2, sticky="news")
        
        self.scr_geography = ScrolledText(self, height=3)
        self.scr_geography.grid(row=1, column=2, columnspan=2, sticky="news")        
        
        self.lbl_history = tk.Label(self, text="History", font=TITLE_FONT)
        self.lbl_history.grid(row=2, column=0, columnspan=2, sticky="news")
        
        self.scr_history = ScrolledText(self, height=3)
        self.scr_history.grid(row=3, column=0, columnspan=2, sticky="news")        
        
        self.lbl_music = tk.Label(self, text="Music", font=TITLE_FONT)
        self.lbl_music.grid(row=2, column=2, columnspan=2, sticky="news")
        
        self.scr_music = ScrolledText(self, height=3)
        self.scr_music.grid(row=3, column=2, columnspan=2, sticky="news")        
        
        self.lbl_random = tk.Label(self, text="Random", font=TITLE_FONT)
        self.lbl_random.grid(row=4, column=0, columnspan=2, sticky="news")
        
        self.scr_random = ScrolledText(self, height=3)
        self.scr_random.grid(row=5, column=0, columnspan=2, sticky="news")        
        
        self.lbl_gauntlet = tk.Label(self, text="Gauntlet", font=TITLE_FONT)
        self.lbl_gauntlet.grid(row=4, column=2, columnspan=2, sticky="news")
        
        self.scr_gauntlet = ScrolledText(self, height=3)
        self.scr_gauntlet.grid(row=5, column=2, columnspan=2, sticky="news")
        
        self.btn_conclusion_quit = tk.Button(self, text="Quit", font=BUTTON_FONT, command=self.go_main_menu)
        self.btn_conclusion_quit.grid(row=8, column=0, columnspan=4, sticky="news")   
        
        
    def go_main_menu(self):
        Screen.current=0
        Screen.switch_frame()        


class AnswerButtons(tk.Frame):
    
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        
        self.btn_answer_1 = tk.Radiobutton(self, text="Answer 1", font=LABEL_FONT, value=1)#, variable = self.favorite, command = self.update_text)
        self.btn_answer_1.grid(row=0, column=0, sticky="news")
       
        self.btn_answer_2 = tk.Radiobutton(self, text="Answer 2", font=LABEL_FONT, value=2)#, variable = self.favorite, command = self.update_text)
        self.btn_answer_2.grid(row=1, column=0, sticky="news")
       
        self.btn_answer_3 = tk.Radiobutton(self, text="Answer 3", font=LABEL_FONT, value=3)#, variable = self.favorite, command = self.update_text)
        self.btn_answer_3.grid(row=2, column=0, sticky="news")
        
        self.btn_answer_4 = tk.Radiobutton(self, text="Answer 4", font=LABEL_FONT, value=4)#, variable = self.favorite, command = self.update_text)
        self.btn_answer_4.grid(row=3, column=0, sticky="news")  
        
        
class TriviaSummary(tk.Frame):
    
    def __init__(self, parent, trivia_category, category_info):
        tk.Frame.__init__(self, master=parent)
        self.parent = parent
        
        
        self.lbl_trivia_type = tk.Label(self, text=trivia_category, font=TITLE_FONT)
        self.lbl_trivia_type.grid(row=0, column=0, columnspan=2, sticky="news")        
        
        if trivia_category == "Gauntlet":
            self.lbl_info_1 = tk.Label(self, text="A 50 question marathon meant", font=LABEL_FONT)
            self.lbl_info_1.grid(row=1, column=0, columnspan=2, sticky="news")
        else:
            self.lbl_info_1 = tk.Label(self, text="A 10 question quiz about", font=LABEL_FONT)
            self.lbl_info_1.grid(row=1, column=0, columnspan=2, sticky="news")        
        
        self.lbl_info_2 = tk.Label(self, text=category_info, font=LABEL_FONT)
        self.lbl_info_2.grid(row=2, column=0, columnspan=2, sticky="news")
        
        self.lbl_name = tk.Label(self, text="Name:", font=LABEL_FONT)
        self.lbl_name.grid(row=3, column=0, sticky="news")
        
        self.ent_name = tk.Entry(self)
        self.ent_name.grid(row=3,column=1,sticky="news")
        
        self.btn_popup_quit = tk.Button(self, text="Exit", font=BUTTON_FONT, command=self.cancel)
        self.btn_popup_quit.grid(row=4, column=0, sticky="news")
        
        self.btn_popup_continue = tk.Button(self, text="Continue", font=BUTTON_FONT, command=self.go_trivia)
        self.btn_popup_continue.grid(row=4, column=1, sticky="news")
        
        
    def cancel(self):
        self.parent.destroy()
        
    def go_trivia(self):
        Trivia().tkraise()
        
        
        '''Screen.current=1
        screens[Screen.current].update()
        Screen.switch_frame()
        self.parent.destroy()'''        


'''class QuestionAnswered(tk.Frame):
    
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)
        self.parent = parent
        
        
        self.lbl_your_answer = tk.Label(self, text="Your Answer Was:", font=LABEL_FONT)
        self.lbl_your_answer.grid(row=0, column=0, sticky="news")
        
        self.ent_your_answer = tk.Entry(self)
        self.ent_your_answer.grid(row=1, column=0, sticky="news")
        
        self.lbl_correct_answer = tk.Label(self, text="The Correct Answer Was:", font=LABEL_FONT)
        self.lbl_correct_answer.grid(row=2, column=0, sticky="news")
        
        self.ent_correct_answer = tk.Entry(self)
        self.ent_correct_answer.grid(row=3, column=0, sticky="news")
        
        self.lbl_trivia_type = tk.Label(self, text="Hooray! / You Suck!", font=LABEL_FONT)
        self.lbl_trivia_type.grid(row=4, column=0, sticky="news")
        
        self.btn_trivia_next = tk.Button(self, text="Continue", font=BUTTON_FONT, command=self.next_question)
        self.btn_trivia_next.grid(row=5, column=0, sticky="news") 
        
        
    def next_question(self):
        self.parent.destroy()'''    
        
        
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