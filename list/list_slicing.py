List = ['G', 'E', 'E', 'K', 'S', 'F', 
        'O', 'R', 'G', 'E', 'E', 'K', 'S'] 
print(List) 
  
# Print elements of a range 
# using Slice operation 
Sliced_List = List[3:8] 
print(Sliced_List) 
  
# Print elements from a 
# pre-defined point to end 
Sliced_List = List[5:] 

print(Sliced_List) 
  
# Printing elements from 
# beginning till end 
Sliced_List = List[:] 
print(Sliced_List) 

print('\n')

p = List[:-6]
print(p)

p = List[-6:-1]
print(p)

p  =List[::-1]
print(p)