import random

vowel = {'a', 'e', 'i','o','u'}

def ReplaceVowels(string):
	for c in vowel:
		string = string.replace(c, '-')
	return string	
	
def RemoveVowels(string):
	for c in vowel:
		string = string.replace(c, '')
	return string
	
def MixLetters(string):
	words = string.split()
	for i in range(len(words)):
		word = words[i]   
		middle = list(word[1:-1])
		random.shuffle(middle)
		words[i] = word[0] + ''.join(middle) + word[-1]
	return ' '.join(words)
	
def FirstLetter(string):
	words = string.split()
	for i in range(len(words)):
		words[i] = words[i][0]
	return ' '.join(words)
	
def RemoveWords(string, level = 1):
	# sanitize level
	level = int(level)
	level = max(level, 1)
	level = min(level, 4)
	words = string.split()
	if level == 1:
		del words[3::4]
	if level == 2:
		del words[2::3]
	if level ==3:
		del words[1::2]
	if level == 4:
		for i in range(len(words),0, -5):
			del words[max(0,i-5):i:2]
	return ' '.join(words)
	
def BeginningAndEnding(string):
	words = string.split()
	words = words[:3] + ['...    ...'] + words [-3:]
	return ' '.join(words)