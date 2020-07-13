# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:52:04 2020

@author: Anirban
"""

###https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/

start = [10, 12, 20]
finish = [20, 25, 30]

ts = finish[0]
ans = []
ans.append(0)

for i in range(1, len(start)):
    if start[i]>=ts:
        ts = finish[i]
        ans.append(i)
        
print(ans)