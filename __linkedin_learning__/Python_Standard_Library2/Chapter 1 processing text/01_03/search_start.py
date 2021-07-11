# Use standard library functions to search strings for content


sampleStr = "The quick brown fox jumps over the lazy dog"

# TODO: startsWith and endsWith functions
print(sampleStr.startswith("The"))
print(sampleStr.startswith("the"))
print(sampleStr.endswith("dog"))

# TODO: the find and rfind functions
print(sampleStr.find("the"))
print(sampleStr.rfind("the"))

print("the" in sampleStr)

# TODO: using replace
newStr = sampleStr.replace("lazy", 'tired')
print(newStr)

# TODO: counting instances of substrings
print(sampleStr.count('over'))