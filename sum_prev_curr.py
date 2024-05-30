# x = int (input("enter num:"))
previous_num = 0

for i in range (1,11):
    sum = previous_num+i
    print("current no. = ", i, " previous no. = ", previous_num," sum = ", sum)
    previous_num = i