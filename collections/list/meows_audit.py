import csv
import itertools


meows_data = []
with open("interp_audit_1.csv", newline='') as f:
    reader = csv.reader(f)
    meows_data = list(reader)

meows_output = []
for data in meows_data:
    text = ''.join(x for x in data)
    red_count = text.count("Red")
    data.append(str(red_count))
    data.append("TRUE" if red_count == int(data[8]) else "FALSE")

    meows_output.append(data)

with open('meows_output.csv', 'w+', newline='') as f_csv:
    writer = csv.writer(f_csv) 
    writer.writerows(meows_output)

print(len(meows_output))

