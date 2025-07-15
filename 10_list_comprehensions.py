# Basic syntax for list comprehensions
# variable= [expression for item in iterable if condition]
# Example 1: Create a list of squares of even numbers from 0 to 9
square = [x**2 for x in range(0 ,10) if x % 2 ==0]
print(square)
# Example 2: Create a list of tuples (number, square) for numbers from 0 to 9
tuple = [(x,x**2) for x in range(0, 10)]
print(tuple)
# Example 3: Create a list of characters from a string
string='independence'
list=[char for char in string]
print(list)
# Example 4: Create a list of numbers from 0 to 9 that are not divisible by 3
list1=[x for x in range(0,10) if x % 3 != 0]
print(list1)
# Example 5: Combine two lists
list2 = [1, 2, 3]
list3 = [4, 5, 6]
combined = [(x, y) for x in list2 for y in list3]
print(combined)