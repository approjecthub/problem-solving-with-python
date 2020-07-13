# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 16:32:18 2019

@author: Anirban
"""

def pair(ar,k):
    ar.sort()
    i=0
    j=len(ar)-1
    ans = []
    while i<j:
        if (ar[i]+ar[j])==k:
            if {ar[i],ar[j]} not in ans:
                ans.append({ar[i],ar[j]})
            j-=1
            
        elif (ar[i]+ar[j])<k:
            i += 1
        else:
            j -= 1
            
    return ans

def driver():
    ar =  [1, 2,1, 4,3]
    k=4
    ans = pair(ar,k)
    print(ans)
        
        
        