def new():
	i=0
	b=[ ]
	while i<len(a):
		if a[i] not in b:
			b.append(a[i])
		i=i+1
	print(b)
a=[1,5,10,12,16,20,1,2,10,13,16]
new()