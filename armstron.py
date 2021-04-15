def armstrog():
    num3=int(input("enter the num="))
    sum2=0
    b=num3
    while num3>0:
	    rem=num3%10
	    var=rem**3
	    sum2=sum2+var
	    num3=num3//10
    print(sum2)
    if sum2==b:
        return "armstrong"
    else:
	    return "not"

print(armstrog())

