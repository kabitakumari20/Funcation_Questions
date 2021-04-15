def student_budjet():
    total_kharcha=student*kharcha
    if total_kharcha<=50000:
        print("ham budjet ke under hai")
    else:
        print("ham budjet ke bahar hai")
    print(total_kharcha)
student=int(input("enter the num of students: "))
kharcha=int(input("enter the 1 student kharcha: "))
student_budjet()