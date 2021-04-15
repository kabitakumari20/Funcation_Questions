def harsad(num):
    num=int(input("enter  the num="))
    n=num
    sum1=0
    rem=0
    while num>0:
        rem=num%10
        sum1=sum1+rem
        num=num//10 
    res=n%sum1
    if res==0:
        return "harsad"
    else:
        return "not"
print(harsad(156))
