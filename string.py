def string():
    i=0
    b=[]
    count=0
    while i<len(a):
        if a[i] not in b:
            b.append(a[i])
            count=count+1
        i=i+1
    print(b)
a = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"] 
string()