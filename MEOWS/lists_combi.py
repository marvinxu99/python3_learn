import csv
import itertools


'''
a = ['a1', 'a2']
b = ['b1', 'b2']
c = ['c1', 'c2']
d = ['d1', 'd2']
e = ['e1', 'e2']
f = ['f1', 'f2']
g = ['g1', 'g2']
'''
# # for Yellows
# a = ['A != 1', 'A = 1']
# b = ['B != 1', 'B = 1']
# c = ['C != 1', 'C = 1']
# d = ['D != 1', 'D = 1']
# e = ['E != 1', 'E = 1']
# f = ['F != 1', 'F = 1']
# g = ['G != 1', 'G = 1']

# # for Reds
a = ['A != 2', 'A = 2']
b = ['B != 2', 'B = 2']
c = ['C != 2', 'C = 2']
d = ['D != 2', 'D = 2']
e = ['E != 2', 'E = 2']
f = ['F != 2', 'F = 2']
g = ['G != 2', 'G = 2']

lists = [a, b, c, d, e, f, g]
combs = list(itertools.product(*lists))


new_combs = []
for comb in combs:
    cmb = list(comb)
    text = ''.join(x for x in cmb)
    cmb.append(str(7 - text.count("!= 2")))
    new_combs.append(cmb)

#print(new_combs)

f_csv = open('listcombi.csv', 'w+', newline='')
with f_csv:
    write = csv.writer(f_csv) 
    write.writerows(new_combs)

print(len(new_combs))

