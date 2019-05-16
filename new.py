a = [[1,2,3],[2,3,4]]
b = []
i =0
j=0
while(i<len(a)):
	j = 0
	while(j<len(a[i])):
		b.append(a[i][j])
		j = j + 1
	i = i + 1
b.sort()
med = len(b)/2
med = int(med)
print(b[med])

