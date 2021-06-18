# def contains_digit(input_str):
#     for char in input_str:
#         if char.isdigit():
#             return True
#     return False

def contains_digit(input_str):
    return any(char.isdigit() for char in input_str)

assert contains_digit('This sentence does not contain any digits') == False
assert contains_digit('But th15 0ne d0e5') == True
assert contains_digit('123-456-7890') == True
print('Passed all tests ...')

def contains_punctuation(input_str):
    '''
    return True if the input_str contains punctuations.
    return False otherwise 
    '''
    pun_chars = [',', '.', ';', '?', '!']
    return any(char in pun_chars for char in input_str )

assert contains_punctuation('This sentence does not contain any digits') == False
assert contains_punctuation('Sentence one; Sentence two') == True
assert contains_punctuation('123-456-7890') == False
print('Passed all tests ...')
