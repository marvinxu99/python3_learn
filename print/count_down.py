'''
Buffering Print Calls:
The os buffers subsequent writes to the standard output in this case. 
You need to know that there are three kinds of streams with respect to buffering:
- Unbuffered
- Line-buffered
- Block-buffered
'''

import time

num_seconds = 3
for countdown in reversed(range(num_seconds + 1)):
    if countdown > 0:
#        print(countdown, end='...')
        print(countdown, end='...', flush=True)
        time.sleep(1)
    else:
        print('Go!')

'''
o fix it, you can simply tell print() to forcefully flush the 
stream without waiting for a newline character in the buffer using its flush flag
'''