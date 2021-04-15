def mult(a,b):
    i=0
    c=[]
    multi=0
    while i<len(b):
        multi=a[i]*b[i]
        c.append(multi)
        i=i+1
    print(c)
a=[5, 10, 50, 20]
b=[2, 20, 3, 5] 
mult(a,b)