# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:16:43 2019

@author: Anirban
"""


### Count substrings with each character occurring at most k times
### https://www.geeksforgeeks.org/count-substrings-character-occurring-k-times/

def counter(test_str):   
    res_dic = {}
    
    for i in test_str:
        res_dic[i] = res_dic.get(i,0) + 1
    return res_dic

def print_substring(word):
    
    l = 0
    all_ss = ['']*((len(word)*(len(word)+1))//2)
    for i in range(len(word)):
        for j in range(i, len(word)):
            for k in range(i,j+1):
                all_ss[l] += word[k]               
            l+=1
            
    return all_ss

def driver_1():
    a = 'aaabb'
    k = 2
    flag = True
    ans = 0
    sub_strings = print_substring(a)
    for i in sub_strings:
        ci = counter(i)
        for j in ci:
            if ci[j]>k:
                flag = False
        if flag:
            ans+=1
        flag = True
        
    return ans

def solution2():        ## O(N^2) solution
    a = 'aaabb'
    k=2
    
    s = list(a)
    ans = 0
    for i in range(len(s)):
        cnt = [0]*26
        for j in range(i, len(s)):
            cnt[ord(s[j]) - ord('a')] += 1
            
            if(cnt[ord(s[j]) - ord('a')]<=k):
                ans += 1
            else:
                break
    return ans
            
from timeit import default_timer as timer

start = timer()
driver_1()
end = timer()
print('logic1 took : ',(end - start)*10**6)

start = timer()
solution2()
end = timer()
print('logic2 took : ',(end - start)*10**6)