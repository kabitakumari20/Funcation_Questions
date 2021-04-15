def dublicate():
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