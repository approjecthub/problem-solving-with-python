# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:50:45 2019

@author: Anirban
"""
a = 123
"""

li = list(str(a))

rev = ""

for i in range(len(li)):
    rev += li[-(i+1)]
    
print(rev)

"""
# ----------------------C style----------------------------------------
div = 0
rem = 0
while True:
    t = a%10
    rem = rem*10 + t
    a = a//10
    
    if(a==0):
        break