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
		if line != '\n' or line != '\r\n':
			if qflag:
				questions.append(line)
				qflag = False
			else:
				answers.append(line)
				qflag = True
	if len(questions)!=len(answers):
		warnings.warn('Malformed input file! The number of questions and answers detected is not the same.')

	return questions, answers

if __name__=="__main__":
	if len(sys.argv) != 2:
		print("Usage: python main.py <filename>")
		sys.exit(1)

	filename = sys.argv[1]
	lines =  ReadFile(filename)
	questions, answers = GetQnA(lines)
	
	numquestions = len(questions)
	
	print('WELCOME to the QnA MEMORIZATION GAME!')
	print('For each level, the the question will be shown and the answers will be obscured in increasingly difficult ways. Decode the answers and write the corrected ones below. ')
	print('You will be shown whether you were correct or wrong.')
	
	print('\n\nLEVEL 1: REMOVED VOWELS\n ')
	qindex = random.sample(list(range(numquestions)), numquestions)
	qno = 1
	for q in qindex:
		print('\n\n' + str(qno) + ' of ' + str(numquestions) + ': ' + questions[q])
		ans = input(RemoveVowels(answers[q]) + '\n')
		#print(get_edits_string(ans, answers[q]))
		qno += 1
	FlashText('Good Job. You have passed this level.')
		
	print('\n\nLEVEL 2: REMOVED WORDS LEVEL 2 AND MISSING VOWELS\n ')
	qindex = random.sample(list(range(numquestions)), numquestions)
	qno = 1
	for q in qindex:
		print('\n\n' + str(qno) + ' of ' + str(numquestions) + ': ' + questions[q])
		ans = input(RemoveWords(RemoveVowels(answers[q]), level=2) + '\n')
		#print(get_edits_string(ans, answers[q]))
		qno += 1
	FlashText('Good Job. You have passed this level.')
	
	print('\n\nLEVEL 3: REMOVED WORDS LEVEL 3 AND MISSING VOWELS\n ')
	qindex = random.sample(list(range(numquestions)), numquestions)
	qno = 1
	for q in qindex:
		print('\n\n' + str(qno) + ' of ' + str(numquestions) + ': ' + questions[q])
		ans = input(RemoveWords(RemoveVowels(answers[q]), level=3) + '\n')
		#print(get_edits_string(ans, answers[q]))
		qno += 1
	FlashText('Good Job. You have passed this level.')
	
	print('\n\nLEVEL 4: REMOVED WORDS LEVEL 4 AND MISSING VOWELS\n ')
	qindex = random.sample(list(range(numquestions)), numquestions)
	qno = 1
	for q in qindex:
		print('\n\n' + str(qno) + ' of ' + str(numquestions) + ': ' + questions[q])
		ans = input(RemoveWords(RemoveVowels(answers[q]), level=4) + '\n')
		#print(get_edits_string(ans, answers[q]))
		qno += 1
	FlashText('Good Job. You have passed this level.')
	
	FlashText('CONGRATULATIONS!!!!CONGRATULATIONS!!!!CONGRATULATIONS!', duration=5)
	
