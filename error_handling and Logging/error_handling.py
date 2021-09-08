# error handling #1
while True:
    try: 
        age = int(input('What is your age?'))
        10/age
        print(age)
        # raise Exception('Hey cut it out')
        # raise ValueError('Hey cut it out2')
    except ValueError: 
        print("please enter a number")
    except ZeroDivisionError: 
        print("please enter a number > 0")
    else:
        print('thank you!')
        break
    finally: 
        print('ok, i am finally done')

# error handling #2
def sum(num1, num2):
    try: 
        return num1/num2
#    except TypeError as err:
    except (TypeError, ZeroDivisionError) as err:
        print(f"enter numbers {err}")

print(sum('1', 2))


# example #3
import sys
file_name = sys.argv[1]
text = []
try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
else:
    text = fh.readlines()
    fh.close()

if text:
    print(text[100])
