# Default arguments
# example1
def surv(name, area="ylm"):
    print("Name:",name)
    print("Area:",area)
    return
surv("Bhanu","vizag")
# if i not declared the parameter for area it will take the default value as ylm 
surv("Charan")

# example2
def percentage(name,marks,max_marks=100):
    print("Name:",name)
    print("marks:",marks)
    tpercent= (marks/max_marks)*100
    print("Total percentage:",tpercent)
    return tpercent
marks= 80
tpercent= percentage("bhanu",marks,200)

marks= 90
tpercent= percentage("charan",marks)

# example3
def std_list(name, marks, grade="F"):
    print("Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)
    return
std_list("Bhanu", 85, "A")
std_list("Charan", 90)  # Will use default grade "F"