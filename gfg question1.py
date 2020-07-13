# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:31:35 2020

@author: Anirban
"""

'''
Build Lowest Number by Removing n digits from a given number

https://www.geeksforgeeks.org/build-lowest-number-by-removing-n-digits-from-a-given-number/
'''

s = '4325043'
n = 3

dig = len(s)-n

ans = ['']*dig

start = 0
end = 0

for i in range(dig):
    end = len(s)-dig+i
    temp = '10'
    #print('start',start,'end', end, 'temp', temp)
    for j in range(start, end+1):
        #print('s[j]', s[j])
        if int(s[j])<int(temp):
            
            temp = s[j]
            start = j+1
            #print('temp ', temp)
            
    ans[i] = temp
    #print('ans ', ans[i])
   
print(ans)