countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
population = [17_500_000, 198_000_000, 10_000_000, 30_000_000, 24_000_000, 128_000_000]

print(max(population))
print(min(countries))
'''
198000000
Japan
'''
'''
Tuple comparision
Compare the corresponding items of each tuple.
If they are the same, move on to the next item
''' 
countries_population = list(zip(countries, population))
print(min(countries_population))
# ('Japan', 128000000)   - only countries are compared

# to compare the popluation, can use the key parameter
def get_population(pair):
    _, population = pair
    return population

print(min(countries_population, key=get_population))
'''('Jordan', 10000000)'''

# Use lambda function
print(min(countries_population, key=lambda x: x[1]))
'''('Jordan', 10000000)'''

# another way to zip (population, country) instead of (country, population)
print(min(zip(population, countries))) 
'''(10000000, 'Jordan')'''

