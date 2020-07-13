##https://www.geeksforgeeks.org/distribute-n-candies-among-k-people/

n = 10
k = 3

li = [0]*k

i=0
j=0
while n>0:

	i += 1
	
	if(j==k):
		j = 0
	if n>=i:
		n -= i
	else:
		i =n
		n=0

	li[j] +=i
	j += 1

		
print(li)