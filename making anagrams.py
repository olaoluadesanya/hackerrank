'''
   problem can be found here : 
   
   https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
   
   My approach is to create a hash map for the longer string
   with integers as the number of occurence of each character.
   This integer is then decremented for every match in the 
   shorter string. the sum of remaining integers plus every 
   'non-match' in the shorter string gives us the minumum number
   of deletions to create an anagram.
   
   time complexity = log(n)
'''

def number_needed(a, b):
    
    ola = dict()
    count_n = 0
    if len(a) >= len(b):
        for i in a:
            ola[i] = a.count(i)
        for j in b:
            if j in ola:
                ola[j] -= 1
            else:
                count_n += 1
        for c, d in ola.items():
            # abs is used here because the shorter string might contain too
            # many occurences of character and the integer might be plunged
            # into negative.
            
            count_n += abs(d)
    
                
    else:
        for j in b:
            ola[j] = b.count(j)
        for i in a:
            if i in ola:
                ola[i] -= 1
            else:
                count_n += 1
        for c, d in ola.items():
            count_n += abs(d)
    
    return count_n


a = input().strip()
b = input().strip()

print(number_needed(a, b))
