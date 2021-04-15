# def squares():
# 	i=1
# 	c=[ ]
# 	while i<len(a):
# 		b=i*i
# 		print(b)
# 		i=i+1
# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# squares()

def dic_squares(num):
    i=1
    while i<=num:
        dic[i]=[i*i]
        i=i+1
dic={}
dic_squares(20)       
print(dic)