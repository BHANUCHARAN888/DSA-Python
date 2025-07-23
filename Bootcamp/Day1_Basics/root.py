# Data types
# int      1,2,3,4.. 
# float    1.1,1.2,..
# string   'bhanu',"charan"
# bool     True,False
# List     [1,2,3,4]
# Tuple    (1,2,3,4)
# set      {1,2,3,4}
# Dict     {'a':1, 'b':2, 'c':3}

# Conditions & Loops
x=5
if x > 10:
    print("x is greater than 10")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is equal to 0")
# for Loop
for i in range(5):
    print(i)
# while loop
i=0
while i<5:
    print(i)
    i+=1

# Functions
# basic function
def greet(name):
    return f"Hello {name}"
print(greet('Bhanu'))
# or
def greet(name):
    return print(f"Hello {name}")
greet('everyone')
# function with default arg
def solve(x,y=2):
    return x ** y
print(solve(2))
print(solve(2,3))
# lambda function
# 1
square = lambda x: x*x
print(square(5))
# 2
add = lambda x, y: x + y
print(add(2, 3))
# 3
student = [('bhanu', 20),('charan', 22),('anil', 21)]
sort=sorted(student, key=lambda x:x[1])
print(sort)
# 4
cube = lambda x: x*x*x
print(cube(3))

