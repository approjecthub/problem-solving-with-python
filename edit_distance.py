str1 = 'abcdef'
str2 = 'azced'

dp = [ [ 0 for i in range(len(str1)+1) ] for j in range(len(str2)+1) ]

for i in range(len(dp[0])):
  dp[0][i] = i
  
for i in range(len(dp)):
  dp[i][0]= i
  
for i in range(1,len(str2)+1):
  for j in range(1, len(str1)+1):
    if str2[i-1] == str1[j-1]:
      dp[i][j] = dp[i-1][j-1]
    
    else:
      dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1
	  
print('ans : ', dp[len(str2)][len(str1)])