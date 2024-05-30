num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num

while temp>0:
    digit = temp%10
    sum = sum+digit**order
    temp = temp//10

if num == sum:
    print("Number is armstrong")

else:
    print("number is not armstrong")
    