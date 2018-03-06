'''problem statement can be found here:
    
   https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem


   it is essentially rotating an array a of size n to the left by k number of times
'''



from collections import deque

def array_left_rotation(a, n, k):
    queue = deque(a) # deque is more efficient for FIFO operations
    i = 0
    while i < k:
       queue.append(queue.popleft())
       i += 1
    return queue
                

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')

