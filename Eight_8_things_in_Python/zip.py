'''
zip(*iterables)

Expected output:
The capital city of Netherlands is Amsterdam
The capital city of Nigeria is Abuja
The capital city of Jordan is Amman
The capital city of Nepal is Kathmandu
The capital city of Niger is Niamey
The capital city of Japan is Tokyo
'''

countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
capitals = ['Amsterdam', 'Abuja', 'Amman', 'Kathmandu', 'Niamey', 'Tokyo']

for country, capital in zip(countries, capitals):
    print(f'The capital city of { country } is { capital }')


countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
capitals = ['Amsterdam', 'Abuja', 'Amman', 'Kathmandu']

for country, capital in zip(countries, capitals):
    print(f'The capital city of { country } is { capital }')

'''
The capital city of Netherlands is Amsterdam
The capital city of Nigeria is Abuja
The capital city of Jordan is Amman
The capital city of Nepal is Kathmandu
'''
from itertools import zip_longest

for country, capital in zip_longest(countries, capitals, fillvalue='unknown'):
    print(f'The capital city of { country } is { capital }')

'''
The capital city of Netherlands is Amsterdam
The capital city of Nigeria is Abuja
The capital city of Jordan is Amman
The capital city of Nepal is Kathmandu
The capital city of Niger is unknown
The capital city of Japan is unknown
'''

countries = ['Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan']
capitals = ['Amsterdam', 'Abuja', 'Amman', 'Kathmandu']

pairs = list(zip(countries, capitals))
'''
[('Netherlands', 'Amsterdam'), ('Nigeria', 'Abuja'), ('Jordan', 'Amman'), ('Nepal', 'Kathmandu')]
'''

# to unzip
countries_2, capitals_2 = zip(*pairs)
'''
>>> countries_2
('Netherlands', 'Nigeria', 'Jordan', 'Nepal', 'Niger', 'Japan')
>>> capitals_2
('Amsterdam', 'Abuja', 'Amman', 'Kathmandu', 'Niamey', 'Tokyo')
'''