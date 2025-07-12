# control flows
# iterative statements
# match statement

# for loop
print("printing name using for loop:\n")
name = "Bhanu"
for i in name:
    print(i,end="\t")
# Now adding keywords like break and continue
# using continue statement
print("\nUsing continue statement in for loop:\n")
for i in name:
    if i=="h":
        continue
    print(i)
# using break statement
print("\nUsing break statement in for loop:\n")

for i in name:
    if i=="u":
        break
    print(i)
# printing even numbers in a range of 1 to 10 numbers
print("\nprinting even numbers in a range of 1 to 10 numbers:\n")
for i in range(1,5):
    if i%2==0:
        print(i, end="\t")

# while loop
print("\nprinting numbers from 1 to 5 using while loop:\n")
i=1
while i<=5:
    print(i ,end="\t")
    i+=1
# match  cases
print("\nprinting odd numbers from 1 to 10 using match statement:\n")
def odd_number(n):
    match n:
        case 1:
            return True
        case 3:
            return True
        case 5:
            return True
        case 7:
            return True
        case 9:
            return True
        case _:
            return False
print(odd_number(1))
print(odd_number(2))
print(odd_number(3))