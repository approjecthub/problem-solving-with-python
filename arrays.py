# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 00:39:10 2019

@author: Anirban
"""

all_items = ['x1', 'x2', 'x3', 'x4']
all_item_prices = [10.2, 25.69, 10.15, 14.3]

items = ['x2', 'x4', 'x1']
prices = [25.69, 14.3, 10.3]

def check(all_items=all_items, all_item_prices=all_item_prices, items=items, prices=prices):
    ans = 0
    for i in range(len(items)):
        for j in range(len(all_items)):
            
            if(items[i]==all_items[j]):
                try:
                    if(prices[i] != all_item_prices[j]):
                        ans += 1
                        break
                    else:
                        continue
                except:
                    print('i: ',i)
                    print('j: ', j)
            else:
                continue
    
    return ans
                
                