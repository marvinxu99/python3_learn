'''
sorted(iterable, *, key=none, reverse=False)
'''

class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population    
    def __repr__(self):
        return f'Country({self.name}, {self.population})'

country_list = [
                Country('Taiwan', 24_000_000),
                Country('Portugal', 10_000_000), 
                Country('Netherlands', 17_500_000), 
                Country('Nigeria', 198_000_000), 
                Country('Jordan', 10_000_000), 
                Country('Nepal', 30_000_000), 
                Country('Niger', 24_000_000), 
                Country('Japan', 128_000_000)
]

#print(sorted(country_list, key=lambda x: x.population, reverse=True), sep="\n")
print(*sorted(country_list, key=lambda x: x.population, reverse=True), sep="\n")
'''
Country(Nigeria, 198000000)
Country(Japan, 128000000)     
Country(Nepal, 30000000)      
Country(Taiwan, 24000000)     
Country(Niger, 24000000)      
Country(Netherlands, 17500000)
Country(Portugal, 10000000)
Country(Jordan, 10000000)
'''
print('-----------------')
print(*sorted(country_list, key=lambda x: (-x.population, x.name)), sep='\n')
'''
Country(Nigeria, 198000000)
Country(Japan, 128000000)
Country(Nepal, 30000000)
Country(Niger, 24000000)
Country(Taiwan, 24000000)
Country(Netherlands, 17500000)
Country(Jordan, 10000000)
Country(Portugal, 10000000)
'''

iso = [
    ('Taiwan', 'iso24000000'), 
    ('Portugal', 'iso10000000'), 
    ('Netherlands', 'iso17500000'), 
    ('Nigeria', 'iso198000000'), 
    ('Jordan', 'iso10000000'), 
    ('Nepal', 'iso30000000'), 
    ('Niger', 'iso24000000'), 
    ('Japan', 'iso128000000')
]

def get_population(pair):
    _, population = pair
    return int(population[3:])

print('-----------------')
print(*sorted(iso, key=get_population), sep="\n")
'''
('Portugal', 'iso10000000')
('Jordan', 'iso10000000')
('Netherlands', 'iso17500000')
('Taiwan', 'iso24000000')
('Niger', 'iso24000000')
('Nepal', 'iso30000000')
('Japan', 'iso128000000')
('Nigeria', 'iso198000000')
'''

def get_sorted(pair):
    country, population = pair
    return (int(population[3:]), country)

print('-----------------')
print(*sorted(iso, key=get_sorted), sep="\n")
'''
('Jordan', 'iso10000000')
('Portugal', 'iso10000000')
('Netherlands', 'iso17500000')
('Niger', 'iso24000000')
('Taiwan', 'iso24000000')
('Nepal', 'iso30000000')
('Japan', 'iso128000000')
('Nigeria', 'iso198000000')
'''
