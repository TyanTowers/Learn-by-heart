import sys
import random
import warnings
from Obscurex import *
from Utils import *

def GetQnA(lines):
	questions = []
	answers = []
	
	''' rules: questions and answer lines alternate, ignoring all newlines'''
	qflag = True
	for line in lines:
		if line != '\n':
			if qflag:
				questions.append(line)
				qflag = False
			else:
				answers.append(line)
				qflag = True
	if len(questions)!=len(answers):
		warnings.warn('Malformed input file! The number of questions and answers detected is not the same.')

	return questions, answers

def ShouldQRepeat():
	while True:
		ans = input('Do you want to repeat? ')
		if ans=='y':
			return True
		elif ans=='n':
			return False
		else:
			print('Please enter "y" or "n"')

if __name__=="__main__":
	if len(sys.argv) != 2:
		print("Usage: python main.py <filename>")
		sys.exit(1)

	filename = sys.argv[1]
	lines =  ReadFile(filename)
	questions, answers = GetQnA(lines)
	
	numquestions = len(questions)
	
	print('Welcome to the REPETITION GAME. ')
	print('You will be given a question. \n After typing the answer, the program will show you how close you were to the answer. ')
	print('After that you will be asked if you want to repeat this question or not. Type "y" for "yes" and "n" for "no"')
	round = 1
	
	while len(questions)>0:
		numquestions = len(questions)
		qindex = random.sample(list(range(numquestions)), numquestions)
		qno = 1
		newqlist = []
		newalist = []
		for q in qindex:
			print(f'\n\n {qno} of {numquestions}: {questions[q]}\n')
			ans = input('')
			print(get_edits_string(ans, questions[q]))
			qno +=1
			if ShouldQRepeat():
				newqlist.append(questions[q])
				newalist.append(answers[q])
		questions = newqlist
		answers = newalist
		FlashText('You have finished round ' + str(round) + '!')
		round += 1


	FlashText('CONGRATULATIONS!!!!CONGRATULATIONS!!!!CONGRATULATIONS!', duration=5)