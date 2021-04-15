def student_max():
    i=0
    b=[]
    while i<len(a):
        j=0
        max=0
        while j<len(a[i]):
            if a[i][j]>max:
                max=a[i][j]
            j=j+1
        b.append(max)
        print(b)
a=[[54,21,42,63],[12,42,42,53],[42,90,78,13],[94,84,78,76],[87,55,98,99]]
student_max()