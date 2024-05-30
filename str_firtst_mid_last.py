n = str(input("enter string: "))
print("original string: " , n)

res = n[0]
l = len(n)
mid = int(l/2)
res= res+n[mid]
res = res+n[l-1]
print("New string: ", res)
