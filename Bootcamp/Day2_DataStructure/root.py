# List - ordered, changeble, allow duplicates
# functions in lists are append(), extend(), insert(), remove(), pop(), sort(), reverse(), index(), count()
num = [1,2,3,4,5,6]
num1 = [8,9,1.0]
print(num)
num.append(7)
num.insert(1,4)
num1.remove(1.0)
num.extend(num1)
num.pop(9)
num.reverse()
print(num)
num.sort()
print(num)
names = ['bhanu','charan','anil','bhanu']
print(names[0])
print(names[1])
print(names[2])
print(names.index('anil'))
print(names.count('bhanu'))

# Tuple - ordered, unchangeable, allow duplicates
# functions in tuples are len(), count(), index(), max(), min(), sum(), sorted()
n = (2,1,3)
print(n)
print(len(n))
print(max(n))
print(min(n))
print(sum(n))
print(n.index(3))
print(n.count(3))
print(sorted(n))

# Sets - unordered, no duplicates
# functions in sets are add(), update(), remove()-error if element not found, discard()-no error if elment is not found, pop(), clear(), union(), intersection(), difference(), issubset(), issuperset()
set1 = {1,2,3}
set2 = {3,4,5}
set1.add(4)
set2.add(2)
print(set1)
print(set2)
set1.update([6,7,8])
set2.update({1,9})
print(set1)
print(set2)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1)
print(set2)
print(set1.difference(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))

# Dictionaries - key-value pairs
# functions in dict. are keys(), values(), items(), get(), pop(), update()
dict1 = {1:"bhanu", 2:"charan", 3:"anil"}
dict2 = {"tulasi":4, "srinivas":5, "suresh":6}
print(dict1.keys())
print(dict1.values())
print(dict1[1])
print(dict2["tulasi"])
print(dict1.items())
print(dict1.get(3))
dict1.update({4: "kalla"})
print(dict1)
# nested dict
dict3 = {
    "name"   : "bhanu",
    "marks"  : {"maths": 80, "physics": 85},
    "section": "CSD",
    "age"    :  18
}
print(dict3["marks"]["maths"])


