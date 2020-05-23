found = False
for thing in things:
    if thing == other_thing:
        found = True
        break
        
found = any(thing == other_thing for thing in things)

'''
any() will return True when at least one of the elements evaluates to True, 
all() will return True only when all the elements evaluate to True.
'''