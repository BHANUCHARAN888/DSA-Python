# List are changeable,Tuples are not
# lists are present in sruarebrackets [], whereas tuples are in rounded brackets ()
list=[1,2,5,4,3]
print(list)
# Accessing some methods using list
print("Accessing some methods using list:")
list.append(6)
print(list)
list.insert(0,6)
print(list)
print(list.count(6))
list.remove(6)
print(list)
list.reverse()
print(list)
list.sort()
print(list)
list.clear()
print(list)
# Accessing some methods using tuple
print("Accessing some methods using tuple:")
tuple=(1,2,2,3,4,5)
print(tuple)
# Accessing some methods using tuple
# tuples does not support methods like append, insert, remove, reverse, sort, clear  
print(tuple.count(2))
print(tuple.index(3))