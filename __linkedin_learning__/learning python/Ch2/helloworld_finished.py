#
# Example file for HelloWorld
#

def main():
    print("hello world!")
    name = input("What is your name? ")
    print("Nice to meet you,", name)

if __name__ == "__main__":
    main()


def multi_add(*args):
    result = 0
    for x in args:
        result += x
    return result

