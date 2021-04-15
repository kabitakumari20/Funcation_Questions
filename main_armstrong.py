# num1=int(input("enter the num1="))
# num2=int(input("enter the num2="))
# num3=int(input("enter the num3="))
# num4=int(input("enter the num4="))



def harsad():
    num=int(input("enter  the harsad="))
    store_num=num
    sum1=0
    remainder=0
    while num>0:
        remainder=num%10
        sum1=sum1+remainder
        num=num//10 
    reminder1=store_num%sum1
    if reminder1==0:
        print("it is hearsad num, because num is  divisiable by digit of sum")
        return store_num
    else:
        print("not hearsad,because num is not divisiable by digit of sum")
        return store_num
        # return n
# print(harsad(156))


def perfect():
    num=int(input("enter the perfect="))
    index=1
    sum=0
    while index<num:
        if num%index==0:
            sum=sum+index
        index=index+1

    if sum==num:
        print("perfect, num of facter's sum equal equal num")
        return sum
    else:
        print("not a perfect,num of facter's sum not equal num")
        return num
# print(perfect())
        

def armstrog():
    num3=int(input("enter the armstrong="))
    sum2=0
    store_num=num3
    while num3>0:
	    reminder=num3%10
	    que=reminder**3
	    sum2=sum2+que
	    num3=num3//10
    print(sum2)
    if sum2==store_num:
        print("armstrong,because it's digit's que's sum = ", num3)
        return sum2
    else:
        print("not a armstrong,because it's digit's que's sum not equal ",num3)
        return store_num

# print(armstrog())



def prime():
    num=int(input("enter the prime="))
    index=2
    count=1
    while index<=num:
        if num%index==0:
            count+=1
        index+=1
    if count==2:
        print("prime, because it's divisiable by only 1 and itself")
        return(num)
    else:
        print("not prime,it is divisiable by nactureal numbers")
        return num
# print(prime())


def main_max():
    empty=[]
    empty.append(harsad())
    empty.append(perfect())
    empty.append(armstrog())
    empty.append(prime())
    index=0
    max=0
    while index<len(empty):
        if empty[index]>max:
            max=empty[index]
        index=index+1
    return max,"it is max number"
empty1=main_max()
print(empty1)
   


 