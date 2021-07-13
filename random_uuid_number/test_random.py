import random

print(random.random())

# randrange
decider =  random.randrange(2)
print(decider)   # possible values: 0, 1

print(random.randrange(1, 7))

# randint
print(random.randint(10, 20))

# Select a random item from a list
foo = ['a', 'b', 'c', 'd', 'e']
print(random.choice(foo))

lotteryWinners = random.sample(range(100), 5) 
print(lotteryWinners)

possiblePets = random.choice(['cat', 'fish', 'dog'])
print(possiblePets)

# For cryptographically secure random choices (e.g. for generating a passphrase from a wordlist) 
# use secrets.choice()
import secrets

foo = ['battery', 'correct', 'horse', 'staple']
print(secrets.choice(foo))

"""
If you want to randomly select more than one item from a list, or select an 
item from a set, I'd recommend using random.sample instead.
"""
# group_of_items = {'a', 'b', 'c', 'd', 'e'}  # a sequence or set will work here.
# num_to_select = 2                           # set the number to select here.
# list_of_random_items = random.sample(group_of_items, num_to_select)
# first_random_item = list_of_random_items[0]
# second_random_item = list_of_random_items[1] 
first_random_item, second_random_item = random.sample({'a', 'b', 'c', 'd', 'e'}, 2)
print(first_random_item, second_random_item)