# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 08:37:07 2019

@author: Anirban
"""

'''
You are given a list of n-1 integers and these integers are in the range of 1 to n. 
There are no duplicates in the list. One of the integers is missing in the list. 
Write an efficient code to find the missing integer.
'''


arr=[1, 2, 3, 5, 6]
n = len(arr)+1

sum_n = n*(n+1)//2
sum_arr = sum(arr)

print(sum_n-sum_arr)

### ------------------------XOR technique------------------------


ans = 0
for i in range(1,len(arr)+2):
    ans ^= i
for i in range(len(arr)):
    ans ^= arr[i]
    
print(ans)