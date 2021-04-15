def perfect():
    i=1
    sum=0
    while i<num:
        if num%i==0:
            sum=sum+i
        i=i+1
    if sum==num:
        print("it is perfect num",i)
    else:
        print("it is not perfect num",i)
num=int(input("enter the num="))
perfect()