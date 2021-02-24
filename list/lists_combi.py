import csv
import itertools


a = ['a1', 'a2']
b = ['b1', 'b2']
c = ['c1', 'c2']
d = ['d1', 'd2']
e = ['e1', 'e2']
f = ['f1', 'f2']
g = ['g1', 'g2']

lists = [a, b, c, d, e, f, g]
combs = list(itertools.product(*lists))

f_csv = open('listcombi.csv', 'w+', newline='')

new_combs = []
for comb in combs:
    cmb = list(comb)
    

with f_csv:
    write = csv.writer(f_csv) 
    write.writerows(combs)
        
print(len(combs))
