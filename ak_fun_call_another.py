def odd(list):
    i=0
    a=[]
    while i<len(list):
        if list[i]%2!=0:
            a.append(list[i])
        i+=1
    return a
list=[1,2,3,4,5,6,7,8,9]
d=odd(list)
def greater(d):
    j=0
    while j<len(d):
        if d[j]>3:
            print(d[j])
        j+=1
greater(d)
print(d)
