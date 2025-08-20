# Learn-by-heart
Memorise anything very fast!

Sorry, this is a very crude script. 

## How it works
This is a small program to help us memorise passages/Q&A word-for-word by simply reading them ~6 to 7 times. The program obscures the text more and more as the levels get harder, so that in the act of reading, your brain automatically learns it. 

## How to use
All you need is Python - I use only built-in libraries. I am using Python 3.9.1, but you can probably get along with a much lower version. Choose which file to run depending on your needs.

1. python PassageFull.py <i>inputfile</i>
    <i>inputfile</i> should be a plaintext file containing a passage. The program shows the whole passage at once, obscuring it at more progressive levels. At each level, type what you think is the correct passage, and the program will show you a diff.
2. python QnA.py <i>inputfile</i>
    <i>inputfile</i> should be a plaintext file having questions and answers in alternate lines separated by a newline. Empty lines will be ignored. The program will show the question and an obscured version of the answer. Type what you think the correct answer is, and the program will show you a diff
3. python Repetition.py <i>inputfile</i>
    <i>inputfile</i> should be a plaintext file having several lines of text. The program asks one line at a time.
4. python RepetitionQnA.py <i>inputfile</i>
    Similar to QnA.py, but you can choose whether to repeat a question later or not.
5. python Passage.py <i>inputfile</i>
    Disregards all newlines in <i>inputfile</i> and considers the text as a single passage, but it shows one line at a time.


