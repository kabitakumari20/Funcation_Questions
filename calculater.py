def calculte(a,b,symbol):
	if symbol=="*":
		c=(a*b)
        return c
	elif symbol=="+":
		c=(a+b)
        return c
	elif symbol=="-":
		c=(a-b)
        return c
	elif symbol=="/":
		c=(a/b)
        return c
	elif symbol=="%":
		c=(a%b)
        return c
	elif symbol=="//":
		c=(a//b)
        return c
	else:
		print("nothing")
	return c
a=int(input("enter the num="))
b=int(input("enter the num="))
symbol=input("enter the symbol=")
print(calculte(a,b,symbol))


# def calculte(a,b,symbol):
# 	if symbol=="*":
# 		print(a*b)
# 	elif symbol=="+":
# 		print(a+b)
# 	elif symbol=="-":
# 		print(a-b)
# 	elif symbol=="/":
# 		print(a/b)
# 	elif symbol=="%":
# 		print(a%b)
# 	elif symbol=="//":
# 		print(a//b)
# 	else:
# 		print("nothing")
# a=int(input("enter the num="))
# b=int(input("enter the num="))
# symbol=input("enter the symbol=")
# calculte(a,b,symbol)