'''Problem statement found here:
    https://www.hackerrank.com/challenges/alternating-characters/problem
    runs in O(n) time
'''


#!/bin/python3

import sys

def alternatingCharacters(s):
    counter = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            counter += 1
    return counter

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)
