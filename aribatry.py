# def student(*names):
# 	for name in names:
# 		print("they are  doing well",names)
# student("kaju")
# student("raju")
# i
# num=int(input("enter the num="))
# def prime(num):
#     i=2
#     while i<num:
#         b=2
#         while b<i:
#             if i%b==0:
#                 # return -1
# 				print(i,"it is not prime")
                
#             b=b+1
#         else:
#             # return i
# 			print(i,"it is prime")
#         i=i+1
# prime(3)i=2

# num=int(input("enter the num="))
# def prime():
# 	num=int(input("enter the num="))
# 	i=2
# 	while i<=num:
# 		b=2
# 		while  b<i:
# 			if i%b==0:
# 				print(i,"it is not prime")
# 				# return -1
# 				break
# 			b=b+1
# 		else:
# 			print(num,"it is prime num")
# 			# break
# 			# return i
# 		i=i+1
# prime()		


# num=int(input("enter the num="))
# i=2
# while i<=num:
# 	if num%i==0:
# 		print(num,"it is prime num")
# 		# break
# 	i=i+1
# else:
# 	print("it is not prime num")


def prime():
	i=int(input("enter the num="))
	b=2
	while b<i:
		if i%2==0:
			# print("it is not prime num",i)
			# break
			return -1
		b=b+1
	else:
		# print("it is prime num",i)
		b=i
		return b
prime()
