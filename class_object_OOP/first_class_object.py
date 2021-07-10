stock = "GOOG, 100, 20.3"
field_types = [str, int, float]
split_stock = stock.split(',')

print(split_stock)

stock_format = [ty(val) for ty, val in zip(field_types, split_stock)]

print(stock_format)