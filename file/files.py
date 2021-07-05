"""
w --> write
r --> read
r+ --> read and write
a --> append
"""

with open('text_file.txt', 'r') as f:
    print(f.readline())
    print(f.readline())


f1 = open('text_file.txt', 'r+')
print('File Name:', f1.name)
print('mode:', f1.mode)
print(f1.readlines())
f1.close()

with open('text_file2.txt', 'w') as f2:
    f2.write("test, test")

with open('text_file2.txt', 'r+') as f3:
    for line in f3:
        print(line)
        new_line = line.replace('test', 'tttt')
        print(new_line)
'''
test, test
tttt, tttt
'''

"""
seek() as needed to reset the pointer
"""


####
def main():
    f = open('lines.txt', "r")
    print(type(f))
    print(f'mode is {f.mode}')
    for line in f:
        print(line.rstrip())



if __name__ == "__main__":
    main()