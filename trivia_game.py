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
TITLE_FONT = ("Times New Roman", 24)
BUTTON_FONT = ("Arial", 15)

#---Classes---


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
    root.title("Media Library")
    root.geometry("500x500")
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    
    
    screens[0].tkraise()
    root.mainloop()    