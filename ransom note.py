'''the problem statement can be found here:
    https://www.hackerrank.com/challenges/ctci-ransom-note/problem
'''
# My naive solution would run in 2(n^n) time as 'count' has to happen 
# for every member of magazine.
def ransom_note(magazine, ransom):
    table = dict()

    for j in magazine:
        table[j] = magazine.count(j)
        # a work around would be to loop around set(magazine) to reduce the time
	# as we only need consider the first occurrence of each element

    for j in ransom:
        if table[j] < 1:
            return False
        table[j] -= 1
            
    return True

#Or better still only loop through once by using a counter initiated dictionary
#This runs in 2n time
'''
from collections import defaultdict

def ransom_note(magazine, ransom):
    table = defaultdict(int)

    for j in magazine:
        table[j] += 1
    for j in ransom:
        if table[j] < 1:
            return False
        table[j] -= 1
            
    return True
    
# Shorter code  but runs in the same 2n time
from collections import Counter

def ransom_note(magazine, ransom):
    
    return not (Counter(ransom) - Counter(magazine))
 '''   
#input and output code:


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    

