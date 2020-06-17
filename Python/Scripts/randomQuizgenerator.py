#! /usr/bin/python3
#randomQuizgenerator.py - Creates a multiple-choice quiz with 3 wrong and 1 correct answer
#50 questions in total
#writes the quiz and the answer keys to a text file
from pathlib import Path
import random, os, pprint

#The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

pythonDir = Path.home() / 'Documents/LearningProgramming/Python'
if (pythonDir / 'Project-randomQuiz').exists():
#Moving to project directory
    os.chdir(pythonDir / 'Project-randomQuiz')
else:
#Creating a directory to proceed with this project
    os.makedirs(pythonDir / 'Project-randomQuiz')
    os.chdir(pythonDir / 'Project-randomQuiz')

#Generate 35 quiz files.
for quizNum in range(35):
   quizFile = open(f'quiz{quizNum + 1}.txt', 'w') 
   answerKeyFile = open(f'answers{quizNum + 1}.txt', 'w') 

   #Write out the header for the quiz.
   quizFile.write('Name:\nDate:\n\n')
   quizFile.write((' '*20) + f'State Capitals Quiz Form{quizNum + 1}')
   quizFile.write('\n\n')

   #Shuffle the order of the states.
   states = list(capitals.keys())
   random.shuffle(states)

   #Loop 50 times to make a question for each state 
   for questionNum in range(50):

       #Get list of the for options
       correctAnswer = capitals[states[questionNum]]
       wrongAnswers = list(capitals.values())
       del wrongAnswers[wrongAnswers.index(correctAnswer)]
       answerOptions = random.sample(wrongAnswers, 3) + [correctAnswer]
       random.shuffle(answerOptions)

       #Write the question and the answer options to the quiz file.
       quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
       for i in range(4):
           quizFile.write(f"{'ABCD'[i]}. {answerOptions[i]}\n")
           quizFile.write('\n')
        
       #Write the answer key to a file.
       answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}")
quizFile.close()
answerKeyFile.close()