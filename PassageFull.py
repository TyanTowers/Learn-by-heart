import sys
import random
import warnings
from Obscurex import *
from Utils import *
from pdb import set_trace

if __name__=="__main__":
	if len(sys.argv) != 2:
		print("Usage: python PassageDavid2.py <filename>")
		sys.exit(1)

	sess = 100
	
	filename = sys.argv[1]
	lines =  ReadFile(filename)
	passage = " ".join(lines).replace("\n", "")
	numchars = len(passage)
	
	print('WELCOME to the PASSAGE MEMORIZATION GAME!')
	print('For each level, the passage will be shown in an obscured manner.')
	print('Decode the passage and read aloud. ')
	
	print('\n\nLEVEL 0: MIX LETTERS\n ')
	print(MixLetters(passage))
	ans=input('')
	print(get_edits_string(ans, passage))
	FlashText('Good Job. You have passed this level.')
	
	print('\n\nLEVEL 1: REPLACED VOWELS\n ')
	print(ReplaceVowels(passage))
	ans=input('')
	print(get_edits_string(ans, passage))
	FlashText('Good Job. You have passed this level.')
	
	
	print('\n\nLEVEL 2: REMOVED VOWELS\n ')
	print(RemoveVowels(passage))
	ans=input('')
	print(get_edits_string(ans, passage))
	FlashText('Good Job. You have passed this level.')
	
	
	print('\n\nLEVEL 3: REMOVED WORDS LEVEL 1\n ')
	print(RemoveWords(passage, level=1))
	ans=input('')
	print(get_edits_string(ans, passage))
	FlashText('Good Job. You have passed this level.')
	
	print('\n\nLEVEL 4: REMOVED WORDS LEVEL 2\n ')
	print(RemoveWords(passage, level=2))
	ans=input('')
	print(get_edits_string(ans, passage))
	FlashText('Good Job. You have passed this level.')
	
	print('\n\nLEVEL 5: REMOVED WORDS LEVEL 2 AND MISSING VOWELS\n ')
	print(RemoveWords(RemoveVowels(passage), level=2))
	ans=input('')
	print(get_edits_string(ans, passage))
	FlashText('Good Job. You have passed this level.')
	
	print('\n\nLEVEL 6: REMOVED WORDS LEVEL 3\n ')
	print(RemoveWords(passage, level=3))
	ans=input('')
	print(get_edits_string(ans, passage))
	FlashText('Good Job. You have passed this level.')
	
	print('\n\nLEVEL 7: REMOVED WORDS LEVEL 3 AND MISSING VOWELS\n ')
	print(RemoveWords(RemoveVowels(passage), level=3))
	ans=input('')
	print(get_edits_string(ans, passage))
	FlashText('Good Job. You have passed this level.')
	
	print('\n\nLEVEL 8: REMOVED WORDS LEVEL 4\n ')
	print(RemoveWords(passage, level=4))
	ans=input('')
	print(get_edits_string(ans, passage))
	FlashText('Good Job. You have passed this level.')
	
	print('\n\nLEVEL 9: REMOVED WORDS LEVEL 4 AND MISSING VOWELS\n ')
	print(RemoveWords(RemoveVowels(passage),level=4))
	input('')
	FlashText('Good Job. You have passed this level.')
	
	print('\n\nLEVEL 10: FIRST LETTER\n ')
	print(FirstLetter(passage))
	ans=input('')
	print(get_edits_string(ans, passage))
	FlashText('Good Job. You have passed this level.')
	
	FlashText('You have passed the hardest level. CONGRATULATIONS!!!!CONGRATULATIONS!!!!CONGRATULATIONS!', duration=15)
	