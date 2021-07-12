# Use standard library functions to search strings for content


sampleStr = "The quick brown fox jumps over the lazy dog"

# startsWith and endsWith functions
print(sampleStr.startswith("The"))
print(sampleStr.startswith("the"))
print(sampleStr.endswith("dog"))


# the find and rfind functions
print(sampleStr.find("the"))
print(sampleStr.rfind("the"))
print("the" in sampleStr)


# using replace
newStr = sampleStr.replace("lazy", "tired")
print(newStr)


# counting instances of substrings
print(sampleStr.count("over"))
