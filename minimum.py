def min():
    a=[2,3,1,4,5,6]
    i=0
    min=a[0]
    while i<len(a):
        if a[i]<min:
            min=a[i]
        i=i+1
    print(min)
min()