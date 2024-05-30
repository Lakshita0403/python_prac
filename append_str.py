s1 = str(input("enter string: "))
print("original string 1: " , s1)

s2 = str(input("enter string: "))
print("original string 2: " , s2)

mid = int(len(s1)/2)

s3 = s1[:mid]+s2+s1[mid:]
print("New string is : ", s3)