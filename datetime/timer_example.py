import time

# run = input("Start? (type yes to start) >")
run = 'yes'

seconds = 0

if run == "yes":
    while seconds != 10:
        print('>', seconds)
        time.sleep(1)
        seconds += 1


#####################################
# time.process_time()
from time import process_time
start = process_time()  

for r in range(2000):
    print(r, end=" ")

end = process_time()
print()
print(end, start)
print(end-start)

##############################################
from time import perf_counter, sleep

n = 10
start = perf_counter()  

for r in range(n): 
    sleep(1)

end = perf_counter() 

print('start=', start, 'end=', end)
print(end-start)