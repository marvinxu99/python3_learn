import csv
from datetime import datetime
from collections import namedtuple
import functools as ft
import itertools as it


class DataPoint(namedtuple('DataPoint', ['date', 'value'])):
    __slots__ = ()

    def __le__(self, other):
        return self.value <= other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value


def read_prices(csvfile, _strptime=datetime.strptime):
    with open(csvfile) as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            yield DataPoint(date=_strptime(row['Date'], '%Y-%m-%d').date(),
                            value=float(row['Adj Close']))


prices = tuple(read_prices('sp500.csv'))

gains = tuple(DataPoint(day.date, 100*(day.value/prev_day.value - 1.))
              for day, prev_day in zip(prices[1:], prices))

# print(gains[0].value)
zdp = DataPoint(None, 0)   # zero DataPoint
max_gain = ft.reduce(max, it.filterfalse(lambda p: p <= zdp, gains))
max_loss = ft.reduce(min, it.filterfalse(lambda p: p > zdp, gains), zdp)

# Display results.
print('Max gain: {1:.2f}% on {0}'.format(*max_gain))
print('Max loss: {1:.2f}% on {0}'.format(*max_loss))
