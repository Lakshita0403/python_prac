# using remove method

l = [1,2,3,4,5,6,8,9,6,4]
print(l)
l.remove(4)
l.remove(6)
print(l)

List = [1, 2, 3, 4, 5, 6, 
        7, 8, 9, 10, 11, 12] 

for i in range(1,5):
    List.remove(i)

print(List)

#  using pop method

li = [1,3,4,5]
print(li)
li.pop(3)
print(li)
li.pop()
print(li)
