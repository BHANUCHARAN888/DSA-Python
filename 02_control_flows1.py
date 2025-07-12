#control flows
# if-else statement
a=10
b=20
if a > b:
    print("a is greater than b")
else:
    print("a is less than b")
# if-elif-else statement
c=30
if a > c:
    print("a is greater than c")
elif b > c:
    print("b is greater than c")
else:
    print(" c is greater than a and b")
# nested if-else statements
marks = 60
if marks >= 90:
    print("Grade A")
elif marks >= 85:
    print("Grade B")
elif marks >= 80:
    print("Grade C")
elif marks >= 75:
    print("Grade D")
elif marks >= 70:
    print("Grade E")
else:
    print("Grade F")
# if-else statements for basic functions
def odd_even(n):
    if n % 2 ==0:
        return "Even"
    else:
        return "Odd"
print(odd_even(10))
print(odd_even(20))
print(odd_even(30))
print(odd_even(99))