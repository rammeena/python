#d.py
# Word Values 
"""
Calculate the dictionary word that would have the most value in Scrabble
(https://en.wikipedia.org/wiki/Scrabble). Follow the methods. 

- 1. First write a function to read in dictionary.txt (DICTIONARY constant) and return a list of word. 
- 2. Second write a function that receives a word and calculates its value. Use the scores stored in LETTER_SCORES. 
- 3. With these two pieces in place, write a third function that takes a list of words and returns the word with the highest
value.
"""
import os
import urllib

DICTIONARY = os.path.join('/tmp', 'dictionary.txt')

urllib.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")
                  ]
LETTER_SCORES = {letter: score for score,letters in scrabble_scores for letter in letters.split()}

def load_words():
    'load the words dictionary (DICTIONARY constant) into a list and return it'
    with open(DICTIONARY,'r') as d:
        return d.read().split()

def calc_word_value(word):
    'given a word calculate its value using LETTER_SCORES'
    value = 0
    for w in word:
        value += LETTER_SCORES[w.upper()]
    return value

def max_word_value(words=None):
    'given a list of words return the word with the maximum word value'
    values = {}
    if words:
        for word in words:
            values[word] = calc_word_value(word)
    else: 
        return False

    for k,v in 
test_words = ('bob', 'julian', 'pybites', 'quit', 'barbeque')
print(max_word_value(test_words))
