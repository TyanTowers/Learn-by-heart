import difflib
import time
import sys
import random

def ReadFile(filename):
	lines = []
	try:
		with open(filename, 'r', encoding='utf-8') as file:
			lines = file.readlines()
	except FileNotFoundError:
		print(f"Error: File '{filename}' not found.")
	except Exception as e:
		print(f"Error: {e}")
	return lines

red = lambda text: f"\033[38;2;255;0;0m{text}\033[0m"
green = lambda text: f"\033[38;2;0;255;0m{text}\033[0m"
blue = lambda text: f"\033[38;2;0;0;255m{text}\033[0m"
white = lambda text: f"\033[38;2;255;255;255m{text}\033[0m"

def get_edits_string(old, new):
    result = ""
    codes = difflib.SequenceMatcher(a=old, b=new).get_opcodes()
    for code in codes:
        if code[0] == "equal": 
            result += old[code[1]:code[2]]
        elif code[0] == "delete":
            result += red(old[code[1]:code[2]])
        elif code[0] == "insert":
            result += green(new[code[3]:code[4]])
        elif code[0] == "replace":
            result += (red(old[code[1]:code[2]]) + green(new[code[3]:code[4]]))
    return result

class Color:
	RESET = "\033[0m"
	RED = "\033[91m"
	GREEN = "\033[92m"
	YELLOW = "\033[93m"
	BLUE = "\033[94m"
	MAGENTA = "\033[95m"
	CYAN = "\033[96m"
		
def FlashText(text, duration=2):
	colors = [Color.RED, Color.GREEN, Color.YELLOW, Color.BLUE, Color.MAGENTA, Color.CYAN]
	interval = 0.1  # Flashing interval in seconds
	iterations = int(duration / interval)

	for _ in range(iterations):
		sys.stdout.write("\r" + " " * len(text))
		sys.stdout.flush()
		time.sleep(interval)

		color = random.choice(colors)
		colored_text = f"{color}{text}{Color.RESET}"
		sys.stdout.write("\r" + colored_text)
		sys.stdout.flush()
		time.sleep(interval)
	
	sys.stdout.write("\r" + " " * len(text) + "\n")
	sys.stdout.flush()