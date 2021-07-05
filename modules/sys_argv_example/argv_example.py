import sys

# Print arguments
print("Number of arguments:", len(sys.argv))
print("Arguments:", sys.argv)

# Remove arguments
sys.argv.remove(sys.argv[0])

print("Arguments:", sys.argv)

# Sum up the arguments:
sum = sum([int(x) for x in sys.argv])
print(sum)