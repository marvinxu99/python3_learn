import itertools
a = ['a1', 'a2']
b = ['b1', 'b2']
c = ['c1', 'c2']
d = ['d1', 'd2']
e = ['e1', 'e2']
f = ['f1', 'f2']
g = ['g1', 'g2']
h = ['h1', 'h2']
i = ['i1', 'i2']
j = ['j1', 'j2']

lists = [a, b, c, d, e, f, g, h, i, j]

combs = list(itertools.product(*lists))

for comb in combs:
    print(comb)

print(len(combs))
