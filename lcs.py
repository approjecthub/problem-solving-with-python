def lcs(s1, s2):
    
    temp = [[0]*(len(s2)+1)]*(len(s1)+1)
    maxm = 0
    
    
    for i in range(len(temp)):
        for j in range(len(temp[i])):
			if i == 0 or j == 0: 
                temp[i][j] = 0
            
            elif s1[i-1]==s2[j-1]:
                
                temp[i][j] = temp[i - 1][j - 1] + 1
               
            else:
                
                if(temp[i][j-1]> temp[i-1][j]):
                    temp[i][j] =  temp[i][j-1]
                else:
                    temp[i][j] = temp[i-1][j]
                
            if temp[i][j]> maxm:
                maxm = temp[i][j]
    

    return maxm
	
s1 = 'a'
s2 = 'aa'
print(lcs(s1,s2))