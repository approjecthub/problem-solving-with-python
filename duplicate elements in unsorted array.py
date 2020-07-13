# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 08:51:44 2019

@author: Anirban
"""

'''
Given an array of n elements which contains elements from 0 to n-1, 
with any of these numbers appearing any number of times. 
Find these repeating numbers in O(n) and using only constant memory space.

For example, let n be 7 and array be {1, 2, 3, 1, 3, 6, 6}, the answer should be 1, 3 and 6.
'''

'''
#arr = [1, 2, 3, 1, 3, 6, 6]
arr = [1, 2, 3, 1, 3, 6, 6,6]

for i in range( len(arr)):
    if(arr[abs(arr[i])]<0):
        print(abs(arr[i]))
        
    else:
        arr[abs(arr[i])] = -arr[abs(arr[i])]
        
''' 
       
'''
There is a problem in above approach. It prints the repeated number more than once. 
For example: {1, 6, 3, 1, 3, 6, 6} it will give output as : 3 6 6. 
So, in this article, another method is discussed to overcome this problem.
'''

arr = [1, 2, 3,  3, 6, 6,6,3]
n=len(arr)
for i in range(n):
    arr[arr[i]%n]+= n
for i in range(n):
    if(arr[i]>2*n):
        print(i)
    