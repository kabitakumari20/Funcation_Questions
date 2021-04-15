# def add_num(num1,num2):
# 	a=num1+num2
# 	print(a)
# add_num(4,5

# def harsad(num):
#     n=num
#     sum=0
#     rem=0
#     while num>0:
#         rem=num%10
#         sum=sum+rem
#         num=num//10 
#         print(sum)
#         res=n%sum
#     if res==0:
#         print("it is harsad num",n)
#     else:
#         print("it is not harsad num",n)
# num=int(input("enter the num="))
# harsad()


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

def armstrog():
	num=int(input("enter the num="))
	sum1=0
	b=num
	while num>0:
		rem=num%10
		var=rem**3
		sum1=sum1+var
		num=num//10
	print(sum1)
	if sum1==b:
		print(sum1,"it is armstron num")
	else:
		print(sum1,"it is not armstrong num")

armstrog()
# num=int(input("enter the num"))
# sum=0
# b=num
# while num>0:
#     rem=num%10
#     var=rem**3
#     sum=sum+var
#     num=num//10
# print(sum)
# if sum==b:
#     print(sum,"it is armstron num")
# else:
#     print(sum, "it is not armstrong num")


def prime():
    i=2
    while i<num:
        b=2
        while b<i:
            if i%2==0:
                print("it is not prime num",i)
                break
            b=b+1
        else:
            print("it is prime num",i)
        i=i+1
num=int(input("enter the num="))
prime()

def main():
    print(prime(num))


   


 