def count_down(x):
    if x == 0:
        print('done!')
        return
    else:
        print(x, '...')
        count_down(x-1)
        print("foo")

count_down(10)