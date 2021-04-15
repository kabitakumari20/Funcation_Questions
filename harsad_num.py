
def harsad(num):
    n=num
    sum1=0
    rem=0
    while num>0:
        rem=num%10
        sum1=sum1+rem
        num=num//10 
        print(sum1)
    res=n%sum1
    if res==0:
        print("it is harsad num",n)
    else:
        print("it is not harsad num",n)
num=int(input("enter the num="))
harsad(num)
