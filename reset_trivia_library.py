#!/usr/bin/python3
# Christian Anderson
# 3/9/2020

'''a program to reset the pickle file associated with game_library.py'''

import pickle

questions = {1:['History Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 'Correct Answer(1, 2, 3, 4)'],
             2:['History Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 'Correct Answer(1, 2, 3, 4)]'], 
             3:['Geography Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 'Correct Answer(1, 2, 3, 4)'],
             4:['Geography Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 'Correct Answer(1, 2, 3, 4)'],
             5:['Music Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 'Correct Answer(1, 2, 3, 4)'],
             6:['Music Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 'Correct Answer(1, 2, 3, 4)'],
             7:['Games Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 'Correct Answer(1, 2, 3, 4)'],
             8:['Games Question', 'Answer 1', 'Answer 2', 'Answer 3', 'Answer 4', 'Correct Answer(1, 2, 3, 4)'],}

datafile = open("question_trivia_library.pickle", "wb")
pickle.dump(questions, datafile)
datafile.close()


highscores = {1:['FPS', 'Halo3', 'Bungie', 'Microsoft', 'Xbox', '2007', '10', '2', '30.00', 'Yes', '1/15/2008', 'This game is overrated'],
         2:['RPG', 'Undertale', 'Toby Fox', '8-4', 'PC, PS4, PS Vita, Nintendo Switch', '2015', '10', '1', '10.00', 'Yes', '2/2/2016', 'Its pretty darn good yo']}

datafile = open("highscore_trivia_library.pickle", "wb")
pickle.dump(highscores, datafile)
datafile.close()