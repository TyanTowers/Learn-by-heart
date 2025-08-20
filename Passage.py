import sys
import random
import warnings
from Obscurex import *
from Utils import *
from pdb import set_trace

if __name__=="__main__":
	if len(sys.argv) != 2:
		print("Usage: python main.py <filename>")
		sys.exit(1)

	sess = 100
	
	filename = sys.argv[1]
	lines =  ReadFile(filename)
	passage = " ".join(lines).replace("\n", "")
	numchars = len(passage)
	
	print('WELCOME to the PASSAGE MEMORIZATION GAME!')
	print('For each level, 200 characters of a passage will be shown at a time in an obscured manner.')
	print('Decode the passage and write down the characters you see as far as you can. You will be shown whether you were correct or wrong.')
	print('The program will start from where you left off')
	
	print('\n\nLEVEL 1: REMOVED VOWELS\n ')
	pointer = 0
	while(pointer<numchars):
		ans = input(f'{pointer}-{min(pointer+sess,numchars)} of {numchars}: {RemoveVowels(passage[pointer:min(pointer+sess,numchars-1)])}\n')
		print(get_edits_string(ans, passage[pointer:min(pointer+len(ans), len(passage)-1)]))
		#pointer += len(ans)
		pointer += 100
	FlashText('Good Job. You have passed this level.')

	print('\n\nLEVEL 2: REMOVED WORDS LEVEL 2 AND MISSING VOWELS\n ')
	pointer = 0
	while(pointer<numchars):
		ans = input(f'{pointer}-{min(pointer+sess,numchars)} of {numchars}: {RemoveWords(RemoveVowels(passage[pointer:min(pointer+sess,numchars-1)]), level=2)}\n')
		print(get_edits_string(ans, passage[pointer:min(pointer+len(ans), len(passage)-1)]))
		#pointer += len(ans)
		pointer += 100
	FlashText('Good Job. You have passed this level.')
	
	print('\n\nLEVEL 3: REMOVED WORDS LEVEL 3 AND MISSING VOWELS\n ')
	pointer = 0
	while(pointer<numchars):
		ans = input(f'{pointer}-{min(pointer+sess,numchars)} of {numchars}: {RemoveWords(RemoveVowels(passage[pointer:min(pointer+sess,numchars-1)]), level=3)}\n')
		print(get_edits_string(ans, passage[pointer:min(pointer+len(ans), len(passage)-1)]))
		#pointer += len(ans)
		pointer +=100
	FlashText('Good Job. You have passed this level.')
	
	print('\n\nLEVEL 4: REMOVED WORDS LEVEL 4 AND MISSING VOWELS\n ')
	pointer = 0
	while(pointer<numchars):
		ans = input(f'{pointer}-{min(pointer+sess,numchars)} of {numchars}: {RemoveWords(RemoveVowels(passage[pointer:min(pointer+sess,numchars-1)]), level=4)}\n')
		print(get_edits_string(ans, passage[pointer:min(pointer+len(ans), len(passage)-1)]))
		#pointer += len(ans)
		pointer += 100
	FlashText('Good Job. You have passed this level.')
	
	FlashText('CONGRATULATIONS!!!!CONGRATULATIONS!!!!CONGRATULATIONS!', duration=5)