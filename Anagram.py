# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 14:41:32 2019

@author: Anirban
"""

ans=1

str1 = "test"
str2 = "trse"

str1_l = list(str1)
str2_l = list(str2)

n1 = len(str1_l)
n2 = len(str2_l)

if(n1!=n2):
    ans=0

dic = {}

for i in range(len(str1_l)):
    dic[str1_l[i]] = dic.get(str1_l[i], 0)+1
    

for i in range(len(str2_l)):
    if(dic.get(str2_l[i],0)!=0):
        dic[str2_l[i]] -= 1
        if(dic[str2_l[i]]<0):
            ans=0
    else:
        ans = 0
 
print(ans)