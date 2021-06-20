import re

def remove_punctuation(words):
    '''Helper function to return a string, removing all punctuations and spaces'''
    return re.sub('\W+', '', words)

def is_palindrome(words):
    '''Palindromes are case insensitive, so both radar and Radar are valid'''
    cl_words = remove_punctuation(words).lower()
    return (cl_words == "".join(reversed(cl_words)))   
    # return (cl_words == cl_words[::-1])

if __name__ == "__main__":
    print(f"radar is palindrome: { is_palindrome('radar')}")
    print(is_palindrome('radar'))
