# Working with string manipulation functions

test_string1 = "The quick brown fox jumps over the lazy dog on the 1st of December"

# upper and lower convert between cases
print(test_string1.upper())
print(test_string1.lower())


# Use the split and join functions
result = test_string1.split(" ")
print(result)

letters = ["a", "b", "c", "d", "e"]
print(", ".join(letters))


# use justification functions to align strings
# ljust, center, rjust
names = ["Amy", "John", "George", "Michael", "Penelope"]
biggest = max(len(name) for name in names)

for name in names:
    print(name.ljust(biggest+2, "-") + ":")
print()
for name in names:
    print(name.center(biggest+2, "-") + ":")
print()
for name in names:
    print(name.rjust(biggest+2, "-") + ":")


# Use a translation table to replace characters
sample_str = "The quick brown fox jumped over the lazy dog"

trans_table = str.maketrans("abegilostz", "4636110572")
print(sample_str)
print(sample_str.translate(trans_table))
