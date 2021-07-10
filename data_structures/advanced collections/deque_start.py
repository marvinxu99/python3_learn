# deque objects are like double-ended queues

import collections
import string


def main():
    
    # TODO: initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)

    # TODO: deques support the len() function
    print("Item count:", len(d))

    # TODO: deques can be iterated over
    for elem in d:
        print(elem.upper(), end=',') 
    print()

    '''
    Item count: 26
    A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,
    '''

    # TODO: manipulate items from either end
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(d)

    # TODO: rotate the deque
    d.rotate(10)
    print(d)


if __name__ == "__main__":
    main()
