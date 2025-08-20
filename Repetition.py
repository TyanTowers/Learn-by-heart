import sys
import random
from Obscurex import *
from Utils import *

def ShouldQRepeat():
	while True:
		ans = input('Do you want to repeat? ')
		if ans=='y':
			return True
		elif ans=='n':
			return False
		else:
			print('Please enter "y" or "n"')

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python main.py <filename>")
		sys.exit(1)

	filename = sys.argv[1]
	questions =  ReadFile(filename)
	
	print('Welcome to the REPETITION GAME. ')
	print('You will be given a prompt for each sentence. \n After typing the full sentence, the program will show you how close you were to the answer. ')
	print('After that you will be asked if you want to repeat this question or not. Type "y" for "yes" and "n" for "no"')
	round = 1
	while len(questions)>0:
		numquestions = len(questions)
		quest = random.sample(questions, len(questions))
		qno = 1
		newlist = []
		for q in quest:
			ans = input('\n\n' + str(qno) + ' of ' + str(numquestions) + ': ' + BeginningAndEnding(q) + '\n')
			print(get_edits_string(ans, q))
			qno +=1
			if ShouldQRepeat():
				newlist.append(q)
		questions = newlist
		FlashText('You have finished round ' + str(round) + '!')
		round += 1

	FlashText('CONGRATULATIONS!!!!CONGRATULATIONS!!!!CONGRATULATIONS!', duration=5)