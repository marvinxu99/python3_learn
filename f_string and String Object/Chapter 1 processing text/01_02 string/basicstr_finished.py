# use predefined string constants
import string


# predefined string constants can be used in common scenarios
print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.punctuation)

# Use the constants to filter information out
test_string1 = "The quick brown fox jumps over the lazy dog on the 1st of December"
test_string2 = "Supercalifragilistic"
test_string3 = "90210"

result = "".join([c for c in test_string1 if c in string.ascii_letters])
print(result)

# String testing methods
print(test_string1.isalnum())
print(test_string2.isalpha())

print(any([c.isalpha() for c in test_string1]))

print(test_string3.isnumeric())
