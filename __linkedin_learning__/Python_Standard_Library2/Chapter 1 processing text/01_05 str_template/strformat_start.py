# String formatting methods and best practices

# https://docs.python.org/3.8/tutorial/inputoutput.html#fancier-output-formatting

"""
string interpolation, also variable substitution or variable interpolation.
"""


from string import Template
import datetime

# TODO: Using Template strings
the_str = "The quick brown $animal $action over the lazy dog"
the_template = Template(the_str)
output_str = the_template.substitute(animal='fox', action='jumps')
print(output_str)

args = {
    'animal': 'cow',
    'action': 'walked'
}
output_str = the_template.substitute(args)
print(output_str)


# TODO: Using str.format()
foo = "foo"
bar = 123
print("output: {} {}".format(foo, bar))
print("output: {1} {0}".format(foo, bar))
print("output: {var1} {var2}".format(var1=foo, var2=bar))
print("output: {var2:x}, {var2:X}, {var1}".format(var1=foo, var2=bar))

# TODO: Using interpolation with f-strings in Python 3.6
product = "Widget"
price = 19.99
tax = 0.07
nyd = datetime.datetime(2020,1,1)

print(f"{product} has a price of {price}, with tax {tax:.2%}, the total is {round(price *(1+tax), 2)}")
print(f"But only on {nyd:%d %B %Y}")