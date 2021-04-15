def sum(num1,num2):
    add_value = num1+num2
    return add_value
def sub(num1,num2):
    sub_value=num1-num2
    return sub_value
def mult(num1,num2):
    mult_value=num1*num2
    return mult_value
def div(num1,num2):
    div_value=num1/num2
    return div_value
def flor(num1,num2):
    flor_value=num1//num2
    return flor_value
def excponent(num1,num2):
    excpo_value=num1**num2
    return excpo_value
def moduls(num1,num2):
    modul_value=num1%num2
    return modul_store
num1=int(input("enter the num1="))
num2=int(input("enter the num2="))
oprater=input("enter the oprater=")
# print(sum(num1,num2))
def main():
    if oprater=="+":
        print(sum(num1,num2))
    elif oprater=="-":
        print(sub(num1,num2))
    elif oprater=="/":
        print(div(num1,num2))
    elif oprater=="//":
        print(flor(num1,num2))
    elif oprater=="%":
        print(moduls(num1,num2))
    elif oprater=="*":
        print(mult(num1,num2))
    elif oprater=="**":
        print(excponent(num1,num2))
        return value
main()
