# String formatting methods and best practices
from string import Template


# TODO: Using Template strings
the_str = "The quick brown $animal $action over the lazy dog"
# the_template = Template(the_str)
# output_str = the_template.substitute(animal="fox",action="jumped")
# print(output_str)
# args = {
#     "animal":"cow",
#     "action":"walked"
# }
# output_str = the_template.substitute(args)
# print(output_str)

# TODO: Using str.format()
foo = "foo"
bar = 123
print("Output: {}, {}".format(foo,bar))
print("Output: {1}, {0}".format(foo,bar))
print("Output: {var1}, {var2}".format(var1=foo,var2=bar))
print("Output: {var2:x}, {var2:X}, {var1}".format(var1=foo,var2=bar))


# TODO: Using interpolation with f-strings in Python 3.6
product = "Widget"
price = 19.99
tax = 0.07
