s = [3,4,-1,0,6,2,3]
lis = [1]*len(s)
ans = 1
for i in range(1, len(s)):
	for j in range(i):
		if s[j]<s[i]:
			lis[i] = max(lis[i], 1+lis[j])
			ans = max(lis[i], ans)
			
print(ans)
			
			
