# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:17:12 2019

@author: Anirban
"""

'''
Count of unique pairs (arr[i], arr[j]) such that i < j
Given an array arr[], the task is to print the count of unique pairs (arr[i], arr[j]) such that i < j.
https://www.geeksforgeeks.org/count-of-unique-pairs-arri-arrj-such-that-i-j/

'''

#arr = [ 1, 2, 2, 4, 2, 5, 3, 5]
arr = [1, 2, 1, 4, 5, 2]
 
'''
dic = dict()
i=0
for j in range(1,len(arr)):
    dic[(arr[i], arr[j])] = dic.get((arr[i], arr[j]),0)+1   #pairwise-> not desired
    #dic[frozenset((arr[i], arr[j]))] = dic.get(frozenset((arr[i], arr[j])),0)+1   #pairwise-> not desired
    i+=1

print(len(dic))
'''

visited1 = set()
visited2 = set()

n = len(arr)
uniq = [0]*n

uniq[n-1] = 0
cnt = 0

for i in range(n-1,0,-1):
    if arr[i] in visited1:
        uniq[i-1] = cnt
    else:
        cnt += 1
        uniq[i-1] = cnt
        visited1.add(arr[i])
        
ans = 0
for i in range(n):
    if arr[i] in visited2:
        continue
    else:
        ans += uniq[i]
    
        visited2.add(arr[i])
        
print(ans)

