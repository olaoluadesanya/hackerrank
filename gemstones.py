#!/bin/python3

'''
Proble, can be found here:
https://www.hackerrank.com/challenges/gem-stones/problem
This is my brute force solution. Could easily implement a
hash so there's no inner loop. Did pass all the test cases
though so this works just fine
'''

import sys

def gemstones(arr):
    count_gem = []
    final_count = 0
    for i, j in enumerate(set(arr[0])):
        count_gem.append(0)
        
        for k in range(1, len(arr)):
            #print(arr[k].find(j))
            if arr[k].find(j) >= 0:
                count_gem[i] += 1
    for l in count_gem:
        if l == (len(arr) - 1):
            final_count += 1
    return final_count

                

n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
   arr_t = str(input().strip())
   arr.append(arr_t)
result = gemstones(arr)
print(result)

