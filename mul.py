

def mul_or_sum(num1, num2):
    num3 = num1*num2
    num4 = num1+num2

    if(num3<=1000):
        print(num3)
    else:
        print(num4)    


num1 = int(input("enter 1st num: "))
num2 = int(input("enter 2nd num: "))
mul_or_sum(num1, num2)
