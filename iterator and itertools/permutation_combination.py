import itertools

# Permutatuons
election = {1: 'Barb', 2: 'Karen', 3: "Erin", 4: "Bob"}
# possible_coutcomes = list(itertools.permutations(election))
# for p in possible_coutcomes:
#     print(p, end='\n')
for p in itertools.permutations(election.values()):
    print(p, end='\n')

# Combinations 
colorsForPainting = ['red', 'blue', 'purplse', 'yellow', 'pink', 'orange']
for c in itertools.combinations(colorsForPainting, 2):
    print(c)

