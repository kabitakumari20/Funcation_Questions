def dublicate():
	i=0
	c=[ ]
	while i<len(a):
		j=0
		while j<1:
			if a[i] in b:
				c.append(a[i])
			j=j+1
		i=i+1
	print(c)
a=[1,342,75,23,98]
b=[75,23,98,12,78,10,1]
dublicate()


#.........................................................



ef dublicate():
    i=0
    a=[]
    while i<len(n)-1:
        j=i+1
        while j<len(n):
            if n[i]==n[j]:  
                a.append(n[i])
            j=j+1
        i+=1
    print(a)     
n= [1, 342, 75, 23, 98,75, 23, 98, 12, 78, 10, 1]
dublicate()