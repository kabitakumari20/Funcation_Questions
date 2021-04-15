# def primeorNot(num):     
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break
#             else:
#                 print(num,"is a prime number")

#     else:
#            print(num,"is not a prime number")
# primeorNot(int(input())) 



def prime():
    num=int(input("enter the num4="))
    i=2
    c=1
    while i<=num:
        if num%i==0:
            c+=1
        i+=1
    if c==2:
        return(num,"primre")
    else:
        return(num,"not prime")
print(prime())
