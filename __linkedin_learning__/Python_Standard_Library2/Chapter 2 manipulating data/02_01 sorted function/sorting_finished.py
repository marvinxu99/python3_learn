# using the built-in sorted function to sort data content

testScores = [82, 67, 94, 73, 79, 86, 58, 91, 89, 71, 88, 77, 84]

# perform a simple sort using sorted()
sortedScores = sorted(testScores)
print(sortedScores)


# explicitly declare a sort order - ascending and descending
sortedScores = sorted(testScores, reverse=True)
print(sortedScores)
