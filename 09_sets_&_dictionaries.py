# sets are mutable
# sets are unordered collections of unique elements
# sets are defined using curly braces or the set() constructor
# duplicates will be removed defaultly while accessing the set in sorted order
# sets are iterable
# functins like add(), remove(), discard(), pop() can be used to manipulate sets
# And perform set operations like union(|), intersection(&), difference(-), symmetric difference(^)
# set operations
set1 = {1,2,2,3,4,5,6}
set2 = {1,2,7}
set3 = {1,2,3,4,5,6,8}
set = set1 | set2 | set3
print(set)  # union
set = set1 & set2 & set3
print(set) # intersection
set = set1 - set2 - set3
print(set)  # difference
set = set1 ^ set2 ^ set3
print(set,)  # symmetric difference
# set functions
set1.add(10)  # add
print(set1) 
set1.remove(2) # remove
print(set1)  
set1.discard(3)  # discard
print(set1)
set1.pop()  # pop
print(set1)  
# dictionaries are mutable
# dictionaries are unordered collections of key-value pairs
# dictionaries are defined using curly braces or the dict() constructor
# dictionary operations
# the methods like keys(), values(), items(), get(), update(), pop(), popitem(), clear() 
dict1={'name' : 'bhanu', 'age': 18, 'city' : 'vizag'}
print(dict1)  
# accessing values using keys
print(dict1['name'])   # or we can access using dict1.get('name')
print(dict1['age'])    #or we can access using dict1.get('age')
dict1.update({'country': 'India'})  
print(dict1) 
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1.get('city'))  
print(dict1.pop('age'))  
print(dict1.clear())
