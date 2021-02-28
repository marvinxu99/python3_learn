import csv
import itertools


meows_data = []
with open("interp_audit_1.csv", newline='') as f:
    reader = csv.reader(f)
    meows_data = list(reader)

meows_output = []
for data in meows_data:
    text = ''.join(x for x in data)
    data.append(str(text.count("Red")))
    meows_output.append(data)

with open('meows_output.csv', 'w+', newline='') as f_csv:
    writer = csv.writer(f_csv) 
    writer.writerows(meows_output)

print(len(meows_output))

