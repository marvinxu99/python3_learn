import sys
import random

if len(sys.argv) != 3:
    print("Please enter two range numbers.")
else:
    lower = int(sys.argv[1])
    upper = int(sys.argv[2])
    my_random = random.randint(lower, upper)

    while True:
        guess = input("What is the number in my mind, enter 'q' to quit ?")

        if guess == "q":
            break
        try:
            if int(guess) == my_random:
                print("bingo")
            else:
                print(f"that is not what I was thinking({my_random})")
        except ValueError:
            print("please enter numbers.")

    print("thanks for playing")

