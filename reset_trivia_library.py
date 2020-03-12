#!/usr/bin/python3
# Christian Anderson
# 3/9/2020

'''a program to reset the pickle file associated with game_library.py'''

import pickle

#this dictionary should be 60 entries long, having 15 questions per category.    Template: 1:['Games Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 'Correct Answer(1, 2, 3, 4)']
questions = {1:['Games Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 'Correct Answer(1, 2, 3, 4)'],
             2:['Games Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 'Correct Answer(1, 2, 3, 4)'], 
             3:['Geography Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 'Correct Answer(1, 2, 3, 4)'],
             4:['Geography Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 'Correct Answer(1, 2, 3, 4)'],
             5:['History Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 'Correct Answer(1, 2, 3, 4)'],
             6:['History Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 'Correct Answer(1, 2, 3, 4)'],
             7:['Music Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 'Correct Answer(1, 2, 3, 4)'],
             8:['Music Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 'Correct Answer(1, 2, 3, 4)'],}

datafile = open("question_trivia_library.pickle", "wb")
pickle.dump(questions, datafile)
datafile.close()

#this dictionary should be 30 entries long, having 5 people per category.  Template: 1:['Name', 'Score', 'Games Highscore']
highscores = {1:['Name', 'Score', 'Games Highscore'],
              2:['Name', 'Score', 'Games Highscore'], 
              3:['Name', 'Score', 'Geography Highscore'],
              4:['Name', 'Score', 'Geography Highscore'],
              5:['Name', 'Score', 'History Highscore'],
              6:['Name', 'Score', 'History Highscore'],
              7:['Name', 'Score', 'Music Highscore'],
              8:['Name', 'Score', 'Music Highscore'],
              7:['Name', 'Score', 'Gauntlet Highscore'],
              8:['Name', 'Score', 'Gauntlet Highscore']}

datafile = open("highscore_trivia_library.pickle", "wb")
pickle.dump(highscores, datafile)
datafile.close()