num = int(input("Enter a number: "))
flag = False
  
if num == 1:
  print(f"{num} is not prime")
elif num>1:
  for i in range(2, num):
    if(num%i) == 0:
        flag = True
        break 

  if flag:
    print("not prime")

  else:
    print("prime")   