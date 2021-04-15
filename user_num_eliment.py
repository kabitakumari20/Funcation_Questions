def name(num,list):
	i=0
	while i<len(list):
		if num==i:
			print(list[i])
		i=i+1
list=["kabita","komal","mahi","manvi"]
num=int(input("enter the num="))
name(num,list)