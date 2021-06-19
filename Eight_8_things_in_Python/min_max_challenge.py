import string
from functools import reduce

DICTIONARY = 'dictionary.txt'

letter_scores = {
                    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 
                    'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 
                    'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 
                    'y': 4, 'z': 10
                }

def get_scrabble_dictionary():
    """Helper function to return the words in DICTIONARY as a list"""
    with open(DICTIONARY, 'rt', encoding='utf-8') as file:
        content = file.read().splitlines()
    return content

def score_word(word):
    """Return the score for a word using letter_scores.
    If the word isn't in DICTIONARY, it gets a score of 0."""
    word_score = 0 
    if word.upper() in get_scrabble_dictionary():
       word_score = reduce(lambda x, y: x + letter_scores[y], word.lower(), 0)
    return word_score

def remove_punctuation(word):
    """Helper function to remove punctuation from word"""
    table = str.maketrans({char:None for char in word if char in string.punctuation})
    return word.translate(table)

def get_word_largest_score(sentence):
    """Given a sentence, return the word in the sentence with the largest score."""
    words_in_sentence = sentence.split()
    words_cleaned = list(map(remove_punctuation, words_in_sentence))
    word_largest_score = max(words_cleaned, key=score_word)
    return word_largest_score

if __name__ == "__main__":
    
    words_in_dict = get_scrabble_dictionary()

    while(True):
        inp_word = input("Enter a word, or enter CRL+C to exit: ")
        print("You entered: " + inp_word)
        print(score_word(inp_word))

    # print(get_word_largest_score("Beautiful is better than ugly."))