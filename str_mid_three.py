n = str(input("enter string: "))
print("original string: " , n)

l = len(n)
mid = int(l/2)
# res = n[mid-1]+n[mid]+n[mid+1]

# string slicing

res = n[mid-1: mid+2]
print("New string is : ", res)