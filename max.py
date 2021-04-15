def list():
    i=0
    max=(a[0])
    while i<len(a):
        if a[i]>max:
            max=a[i]
        i=i+1
    print(max)
a=[34,56,78,34,67,90]
list()
