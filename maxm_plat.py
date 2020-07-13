# arr = [9:00, 9:40, 9:50, 11:00, 15:00, 18:00]
# dep = [9:10, 12:00, 11:20, 11:30, 19:00, 20:00]

#https://www.faceprep.in/procoder/knowledgebase/minimum-number-of-platforms-required-for-a-railwaybus-station/

arr = ['9:00', '9:40', '9:50', '11:00', '15:00', '18:00']

dep = ['9:10', '12:00', '11:20', '11:30', '19:00', '20:00']
c = 0
cmax = 1

#print(arr)
#print(dep)

for i in range(len(arr)):
	arr[i] = int(arr[i].replace(':',''))
	dep[i] = int(dep[i].replace(':',''))


#print(arr)
#print(dep)
a=0
d=0

time = arr + dep
time.sort()
dep.sort()

for i in range(len(time)):
	#print(time[i])
	if(a!=len(arr) and d!=len(dep) and arr[a]==dep[d] and arr[a]==time[i]):
		a += 1
		d += 1
	elif(a!=len(arr) and arr[a]==time[i]):
		print('+')
		a += 1
		c += 1
		if(cmax<c):
			cmax = c
	elif(d!=len(dep) and dep[d]==time[i]):
		print('-')
		d += 1
		c -= 1

		
print(cmax)