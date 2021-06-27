with open('text_file.txt') as f:
    print(f.readline())
    print(f.readline())


f1 = open('text_file.txt')
print(f1.readlines())

f1.close()

####
def main():
    f = open('lines.txt', "r")
    print(type(f))
    print(f'mode is {f.mode}')
    for line in f:
        print(line.rstrip())



if __name__ == "__main__":
    main()