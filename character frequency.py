# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:29:41 2019

@author: Anirban
"""

### Frequency of each character in String
  
def logic1(test_str = "GeeksforGeeks"):  
    from collections import Counter 
    res = Counter(test_str) 
    
    #print ('logic-1 :\n',res)
    return res


##  ------------- logic 2 -------------------
    
def logic2(test_str = "GeeksforGeeks"):   
    res_dic = {}
    
    for i in test_str:
        res_dic[i] = res_dic.get(i,0) + 1
        
    #print('logic-2 :\n', res_dic)
    return res_dic
    
    
from timeit import default_timer as timer

start = timer()
logic1()
end = timer()
print('logic1 took : ',(end - start)*10**6)

start = timer()
logic2()
end = timer()
print('logic2 took : ',(end - start)*10**6)

