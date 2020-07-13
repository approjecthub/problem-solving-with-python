str1 = 'aab'
str2 = 'axy'

str3 = 'aaxaby'

T = [ [ 0 for i in range(len(str1)+1) ] for j in range(len(str2)+1) ] #dimension : len(str1)X len(str2)
T[0][0] = True

for i in range(1, len(str1)+1):
  if str3[i-1] == str1[i-1]:
    T[0][i] = T[0][i-1]
  else:
    T[0][i] = False

for j in range(1, len(str2)+1):

  if str3[j-1] == str2[j-1]:
    T[j][0] = T[j-1][0]
  else:
    T[j][0] = False
	
for i in range(1, len(str2)+1):
  for j in range(1, len(str1)+1):
    if str3[i+j-1] == str2[i-1]:
      T[i][j] = T[i-1][j]
    elif str3[i+j-1] == str1[j-1]:
      T[i][j] = T[i][j-1]
    else:
      T[i][j] = False

print(T[len(str2)][len(str1)])  #ans