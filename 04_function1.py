# functions
# User defined functions
# With-out return type
def func():
    print("hello everyone..")
func()

# With return type
def func1():
    return "hello everyone.."
func1()
print(func())

def sum(a,b):
    return a+b
result=sum(10,20)
print(result)
# With arguments
def op(*, n, m):
    print(n * m)
print(op(n=10, m=20))

# parameters, which the variable defined in function.
# arguments, which the variable defined while calling the function(actual value).