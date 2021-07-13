# Functions for generating random data sequences
import random
import string

# TODO: Use the choice function to randomly select from a sequence
moves = ["rock", "paper", "scissors"]
print(random.choice(moves))

# TODO: Use the choices function to create a list of random elements
roulette_wheel = ["black", "red", "green"]
print(random.choices(roulette_wheel, k=10,))

# Assign weights to elements
weights = [18, 18, 2]
print(random.choices(roulette_wheel, weights, k=10))

# TODO: The sample function randomly selects elements from a population
# without replacement (the chosen items are not replaced)
chosen = random.sample(string.ascii_letters, 6)
print(chosen)

# TODO: The shuffle function shuffles a sequence in place
players = ["Bill", "Jane", "Joe", "Sally", "Mike", "Lindsay"]
random.shuffle(players)
print(players)

# TODO: to shuffle an immutable sequence, use the sample function first
result = random.sample(string.ascii_uppercase, k=len(string.ascii_uppercase))
random.shuffle(result)
print(''.join(result))